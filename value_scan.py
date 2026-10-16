"""
Weekly value screen for the Friday value pick (runs on GitHub Actions, Fridays).

Separate from the daily swing scan: it never reads or writes data/latest.csv.
Long-term idea hunt, not a trade list.

Universe: Nifty Midcap 150 + Nifty Smallcap 250 (no Nifty 100 blue chips),
market cap Rs 2,000 cr to Rs 40,000 cr.

Numbers screen (all must pass; lenders use ROE instead of ROCE and skip debt and cash-flow rules):
  ROCE (or ROE for lenders) > 15%   - latest year
  Sales and profit growth > 15%     - 3-year CAGR (2-year if only 3 years are published)
  Debt / equity < 0.5
  Operating cash flow >= 70% of profit, summed over the last 3 years
  P/E below its own median of the last 4 year-ends, or below its industry's median P/E
Numeric manipulation hints (shown, never decided here; the Claude routine checks the rest):
  price_3x  - price up more than 3x in a year while profit grew less than 100%
  low_insider - promoter/insider holding below 40% (Yahoo's figure; the routine verifies on NSE)

Writes:
  data/value/latest.csv     - every stock in the universe with its numbers and which rules it failed
  data/value/shortlist.csv  - the stocks that passed, best score first (topped up with one-rule misses if < 10 pass)
  data/value/meta.json      - run date, counts, thresholds
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
OUT_DIR = os.path.join("data", "value")
NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.nseindia.com/",
}
INDEX_FILES = ("ind_niftymidcap150list.csv", "ind_niftysmallcap250list.csv")

# ---- Screen thresholds (agreed with Parth, 16 Oct 2026) ----
MCAP_MIN_CR, MCAP_MAX_CR = 2_000, 40_000
MIN_ROCE = 15.0
MIN_GROWTH = 15.0
MAX_DE = 0.5
MIN_CASH_CONVERSION = 0.70
MAX_INSIDER_HINT = 40.0
SHORTLIST_MIN, SHORTLIST_MAX = 10, 15
LENDER_INDUSTRIES = {"Financial Services"}
CR = 1e7


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


def get_index(fname):
    """Constituents (symbol, company, industry) of a Nifty index from NSE / niftyindices."""
    for url in (f"https://nsearchives.nseindia.com/content/indices/{fname}",
                f"https://www.niftyindices.com/IndexConstituent/{fname}",
                f"https://niftyindices.com/IndexConstituent/{fname}"):
        try:
            df = pd.read_csv(io.StringIO(nse_get(url)))
            df.columns = [c.strip().upper() for c in df.columns]
            if len(df) >= 20 and "SYMBOL" in df.columns:
                return df, url
        except Exception as e:
            print(f"Index list fetch failed ({url}):", e)
    return pd.DataFrame(), "not available"


def row(df, *names):
    """First matching row of a yfinance statement as a list, newest year first (NaN-free values only kept as NaN)."""
    if df is None or df.empty:
        return []
    for n in names:
        if n in df.index:
            return [float(x) if pd.notna(x) else math.nan for x in df.loc[n].tolist()]
    return []


def cagr(vals):
    """Growth per year from the oldest to the newest value (newest first). Needs 3+ years and a positive base."""
    v = [x for x in vals if not math.isnan(x)]
    if len(v) < 3 or v[-1] <= 0 or v[0] <= 0:
        return math.nan
    years = len(v) - 1
    return ((v[0] / v[-1]) ** (1 / years) - 1) * 100


def r2(x):
    return None if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))) else round(float(x), 2)


def fetch(sym, tries=3):
    for i in range(tries):
        try:
            t = yf.Ticker(sym + ".NS")
            info = t.info or {}
            fin, bs, cf = t.financials, t.balance_sheet, t.cashflow
            hist = t.history(period="5y", auto_adjust=False)
            return info, fin, bs, cf, hist
        except Exception as e:
            print(f"{sym}: try {i + 1} failed: {e}")
            time.sleep(5 * (i + 1))
    return None


def analyse(sym, company, industry):
    got = fetch(sym)
    out = {"symbol": sym, "company": company, "industry": industry, "data_ok": False}
    if not got:
        return out
    info, fin, bs, cf, hist = got
    mcap = info.get("marketCap")
    revenue = row(fin, "Total Revenue", "Operating Revenue")
    profit = row(fin, "Net Income Common Stockholders", "Net Income", "Net Income From Continuing Operation Net Minority Interest")
    ebit = row(fin, "EBIT", "Operating Income")
    assets = row(bs, "Total Assets")
    cur_liab = row(bs, "Current Liabilities")
    equity = row(bs, "Stockholders Equity", "Common Stock Equity")
    debt = row(bs, "Total Debt")
    cfo = row(cf, "Operating Cash Flow", "Cash Flow From Continuing Operating Activities")
    lender = industry in LENDER_INDUSTRIES

    out["data_ok"] = bool(mcap and revenue and profit)
    out["mcap_cr"] = r2(mcap / CR) if mcap else None
    out["years_of_data"] = len([x for x in profit if not math.isnan(x)])
    out["lender_rules"] = lender

    roce = math.nan
    if ebit and assets and cur_liab and not math.isnan(ebit[0]) and assets[0] - cur_liab[0] > 0:
        roce = ebit[0] / (assets[0] - cur_liab[0]) * 100
    roe = math.nan
    if profit and equity and not math.isnan(profit[0]) and equity[0] > 0:
        roe = profit[0] / equity[0] * 100
    out["roce_pct"], out["roe_pct"] = r2(roce), r2(roe)
    out["sales_cagr_pct"], out["profit_cagr_pct"] = r2(cagr(revenue[:4])), r2(cagr(profit[:4]))
    de = math.nan
    if equity and equity[0] > 0:
        de = (debt[0] if debt and not math.isnan(debt[0]) else 0.0) / equity[0]
    out["debt_equity"] = r2(de)
    p3 = [x for x in profit[:3] if not math.isnan(x)]
    c3 = [x for x in cfo[:3] if not math.isnan(x)]
    conv = math.nan
    if len(p3) == 3 and len(c3) == 3 and sum(p3) > 0:
        conv = sum(c3) / sum(p3)
    out["cfo_to_profit_3y"] = r2(conv)

    pe = math.nan
    if mcap and profit and not math.isnan(profit[0]) and profit[0] > 0:
        pe = mcap / profit[0]
    out["pe"] = r2(pe)

    # Own P/E at each of the last 4 year-ends, using today's share count (close enough for a median).
    own_pes = []
    shares = info.get("sharesOutstanding")
    if shares and hist is not None and not hist.empty and fin is not None and not fin.empty:
        closes = hist["Close"].copy()
        closes.index = closes.index.tz_localize(None)
        for i, d in enumerate(list(fin.columns)[:4]):
            if i >= len(profit) or math.isnan(profit[i]) or profit[i] <= 0:
                continue
            before = closes[closes.index <= pd.Timestamp(d)]
            if len(before):
                own_pes.append(before.iloc[-1] * shares / profit[i])
    out["own_median_pe"] = r2(float(np.median(own_pes))) if len(own_pes) >= 2 else None

    insider = info.get("heldPercentInsiders")
    out["insider_pct"] = r2(insider * 100) if insider is not None else None

    ret_1y = math.nan
    if hist is not None and len(hist) > 260:
        c = hist["Close"].dropna()
        ret_1y = (c.iloc[-1] / c.iloc[-252] - 1) * 100 if len(c) > 252 else math.nan
        out["close"] = r2(c.iloc[-1])
        out["high_52w"] = r2(c.iloc[-252:].max())
        out["pct_below_high52"] = r2((1 - c.iloc[-1] / c.iloc[-252:].max()) * 100)
    out["ret_1y_pct"] = r2(ret_1y)
    latest_profit_growth = math.nan
    if len(profit) >= 2 and profit[1] > 0 and not math.isnan(profit[0]):
        latest_profit_growth = (profit[0] / profit[1] - 1) * 100
    out["price_3x"] = bool(not math.isnan(ret_1y) and ret_1y > 200 and
                           (math.isnan(latest_profit_growth) or latest_profit_growth < 100))
    out["low_insider"] = bool(out["insider_pct"] is not None and out["insider_pct"] < MAX_INSIDER_HINT)
    return out


def apply_rules(df):
    ind_pe = (df[df["pe"].notna() & (df["pe"] > 0)].groupby("industry")["pe"]
              .agg(["median", "count"]))
    all_median = df.loc[df["pe"] > 0, "pe"].median()
    df["industry_median_pe"] = df["industry"].map(
        lambda i: r2(ind_pe.loc[i, "median"]) if i in ind_pe.index and ind_pe.loc[i, "count"] >= 3 else r2(all_median))

    fails = []
    for _, r in df.iterrows():
        f = []
        if not r["data_ok"]:
            f.append("no data")
        mc = r.get("mcap_cr")
        if mc is None or not (MCAP_MIN_CR <= mc <= MCAP_MAX_CR):
            f.append("size")
        ret = r["roe_pct"] if r["lender_rules"] else r["roce_pct"]
        if pd.isna(ret) or ret <= MIN_ROCE:
            f.append("ROE" if r["lender_rules"] else "ROCE")
        if pd.isna(r["sales_cagr_pct"]) or r["sales_cagr_pct"] <= MIN_GROWTH:
            f.append("sales growth")
        if pd.isna(r["profit_cagr_pct"]) or r["profit_cagr_pct"] <= MIN_GROWTH:
            f.append("profit growth")
        if not r["lender_rules"]:
            if pd.isna(r["debt_equity"]) or r["debt_equity"] >= MAX_DE:
                f.append("debt")
            if pd.isna(r["cfo_to_profit_3y"]) or r["cfo_to_profit_3y"] < MIN_CASH_CONVERSION:
                f.append("cash flow")
        pe, own, ind = r["pe"], r["own_median_pe"], r["industry_median_pe"]
        cheap = (pd.notna(pe) and pe > 0 and
                 ((pd.notna(own) and pe < own) or (pd.notna(ind) and pe < ind)))
        if not cheap:
            f.append("valuation")
        fails.append(f)
    df["failed_rules"] = [", ".join(f) for f in fails]
    df["n_failed"] = [len(f) for f in fails]
    df["passed"] = df["n_failed"] == 0

    # Score: average percentile of quality, growth, cash and cheapness (higher is better).
    q = df.apply(lambda r: r["roe_pct"] if r["lender_rules"] else r["roce_pct"], axis=1)
    cheapness = df["industry_median_pe"] / df["pe"].where(df["pe"] > 0)
    parts = [q.rank(pct=True), df["sales_cagr_pct"].rank(pct=True), df["profit_cagr_pct"].rank(pct=True),
             df["cfo_to_profit_3y"].clip(upper=1.5).rank(pct=True), cheapness.rank(pct=True)]
    df["score"] = (pd.concat(parts, axis=1).mean(axis=1) * 100).round(1)
    return df


def main():
    now = datetime.now(IST)
    os.makedirs(OUT_DIR, exist_ok=True)
    frames, sources = [], []
    for fname in INDEX_FILES:
        d, src = get_index(fname)
        sources.append(src)
        if not d.empty:
            frames.append(d)
    if not frames:
        raise SystemExit("Could not load the Midcap 150 / Smallcap 250 lists")
    uni = pd.concat(frames).drop_duplicates("SYMBOL")
    uni.columns = [c.replace(" ", "_") for c in uni.columns]    # NSE's header is "COMPANY NAME"
    rows = []
    for i, r in enumerate(uni.itertuples(index=False)):
        sym = str(r.SYMBOL).strip()
        company = str(getattr(r, "COMPANY_NAME", sym)).strip()
        industry = str(getattr(r, "INDUSTRY", "")).strip()
        rows.append(analyse(sym, company, industry))
        if i % 25 == 0:
            print(f"{i + 1}/{len(uni)} {sym}")
        time.sleep(0.4)
    df = apply_rules(pd.DataFrame(rows))
    df = df.sort_values(["passed", "score"], ascending=[False, False])
    df.to_csv(os.path.join(OUT_DIR, "latest.csv"), index=False)

    passed = df[df["passed"]]
    short = passed.head(SHORTLIST_MAX).assign(near_miss=False)
    if len(short) < SHORTLIST_MIN:
        # Top up with stocks that missed exactly one rule, never on size or missing data.
        miss = df[(df["n_failed"] == 1) & ~df["failed_rules"].isin(["size", "no data"])]
        short = pd.concat([short, miss.head(SHORTLIST_MIN - len(short)).assign(near_miss=True)])
    short.to_csv(os.path.join(OUT_DIR, "shortlist.csv"), index=False)

    meta = {
        "generated_at_ist": now.strftime("%Y-%m-%d %H:%M"),
        "data_date": now.strftime("%Y-%m-%d"),
        "universe_source": sources,
        "universe_count": int(len(uni)),
        "with_data": int(df["data_ok"].sum()),
        "in_size_band": int((~df["failed_rules"].str.contains("size")).sum()),
        "passed_count": int(len(passed)),
        "shortlist_count": int(len(short)),
        "near_miss_count": int(short["near_miss"].sum()),
        "thresholds": {"mcap_cr": [MCAP_MIN_CR, MCAP_MAX_CR], "min_roce_or_roe_pct": MIN_ROCE,
                       "min_3y_sales_and_profit_cagr_pct": MIN_GROWTH, "max_debt_equity": MAX_DE,
                       "min_cfo_to_profit_3y": MIN_CASH_CONVERSION,
                       "valuation": "P/E below own 4-year-end median or industry median",
                       "lenders": sorted(LENDER_INDUSTRIES)},
        "source": "Yahoo Finance via yfinance (annual statements); the Claude routine re-checks key numbers on Screener/NSE",
    }
    with open(os.path.join(OUT_DIR, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
