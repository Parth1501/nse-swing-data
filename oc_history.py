"""
Nifty option chain history from NSE's end-of-day F&O bhavcopy (runs on GitHub Actions; NSE
blocks most other networks).

The 30-minute snapshots in data/option_chain/ only start on 14 Oct 2026, which is far too little
to learn anything from. NSE publishes one file per trading day with every option contract's close,
settlement price, OI, change in OI and volume, going back years. This script saves the Nifty part
of it, in the same shape as the snapshots (one row per strike, CE and PE side by side), for the
same two expiries the snapshots keep: the nearest (weekly) one and the monthly one (the last
expiry of its month; when the nearest is itself monthly, next month's). Strikes further than 12%
from spot are dropped. Only NSE's numbers are saved; IV and everything else is worked out by
oc_learn.py.

One file per month: data/option_chain_eod/YYYY-MM.csv. Days already saved are skipped, so a run
only fetches what is missing. Usage:
  python oc_history.py                  # from the day after the last saved day up to today
  python oc_history.py 2024-11-20       # from this date (days already saved are still skipped)
"""
import csv
import io
import os
import sys
import time
import zipfile
from datetime import date, datetime, timedelta, timezone

import requests

IST = timezone(timedelta(hours=5, minutes=30))
OUT_DIR = os.path.join("data", "option_chain_eod")
SYMBOL = "NIFTY"
# After SEBI's Nov 2024 rule (one weekly expiry per exchange) Nifty weeklies look the way they do
# now; older data comes from a different market and is not fetched by default.
DEFAULT_START = date(2024, 11, 20)
URL = "https://nsearchives.nseindia.com/content/fo/BhavCopy_NSE_FO_0_0_0_{d:%Y%m%d}_F_0000.csv.zip"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
BAND = 0.12
SIDE_FIELDS = (("ltp", "ClsPric"), ("settle", "SttlmPric"), ("oi", "OpnIntrst"),
               ("chg_oi", "ChngInOpnIntrst"), ("volume", "TtlTradgVol"))
COLUMNS = (["date", "spot", "expiry", "expiry_type", "strike"]
           + [f"{side}_{name}" for side in ("ce", "pe") for name, _ in SIDE_FIELDS])


def session():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
                      "Referer": "https://www.nseindia.com/"})
    try:
        s.get("https://www.nseindia.com", timeout=15)
    except Exception:
        pass
    return s


def download(s, d):
    """The day's bhavcopy as CSV text, or None when NSE has no file (holiday, not out yet)."""
    for i in range(3):
        try:
            r = s.get(URL.format(d=d), timeout=60)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                return z.read(z.namelist()[0]).decode("utf-8", "replace")
        except Exception as e:
            print(f"{d}: try {i + 1} failed: {e}")
            time.sleep(5 * (i + 1))
    raise RuntimeError(f"{d}: NSE did not answer")


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def pick_expiries(expiries, d):
    """{expiry: 'weekly'|'monthly'}, the same rule as option_chain.py."""
    ds = sorted(e for e in expiries if e >= d)
    if not ds:
        return {}
    last_of_month = {}
    for e in ds:
        last_of_month[(e.year, e.month)] = e
    monthly = next((e for e in sorted(last_of_month.values()) if e > ds[0]), None)
    out = {ds[0]: "weekly"}
    if monthly:
        out[monthly] = "monthly"
    return out


def nifty_rows(text, d):
    rd = csv.DictReader(io.StringIO(text))
    need = {"TckrSymb", "FinInstrmTp", "XpryDt", "StrkPric", "OptnTp", "UndrlygPric"}
    if not need <= set(rd.fieldnames or []):
        raise RuntimeError(f"{d}: unexpected bhavcopy columns: {rd.fieldnames}")
    legs = [r for r in rd if r["TckrSymb"].strip() == SYMBOL and r["FinInstrmTp"].strip() == "IDO"]
    if not legs:
        return []
    for r in legs:
        r["_exp"] = datetime.strptime(r["XpryDt"].strip()[:10], "%Y-%m-%d").date()
    types = pick_expiries({r["_exp"] for r in legs}, d)
    spot = num(legs[0]["UndrlygPric"])
    table = {}
    for r in legs:
        if r["_exp"] not in types:
            continue
        k = num(r["StrkPric"])
        if spot and abs(k / spot - 1) > BAND:
            continue
        row = table.setdefault((r["_exp"], k), {
            "date": f"{d}", "spot": spot, "expiry": f"{r['_exp']}", "expiry_type": types[r["_exp"]],
            "strike": int(k) if k == int(k) else k})
        side = r["OptnTp"].strip().lower()
        for name, key in SIDE_FIELDS:
            row[f"{side}_{name}"] = r.get(key, "").strip()
    return [table[key] for key in sorted(table)]


def saved_days():
    days = set()
    if os.path.isdir(OUT_DIR):
        for name in os.listdir(OUT_DIR):
            if name.endswith(".csv"):
                with open(os.path.join(OUT_DIR, name), newline="") as f:
                    days |= {row["date"] for row in csv.DictReader(f)}
    return days


def append(rows):
    path = os.path.join(OUT_DIR, rows[0]["date"][:7] + ".csv")
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, restval="")
        if new:
            w.writeheader()
        w.writerows(rows)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    have = saved_days()
    if sys.argv[1:]:
        start = date.fromisoformat(sys.argv[1])
    elif have:
        start = date.fromisoformat(max(have)) + timedelta(days=1)
    else:
        start = DEFAULT_START
    today = datetime.now(IST).date()
    s, added = session(), 0
    d = start
    while d <= today:
        if d.weekday() < 5 and f"{d}" not in have:
            text = download(s, d)
            if text is None:
                print(f"{d}: no file")
            else:
                rows = nifty_rows(text, d)
                if rows:
                    append(rows)
                    added += 1
                print(f"{d}: {len(rows)} rows")
            time.sleep(1)
        d += timedelta(days=1)
    print(f"{added} days added")


if __name__ == "__main__":
    main()
