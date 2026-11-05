"""
Muhurat pick research (one-off, Diwali 2026). Separate from the daily swing scan: it never
touches data/.

Question: which kind of stock, bought at the Diwali Muhurat session and held one Samvat year
(Diwali to next Diwali), has beaten Nifty, and which stock fits that best today?

1. Universe: Nifty 500 (NSE list) + Nifty 50 index (^NSEI) as the benchmark.
2. Prices: Yahoo daily, adjusted, from 2012.
3. Backtest: at each Diwali 2014-2024, rank stocks with only the prices known that day using
   several rules, buy the top 1 / 5 / 10, hold to the next Diwali, compare with Nifty.
   Caveat: today's Nifty 500 list is used for every year (survivorship bias), so absolute
   returns are flattering; the comparison BETWEEN rules is what matters.
4. Per stock: its own Samvat-year record (return each Diwali-to-Diwali year, beat-Nifty rate).
5. Today: every rule's current top 15, with trend, risk and level numbers, plus Yahoo
   fundamentals for the names that show up.

Writes muhurat/out/{backtest_years.csv, backtest_summary.csv, today.csv, stock_samvat.csv, summary.json}
"""
import io
import json
import math
import os
import time
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import requests
import yfinance as yf

IST = timezone(timedelta(hours=5, minutes=30))
OUT = os.path.join("muhurat", "out")
NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.nseindia.com/",
}
# Lakshmi Puja / Muhurat session dates. Entry = last close on or before the date.
DIWALI = ["2014-10-23", "2015-11-11", "2016-10-30", "2017-10-19", "2018-11-07", "2019-10-27",
          "2020-11-14", "2021-11-04", "2022-10-24", "2023-11-12", "2024-11-01", "2025-10-21"]
TODAY_MUHURAT = "2026-11-08"


def nse_get(url):
    s = requests.Session()
    s.headers.update(NSE_HEADERS)
    try:
        s.get("https://www.nseindia.com", timeout=15)
    except Exception:
        pass
    r = s.get(url, timeout=30)
    r.raise_for_status()
    return r.text


def universe():
    for url in ("https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv",
                "https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv"):
        try:
            df = pd.read_csv(io.StringIO(nse_get(url)))
            df.columns = [c.strip().upper().replace(" ", "_") for c in df.columns]
            if len(df) > 300:
                return df[["SYMBOL", "COMPANY_NAME", "INDUSTRY"]], url
        except Exception as e:
            print("universe fetch failed", url, e)
    raise SystemExit("no Nifty 500 list")


def download(symbols):
    closes, vols, highs, lows = {}, {}, {}, {}
    for i in range(0, len(symbols), 50):
        chunk = symbols[i:i + 50]
        tick = [s + ".NS" for s in chunk]
        for attempt in range(3):
            try:
                d = yf.download(tick, start="2012-06-01", auto_adjust=True, progress=False,
                                group_by="ticker", threads=True)
                break
            except Exception as e:
                print("download failed", e)
                time.sleep(10)
        else:
            continue
        for s, t in zip(chunk, tick):
            try:
                x = d[t].dropna(subset=["Close"])
            except Exception:
                continue
            if len(x) < 260:
                continue
            closes[s], vols[s], highs[s], lows[s] = x["Close"], x["Volume"], x["High"], x["Low"]
        print(f"downloaded {min(i + 50, len(symbols))}/{len(symbols)}")
        time.sleep(2)
    C = pd.DataFrame(closes).sort_index()
    V = pd.DataFrame(vols).reindex(C.index)
    H = pd.DataFrame(highs).reindex(C.index)
    L = pd.DataFrame(lows).reindex(C.index)
    return C, V, H, L


def pos_on_or_before(idx, date):
    p = idx.searchsorted(pd.Timestamp(date), side="right") - 1
    return int(p)


