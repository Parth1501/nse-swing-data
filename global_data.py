"""
Global market numbers for the morning list's "Global & season" box (runs on GitHub Actions).

The morning routine's web fetcher is blocked by most news sites, so it often can't find two
sources for Brent, USD/INR, Hang Seng, GIFT Nifty and FII/DII. This script reads them from
machine-readable feeds instead and writes data/global.json. Each item carries its own value,
the date/time the value is for, and a second feed's value as a cross-check where one exists.

Feeds:
  Yahoo Finance (yfinance)   S&P 500, Nasdaq, Nikkei, Hang Seng, Brent, USD/INR, US 10-yr
  Stooq (CSV)                second feed for the same, where it has the instrument
  US Treasury (CSV)          official US 10-yr par yield
  NSE (JSON API)             provisional FII/FPI and DII net cash-market flows
Nothing here is invented: an item that a feed doesn't return is written with value null and
the error, so the morning list shows "not verified today" for it.
"""
import io
import json
import os
from datetime import datetime, timedelta, timezone

import pandas as pd
import requests
import yfinance as yf

IST = timezone(timedelta(hours=5, minutes=30))
OUT = os.path.join("data", "global.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
AGREE_PCT = 1.0                       # two feeds agree when within 1% (same rule as the morning list)

# name -> (Yahoo symbol, Stooq symbol or None, decimals)
MARKETS = {
    "S&P 500": ("^GSPC", "^spx", 2),
    "Nasdaq Composite": ("^IXIC", "^ndq", 2),
    "Nikkei 225": ("^N225", "^nkx", 2),
    "Hang Seng": ("^HSI", "^hsi", 2),
    "Brent crude (front-month future, $/bbl)": ("BZ=F", "cb.f", 2),
    "USD/INR": ("INR=X", "usdinr", 4),
    "US 10-yr yield (%)": ("^TNX", "10usy.b", 3),
}


def pct(a, b):
    return None if a is None or b in (None, 0) else round((a / b - 1) * 100, 2)


def yahoo(sym):
    """Last two daily closes (the last one may be a session still in progress) and a month-ago close."""
    h = yf.Ticker(sym).history(period="2mo", interval="1d", auto_adjust=False)
    h = h.dropna(subset=["Close"])
    if len(h) < 2:
        raise ValueError("fewer than 2 daily bars")
    last, prev = h.iloc[-1], h.iloc[-2]
    month_ago = h[h.index <= h.index[-1] - pd.Timedelta(days=30)]
    return {
        "value": float(last["Close"]),
        "prev_close": float(prev["Close"]),
        "bar_date": h.index[-1].strftime("%Y-%m-%d"),
        "prev_date": h.index[-2].strftime("%Y-%m-%d"),
        "month_ago": float(month_ago["Close"].iloc[-1]) if len(month_ago) else None,
    }


def stooq(sym):
    r = requests.get(f"https://stooq.com/q/l/?s={sym}&f=sd2t2c&h&e=csv",
                     headers={"User-Agent": UA}, timeout=20)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    row = df.iloc[0]
    c = row.get("Close")
    if pd.isna(c) or str(c).upper() == "N/D":
        raise ValueError(f"no data: {r.text.strip()[:120]}")
    return {"value": float(c), "date": str(row.get("Date")), "time": str(row.get("Time"))}


def treasury_10y():
    year = datetime.now(IST).year
    url = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
           f"daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve"
           f"&field_tdr_date_value={year}&page&_format=csv")
    r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    last, prev = df.iloc[-1], df.iloc[-2]
    return {"value": float(last["10 Yr"]), "prev_close": float(prev["10 Yr"]),
            "date": last["Date"].strftime("%Y-%m-%d"), "source_url": url}


def nse_fii_dii():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "*/*", "Referer": "https://www.nseindia.com/reports/fii-dii"})
    try:
        s.get("https://www.nseindia.com/reports/fii-dii", timeout=15)
    except Exception:
        pass
    url = "https://www.nseindia.com/api/fiidiiTradeReact"
    r = s.get(url, timeout=30)
    r.raise_for_status()
    out = {}
    for row in r.json():
        cat = str(row.get("category", "")).upper()
        key = "FII/FPI" if "FII" in cat or "FPI" in cat else "DII" if "DII" in cat else None
        if key:
            out[key] = {"net_cr": float(str(row["netValue"]).replace(",", "")),
                        "buy_cr": float(str(row["buyValue"]).replace(",", "")),
                        "sell_cr": float(str(row["sellValue"]).replace(",", "")),
                        "date": datetime.strptime(row["date"], "%d-%b-%Y").strftime("%Y-%m-%d")}
    if not out:
        raise ValueError("no FII/DII rows")
    return out, url


def main():
    now = datetime.now(IST)
    items = []
    for name, (ysym, ssym, dp) in MARKETS.items():
        it = {"name": name, "value": None, "for_date": None, "change_pct": None,
              "source": f"Yahoo Finance {ysym}", "source_url": f"https://finance.yahoo.com/quote/{ysym}",
              "check_source": None, "check_value": None, "agree": None, "errors": []}
        try:
            y = yahoo(ysym)
            it.update(value=round(y["value"], dp), for_date=y["bar_date"], prev_close=round(y["prev_close"], dp),
                      prev_date=y["prev_date"], change_pct=pct(y["value"], y["prev_close"]))
            if y["month_ago"] and name.startswith("Brent"):
                it["change_1m_pct"] = pct(y["value"], y["month_ago"])
        except Exception as e:
            it["errors"].append(f"Yahoo: {e}")
        if ssym:
            try:
                s = stooq(ssym)
                it.update(check_source=f"Stooq {ssym}", check_value=s["value"],
                          check_url=f"https://stooq.com/q/?s={ssym}", check_date=f'{s["date"]} {s["time"]}')
            except Exception as e:
                it["errors"].append(f"Stooq: {e}")
        if it["value"] is not None and it["check_value"] is not None:
            it["agree"] = abs(pct(it["value"], it["check_value"])) <= AGREE_PCT
        items.append(it)

    try:                                   # official US Treasury yield replaces the Stooq cross-check
        t = treasury_10y()
        it = next(i for i in items if i["name"].startswith("US 10-yr"))
        it.update(check_source="US Treasury par yield curve", check_value=t["value"],
                  check_url=t["source_url"], check_date=t["date"])
        if it["value"] is not None:
            it["agree"] = abs(it["value"] - t["value"]) <= 0.05      # within 5 bp
    except Exception as e:
        next(i for i in items if i["name"].startswith("US 10-yr"))["errors"].append(f"Treasury: {e}")

    fii = {"source": "NSE provisional FII/DII (cash market)", "source_url": "https://www.nseindia.com/reports/fii-dii"}
    try:
        rows, url = nse_fii_dii()
        fii.update(rows)
        fii["api_url"] = url
    except Exception as e:
        fii["error"] = str(e)

    out = {"generated_at_ist": now.strftime("%Y-%m-%d %H:%M"), "items": items, "fii_dii": fii}
    os.makedirs("data", exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    for it in items:
        print(f'{it["name"]:42} {it["value"]!s:>12} {it["for_date"]!s:>11} chk={it["check_value"]!s:>12} '
              f'agree={it["agree"]} {"; ".join(it["errors"])}')
    print("FII/DII:", json.dumps({k: v for k, v in fii.items() if k in ("FII/FPI", "DII", "error")}))


if __name__ == "__main__":
    main()