def features(C, V, nifty, p):
    """Point-in-time features at row p (uses rows <= p only)."""
    c = C.iloc[: p + 1]
    last = c.iloc[-1]
    ok = c.iloc[-260:].notna().sum() >= 250
    dma200 = c.iloc[-200:].mean()
    dma200_prev = c.iloc[-220:-20].mean()
    dma50 = c.iloc[-50:].mean()
    hi = c.iloc[-252:].max()
    r = c.pct_change(fill_method=None).iloc[-252:]
    vol = r.std() * math.sqrt(252) * 100
    m12_1 = (c.iloc[-22] / c.iloc[-253] - 1) * 100
    m6 = (last / c.iloc[-127] - 1) * 100
    m3 = (last / c.iloc[-64] - 1) * 100
    n = nifty.iloc[: p + 1]
    n6 = (n.iloc[-1] / n.iloc[-127] - 1) * 100
    n3 = (n.iloc[-1] / n.iloc[-64] - 1) * 100
    tv = (C.iloc[p - 59: p + 1] * V.iloc[p - 59: p + 1]).median() / 1e7
    f = pd.DataFrame({
        "close": last, "dma50": dma50, "dma200": dma200,
        "dma200_slope_pct": (dma200 / dma200_prev - 1) * 100,
        "off_high_pct": (last / hi - 1) * 100,
        "vol_pct": vol, "m12_1": m12_1, "m6": m6, "m3": m3,
        "rs6": m6 - n6, "rs3": m3 - n3, "tv_cr": tv,
    })
    f = f[ok & f["close"].notna() & f["m12_1"].notna()]
    f["liq_pctile"] = f["tv_cr"].rank(pct=True)
    f["trend"] = (f["close"] > f["dma200"]) & (f["dma200_slope_pct"] > 0) & (f["dma50"] > f["dma200"])
    return f


def rules(f):
    """Each rule returns symbols best first."""
    liq = f[f["liq_pctile"] >= 0.3]
    out = {}
    t = liq[liq["trend"]]
    out["R1 momentum leader (trend, <=10% off high, 12-1 mom / vol)"] = \
        t[t["off_high_pct"] >= -10].assign(k=lambda d: d.m12_1 / d.vol_pct).sort_values("k", ascending=False).index.tolist()
    out["R2 leader on a dip (trend, 5-20% off high, RS6>0, 12-1 mom / vol)"] = \
        t[(t["off_high_pct"] <= -5) & (t["off_high_pct"] >= -20) & (t["rs6"] > 0)].assign(
            k=lambda d: d.m12_1 / d.vol_pct).sort_values("k", ascending=False).index.tolist()
    out["R3 pure 12-1 momentum"] = liq.sort_values("m12_1", ascending=False).index.tolist()
    out["R4 low-volatility uptrend"] = t.sort_values("vol_pct").index.tolist()
    out["R5 last year's laggard (mean reversion)"] = liq.sort_values("m12_1").index.tolist()
    out["R6 steady compounder (trend, vol in lowest half, 12-1 mom)"] = \
        t[t["vol_pct"] <= liq["vol_pct"].median()].sort_values("m12_1", ascending=False).index.tolist()
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    uni, src = universe()
    syms = [str(s).strip() for s in uni["SYMBOL"]]
    nifty = yf.download("^NSEI", start="2012-06-01", auto_adjust=True, progress=False)["Close"]
    if isinstance(nifty, pd.DataFrame):
        nifty = nifty.iloc[:, 0]
    C, V, H, L = download(syms)
    nifty = nifty.reindex(C.index).ffill()
    print("prices:", C.shape, "last date", C.index[-1].date())

    # ---------- backtest ----------
    years = []
    for d0, d1 in zip(DIWALI[:-1], DIWALI[1:]):
        p0, p1 = pos_on_or_before(C.index, d0), pos_on_or_before(C.index, d1)
        if p0 < 260:
            continue
        f = features(C, V, nifty, p0)
        fwd = (C.iloc[p1] / C.iloc[p0] - 1) * 100
        n_ret = (nifty.iloc[p1] / nifty.iloc[p0] - 1) * 100
        uni_avg = fwd[f.index].mean()
        for name, order in rules(f).items():
            for k in (1, 5, 10):
                pick = order[:k]
                if len(pick) < k:
                    continue
                r = fwd[pick].mean()
                years.append({"samvat_start": d0, "rule": name, "top": k, "ret_pct": round(r, 2),
                              "nifty_pct": round(n_ret, 2), "universe_avg_pct": round(uni_avg, 2),
                              "excess_vs_nifty": round(r - n_ret, 2), "picks": " ".join(pick)})
    by = pd.DataFrame(years)
    by.to_csv(os.path.join(OUT, "backtest_years.csv"), index=False)
    summ = by.groupby(["rule", "top"]).agg(
        years=("ret_pct", "size"), avg_ret=("ret_pct", "mean"), median_ret=("ret_pct", "median"),
        avg_excess=("excess_vs_nifty", "mean"),
        beat_nifty_years=("excess_vs_nifty", lambda x: int((x > 0).sum())),
        worst_year=("ret_pct", "min"), best_year=("ret_pct", "max"),
        avg_universe=("universe_avg_pct", "mean")).round(2).reset_index()
    summ.to_csv(os.path.join(OUT, "backtest_summary.csv"), index=False)
    print(summ.to_string())

    # ---------- each stock's own Samvat record ----------
    rec = {}
    for d0, d1 in zip(DIWALI[:-1], DIWALI[1:]):
        p0, p1 = pos_on_or_before(C.index, d0), pos_on_or_before(C.index, d1)
        fwd = (C.iloc[p1] / C.iloc[p0] - 1) * 100
        n_ret = (nifty.iloc[p1] / nifty.iloc[p0] - 1) * 100
        rec[d0[:4]] = fwd.round(1)
        rec["ex" + d0[:4]] = (fwd - n_ret).round(1)
        # first month after Diwali
        p20 = min(p0 + 20, len(C) - 1)
        rec["m1_" + d0[:4]] = ((C.iloc[p20] / C.iloc[p0] - 1) * 100 - (nifty.iloc[p20] / nifty.iloc[p0] - 1) * 100).round(1)
    sv = pd.DataFrame(rec)
    yrs = [c for c in sv.columns if c.isdigit()]
    exs = ["ex" + y for y in yrs]
    m1s = ["m1_" + y for y in yrs]
    sv["samvat_years"] = sv[yrs].notna().sum(axis=1)
    sv["samvat_up_years"] = (sv[yrs] > 0).sum(axis=1)
    sv["samvat_beat_nifty_years"] = (sv[exs] > 0).sum(axis=1)
    sv["samvat_median_ret"] = sv[yrs].median(axis=1).round(1)
    sv["post_diwali_month_beat_nifty"] = (sv[m1s] > 0).sum(axis=1)
    p_last_diwali = pos_on_or_before(C.index, DIWALI[-1])
    sv["samvat2082_so_far"] = ((C.iloc[-1] / C.iloc[p_last_diwali] - 1) * 100).round(1)
    sv.index.name = "symbol"
    sv.to_csv(os.path.join(OUT, "stock_samvat.csv"))

    # ---------- today ----------
    p = len(C) - 1
    f = features(C, V, nifty, p)
    rl = rules(f)
    names = set()
    for order in rl.values():
        names.update(order[:15])
    t = f.loc[sorted(names)].copy()
    for name, order in rl.items():
        t[name.split()[0] + "_rank"] = [order.index(s) + 1 if s in order else None for s in t.index]
    wk = C.resample("W-FRI").last()
    wl = L.resample("W-FRI").min()
    t["low_13w"] = wl.iloc[-13:].min()[t.index]
    t["low_26w"] = wl.iloc[-26:].min()[t.index]
    t["high_52w"] = H.iloc[-252:].max()[t.index]
    tr = pd.concat([H - L, (H - C.shift()).abs(), (L - C.shift()).abs()]).groupby(level=0).max()
    t["atr14"] = tr.iloc[-14:].mean()[t.index]
    t["weekly_close_last4"] = [" ".join(f"{x:.1f}" for x in wk[s].iloc[-4:]) for s in t.index]
    meta = uni.set_index("SYMBOL")
    t["company"] = meta.reindex(t.index)["COMPANY_NAME"]
    t["industry"] = meta.reindex(t.index)["INDUSTRY"]
    t = t.join(sv[["samvat_years", "samvat_up_years", "samvat_beat_nifty_years", "samvat_median_ret",
                   "post_diwali_month_beat_nifty", "samvat2082_so_far"]])
    fund = []
    for s in t.index:
        try:
            i = yf.Ticker(s + ".NS").info or {}
        except Exception:
            i = {}
        fund.append({k: i.get(k) for k in ("marketCap", "trailingPE", "forwardPE", "priceToBook",
                                           "returnOnEquity", "debtToEquity", "revenueGrowth",
                                           "earningsGrowth", "profitMargins", "heldPercentInsiders")})
        time.sleep(0.3)
    fd = pd.DataFrame(fund, index=t.index)
    fd["marketCap"] = (fd["marketCap"] / 1e7).round(0)
    t = t.join(fd.rename(columns={"marketCap": "mcap_cr"}))
    t.round(2).to_csv(os.path.join(OUT, "today.csv"))

    json.dump({"generated_at_ist": datetime.now(IST).strftime("%Y-%m-%d %H:%M"),
               "price_last_date": str(C.index[-1].date()), "universe_source": src,
               "stocks_with_prices": int(C.shape[1]), "diwali_dates": DIWALI,
               "muhurat_2026": TODAY_MUHURAT,
               "nifty_close": round(float(nifty.iloc[-1]), 2),
               "caveat": "survivorship bias: today's Nifty 500 list used for all past years"},
              open(os.path.join(OUT, "summary.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
