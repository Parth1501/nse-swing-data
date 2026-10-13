"""
Daily NSE price-action swing list builder (runs on GitHub Actions).

Universe: NSE F&O stocks + Nifty Midcap 150 + every other NSE EQ stock with a
20-day average traded value >= Rs 50 crore.

No indicators (no moving averages, RSI, MACD or ATR). Only price structure and volume.
SUPPORT TRADES ONLY (user's choice, 8 Oct 2026): no breakout setups, and support is read from WEEKLY candles.
Weekly support = a weekly swing low (last 2 years) no weekly close has broken since, or an old weekly swing
high that price has closed above and held (old resistance turned support).
  A  Uptrend structure    - weekly: last 2 weekly swing peaks and last 2 weekly swing troughs each higher
  C  Pullback to support  - in a weekly uptrend, price back within 3% of a weekly support and holding
  D  Retest               - an old weekly peak broken 1-4 weeks ago, revisited, holding as support
  E  Candle at support    - daily hammer / bullish engulfing / inside-day breakout at a weekly support
  F  Room to run          - next resistance at least 6% above entry (REQUIRED)
  G  Relative strength    - beat Nifty over 1 and 3 months
  Volume check            - trigger day volume >= 1.5x its prior 20-day average
Each stock gets a score; the list is ranked. No stop-loss (user's choice).

Writes:
  data/latest.csv  - one row per stock: patterns, score, entry/exit levels, reason, flags
  data/meta.json   - data date, Nifty context, F&O ban list, run stats
  data/sector_map.csv - sectors of stocks outside the Nifty Total Market list, read once from
                        NSE's stock quote page and reused (re-checked every ~6 months)
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

import charts

IST = timezone(timedelta(hours=5, minutes=30))
OUT_DIR = "data"
NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.nseindia.com/",
}
INDEX_SYMBOLS = {"NIFTY", "BANKNIFTY", "FINNIFTY", "MIDCPNIFTY", "NIFTYNXT50", "NIFTYFPI", "SENSEX", "BANKEX"}

# ---- Plan parameters ----
T1_PCT, T2_PCT = 0.03, 0.06          # exits: +3% and +6% from the entry reference
TIME_EXIT_DAYS = 30                  # calendar days
MIN_ROOM_PCT = 6.0                   # F: next resistance must be >= 6% above entry
PIVOT_W = 5                          # daily swing point = highest/lowest of 5 days either side
WEEKLY_PIVOT_W = 2                   # weekly swing point = highest/lowest of 2 weeks either side
WEEKLY_LOOKBACK = 104                # weekly supports come from the last 2 years
WEEKLY_HOLD_TOL_PCT = 1.0            # a weekly close up to 1% under a level doesn't break it
SUPPORT_TOUCH_DAYS = 5               # C/E: the low came to the weekly support within the last week (5 sessions)
NEAR_SUPPORT_PCT = 3.0               # C/E: within 3% of support
RETEST_NEAR_PCT = 2.0                # D: came back within 2% of the broken level
RETEST_MAX_ABOVE_PCT = 5.0           # D: price must still be within 5% of the level (else it has run away)
MAX_PULLBACK_PCT = 15.0              # C/D/E: a drop of more than 15% from the 20-day high is a fall, not a dip
BUY_ZONE_PCT = 3.0                   # support-style buy zone = support .. +3%
VOL_MULT = 1.5
SCORE = {"D": 3, "A": 2, "C": 2, "G": 2, "E": 1, "VOL": 1,
         "SWEEP": 2, "OB": 2, "FVG": 1, "CHOCH": -2}   # Smart Money Concepts: points only, never eligibility
SMC_LOOKBACK = 60                    # SMC zones are searched in the last 60 sessions (about 3 months)
SWEEP_MAX_PCT = 3.0                  # sweep: a dip of at most 3% under the low; deeper is a breakdown
OB_MOVE_PCT = 5.0                    # order block: the move after it must clear its high by 5% within 3 sessions
FVG_MIN_PCT = 1.0                    # fair value gap must be at least 1% of price
MIN_VALUE_CR = 50
MIN_HISTORY = 40                     # shorter histories can't show any structure
SHORT_HISTORY_FLAG = 120

# ---- Track record ----
PICKS_FILE = os.path.join("data", "picks_log.csv")
TOP_N = 10                           # the daily list = top 10 eligible
ENTRY_WINDOW = 3                     # a pick can be bought within the first 3 sessions after the list date
BAD_LIST_DATES = {"2026-09-28"}      # a run just after midnight got stale Yahoo data and logged these by mistake
PICK_STATIC = ["list_date", "rank", "symbol", "segment", "entry_style", "entry_low", "entry_high",
               "t1", "t2", "warning_at_listing", "sector", "sector_tag"]
MIN_SECTOR_STOCKS = 3                # need at least 3 stocks to judge a sector
SECTOR_CACHE = os.path.join("data", "sector_map.csv")
MAX_SECTOR_LOOKUPS = 150             # NSE quote lookups per run (the cache means later runs need only a few)
SECTOR_CACHE_DAYS = 180              # re-check a cached sector after about 6 months
SECTOR_LOOKUP_PAUSE = 0.4            # seconds between NSE requests, to stay polite
ETF_SECTOR = "ETF / Fund"            # shown as the sector, never rated as a sector group

# ---- Track record of past picks
TOP_N = 10                           # the list shows the top 10 eligible stocks each day
ENTRY_WINDOW_SESSIONS = 3            # a pick counts as bought if the entry is reached within 3 sessions
PICKS_LOG = os.path.join(OUT_DIR, "picks_log.csv")        # permanent diary of every day's top 10
PICKS_STATUS = os.path.join(OUT_DIR, "picks_status.csv")  # re-evaluated every run from real prices
CHART_DIR = os.path.join(OUT_DIR, "charts")  # one folder per data date: charts/<YYYY-MM-DD>/<SYMBOL>.png
CHART_N = 12                         # top 12 eligible: the list's 10 plus spares for the teardown's ETF skips
CHART_KEEP_DAYS = 45

FALLBACK_FNO = """ABB ABCAPITAL ADANIENSOL ADANIENT ADANIGREEN ADANIPORTS ALKEM AMBER AMBUJACEM ANGELONE
APLAPOLLO APOLLOHOSP ASHOKLEY ASIANPAINT ASTRAL AUBANK AUROPHARMA AXISBANK BAJAJ-AUTO BAJAJFINSV
BAJFINANCE BANDHANBNK BANKBARODA BANKINDIA BDL BEL BHARATFORG BHARTIARTL BHEL BIOCON BLUESTARCO
BOSCHLTD BPCL BRITANNIA BSE CAMS CANBK CDSL CGPOWER CHOLAFIN CIPLA COALINDIA COFORGE COLPAL CONCOR
CROMPTON CUMMINSIND CYIENT DABUR DALBHARAT DELHIVERY DIVISLAB DIXON DLF DMART DRREDDY EICHERMOT
ETERNAL EXIDEIND FEDERALBNK FORTIS GAIL GLENMARK GMRAIRPORT GODREJCP GODREJPROP GRASIM HAL HAVELLS
HCLTECH HDFCAMC HDFCBANK HDFCLIFE HEROMOTOCO HFCL HINDALCO HINDPETRO HINDUNILVR HINDZINC HUDCO
ICICIBANK ICICIGI ICICIPRULI IDEA IDFCFIRSTB IEX IGL IIFL INDHOTEL INDIANB INDIGO INDUSINDBK
INDUSTOWER INFY INOXWIND IOC IRCTC IREDA IRFC ITC JINDALSTEL JIOFIN JSWENERGY JSWSTEEL JUBLFOOD
KALYANKJIL KAYNES KEI KFINTECH KOTAKBANK KPITTECH LAURUSLABS LICHSGFIN LICI LODHA LT LTF LTIM LUPIN
M&M MANAPPURAM MANKIND MARICO MARUTI MAXHEALTH MAZDOCK MCX MFSL MOTHERSON MPHASIS MUTHOOTFIN
NATIONALUM NAUKRI NBCC NCC NESTLEIND NHPC NMDC NTPC NUVAMA NYKAA OBEROIRLTY OFSS OIL ONGC PAGEIND
PATANJALI PAYTM PERSISTENT PETRONET PFC PGEL PHOENIXLTD PIDILITIND PIIND PNB PNBHOUSING POLICYBZR
POLYCAB POWERGRID PPLPHARMA PRESTIGE RBLBANK RECLTD RELIANCE RVNL SAIL SAMMAANCAP SBICARD SBILIFE
SBIN SHREECEM SHRIRAMFIN SIEMENS SOLARINDS SONACOMS SRF SUNPHARMA SUPREMEIND SUZLON SYNGENE
TATACONSUM TATAELXSI TATAPOWER TATASTEEL TATATECH TCS TECHM TIINDIA TITAGARH TITAN TORNTPHARM
TORNTPOWER TRENT TVSMOTOR ULTRACEMCO UNIONBANK UNITDSPR UNOMINDA UPL VBL VEDL VOLTAS WIPRO YESBANK
ZYDUSLIFE""".split()


# ---------------------------------------------------------------- NSE files
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


def get_fno_universe():
    """Current F&O stock list from NSE's lot-size file; falls back to a built-in list."""
    try:
        txt = nse_get("https://nsearchives.nseindia.com/content/fo/fo_mktlots.csv")
        df = pd.read_csv(io.StringIO(txt))
        df.columns = [c.strip().upper() for c in df.columns]
        syms = [str(x).strip() for x in df["SYMBOL"].dropna()]
        syms = [x for x in syms if x and x.upper() != "SYMBOL" and x.upper() not in INDEX_SYMBOLS]
        syms = sorted(set(syms))
        if len(syms) > 100:
            return syms, "NSE fo_mktlots.csv"
    except Exception as e:
        print("F&O list fetch failed:", e)
    return sorted(set(FALLBACK_FNO)), "built-in fallback list"


def get_ban_list():
    try:
        txt = nse_get("https://nsearchives.nseindia.com/content/fo/fo_secban.csv")
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        header = lines[0] if lines else ""
        syms = []
        for l in lines[1:]:
            parts = [p.strip() for p in l.split(",")]
            if len(parts) >= 2 and parts[1]:
                syms.append(parts[1])
        return {"status": "ok", "header": header, "symbols": syms}
    except Exception as e:
        print("Ban list fetch failed:", e)
        return {"status": "not available", "header": "", "symbols": []}


def get_price_bands():
    try:
        txt = nse_get("https://nsearchives.nseindia.com/content/equities/sec_list.csv")
        df = pd.read_csv(io.StringIO(txt))
        df.columns = [c.strip().upper() for c in df.columns]
        df = df[df["SERIES"].astype(str).str.strip() == "EQ"]
        return {str(r["SYMBOL"]).strip(): str(r["BAND"]).strip() for _, r in df.iterrows()}
    except Exception as e:
        print("Price band fetch failed:", e)
        return {}


def get_index_members(fname):
    """Constituents of a Nifty index (e.g. ind_niftymidcap150list.csv) from NSE / niftyindices."""
    for url in (f"https://nsearchives.nseindia.com/content/indices/{fname}",
                f"https://www.niftyindices.com/IndexConstituent/{fname}",
                f"https://niftyindices.com/IndexConstituent/{fname}"):
        try:
            df = pd.read_csv(io.StringIO(nse_get(url)))
            df.columns = [c.strip().upper() for c in df.columns]
            syms = sorted({str(x).strip() for x in df["SYMBOL"].dropna() if str(x).strip()})
            if len(syms) >= 20:
                return syms, url
        except Exception as e:
            print(f"Index list fetch failed ({url}):", e)
    return [], "not available"


def get_industry_map():
    """NSE industry for each stock, from the Nifty Total Market list (≈750 stocks), else Nifty 500 + Microcap 250."""
    groups = (("ind_niftytotalmarket_list.csv",), ("ind_nifty500list.csv", "ind_niftymicrocap250_list.csv"))
    for files in groups:
        mapping, used = {}, []
        for fname in files:
            for url in (f"https://nsearchives.nseindia.com/content/indices/{fname}",
                        f"https://www.niftyindices.com/IndexConstituent/{fname}",
                        f"https://niftyindices.com/IndexConstituent/{fname}"):
                try:
                    df = pd.read_csv(io.StringIO(nse_get(url)))
                    df.columns = [c.strip().upper() for c in df.columns]
                    if "INDUSTRY" not in df.columns:
                        continue
                    for _, r in df.iterrows():
                        s, ind = str(r["SYMBOL"]).strip(), str(r["INDUSTRY"]).strip()
                        if s and ind and ind.lower() != "nan":
                            mapping.setdefault(s, ind)
                    used.append(url)
                    break
                except Exception as e:
                    print(f"Industry list fetch failed ({url}):", e)
        if len(mapping) >= 400:
            return mapping, "; ".join(used)
    return {}, "not available"


def load_sector_cache():
    try:
        df = pd.read_csv(SECTOR_CACHE, dtype=str, keep_default_na=False)
        return {r["symbol"]: r.to_dict() for _, r in df.iterrows() if r.get("symbol")}
    except Exception:
        return {}


def save_sector_cache(cache):
    cols = ["symbol", "sector", "macro", "industry", "basic_industry", "fetched_on"]
    rows = [{c: cache[s].get(c, "") for c in cols} for s in sorted(cache)]
    pd.DataFrame(rows, columns=cols).to_csv(SECTOR_CACHE, index=False, encoding="utf-8")


def _pick_sector(info, known):
    """NSE's quote page has macro / sector / industry / basic industry. Use the level whose name
    matches the sector names in the index list, so every stock is grouped the same way."""
    vals = [str(info.get(k) or "").strip() for k in ("sector", "macro", "industry")]
    vals = [v for v in vals if v and v.upper() not in ("-", "NA", "N/A", "NONE", "NAN")]
    for v in vals:
        if v in known:
            return v
    return vals[0] if vals else ""


def fill_missing_sectors(symbols, industry):
    """Sector for stocks that are not in the Nifty Total Market list, from NSE's stock quote API.
    Results are kept in data/sector_map.csv, so each stock is looked up once (re-checked after ~6 months).
    Looks up in the given order (best-ranked first); stops early if NSE blocks us."""
    known = set(industry.values())
    cache = load_sector_cache()
    today = datetime.now(IST).date()
    result, todo = {}, []
    for s in symbols:
        if s in industry:
            continue
        c = cache.get(s)
        if c and c.get("sector"):
            result[s] = c["sector"]
            try:
                age = (today - datetime.strptime(c.get("fetched_on", ""), "%Y-%m-%d").date()).days
            except ValueError:
                age = SECTOR_CACHE_DAYS + 1
            if age <= SECTOR_CACHE_DAYS:
                continue
        todo.append(s)
    stats = {"outside_index_list": len([s for s in symbols if s not in industry]),
             "from_cache": len(result), "looked_up": 0, "found": 0, "not_found": [], "errors": 0,
             "stopped_early": False}
    sess, streak, changed = None, 0, False
    for i, s in enumerate(todo[:MAX_SECTOR_LOOKUPS]):
        if sess is None or i % 40 == 0:        # fresh NSE cookies every 40 requests
            sess = requests.Session()
            sess.headers.update(NSE_HEADERS)
            try:
                sess.get("https://www.nseindia.com", timeout=15)
            except Exception:
                pass
        stats["looked_up"] += 1
        try:
            r = sess.get("https://www.nseindia.com/api/quote-equity", params={"symbol": s}, timeout=20)
            r.raise_for_status()
            js = r.json()
            streak = 0
            info = js.get("industryInfo") or {}
            sec = _pick_sector(info, known)
            if not sec and (js.get("info") or {}).get("isETFSec"):
                sec = ETF_SECTOR
            if sec:
                cache[s] = {"symbol": s, "sector": sec, "macro": str(info.get("macro") or ""),
                            "industry": str(info.get("industry") or ""),
                            "basic_industry": str(info.get("basicIndustry") or ""),
                            "fetched_on": today.isoformat()}
                result[s] = sec
                stats["found"] += 1
                changed = True
            else:
                stats["not_found"].append(s)
        except Exception as e:
            stats["errors"] += 1
            streak += 1
            sess = None                         # get new cookies before the next try
            print(f"Sector lookup failed for {s}:", e)
            if streak >= 5:
                stats["stopped_early"] = True
                print("Sector lookups stopped: 5 failures in a row (NSE may be blocking)")
                break
        time.sleep(SECTOR_LOOKUP_PAUSE)
    stats["left_for_next_run"] = max(0, len(todo) - stats["looked_up"])
    if changed:
        save_sector_cache(cache)
    return result, stats


def add_sector_strength(table, nifty):
    """Sector = NSE industry. Sector strength = median 1M and 3M return of our stocks in that sector vs Nifty.
    Leading: beating Nifty on both. Improving: 1M better, 3M not. Weakening: 3M better, 1M not. Lagging: neither."""
    if table.empty:
        return table, []
    n1, n3 = nifty["ret_1m"], nifty["ret_3m"]
    stats = []
    for sec, g in table[~table["sector"].isin(["Unknown", ETF_SECTOR])].groupby("sector"):
        if len(g) < MIN_SECTOR_STOCKS:
            continue
        m1, m3 = g["ret_1m"].median(), g["ret_3m"].median()
        if m1 != m1 or m3 != m3:
            continue
        rs1, rs3 = m1 - n1, m3 - n3
        tag = ("Leading" if rs1 > 0 and rs3 > 0 else "Improving" if rs1 > 0
               else "Weakening" if rs3 > 0 else "Lagging")
        stats.append({"sector": sec, "stocks": int(len(g)), "median_1m": r2(m1), "median_3m": r2(m3),
                      "vs_nifty_1m": r2(rs1), "vs_nifty_3m": r2(rs3), "tag": tag})
    stats.sort(key=lambda s: s["vs_nifty_1m"] + s["vs_nifty_3m"], reverse=True)
    by = {s["sector"]: s for s in stats}
    table["sector_tag"] = table["sector"].map(lambda s: by[s]["tag"] if s in by else "No data")
    table["sector_1m"] = table["sector"].map(lambda s: by[s]["median_1m"] if s in by else None)
    table["sector_3m"] = table["sector"].map(lambda s: by[s]["median_3m"] if s in by else None)
    return table, stats


def get_eq_symbols(bands):
    """All NSE EQ-series symbols (normal rolling settlement). Uses sec_list if loaded, else EQUITY_L.csv."""
    if len(bands) > 500:
        return sorted(bands), "NSE sec_list.csv"
    try:
        txt = nse_get("https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv")
        df = pd.read_csv(io.StringIO(txt))
        df.columns = [c.strip().upper() for c in df.columns]
        df = df[df["SERIES"].astype(str).str.strip() == "EQ"]
        syms = sorted({str(x).strip() for x in df["SYMBOL"].dropna()})
        if len(syms) > 500:
            return syms, "NSE EQUITY_L.csv"
    except Exception as e:
        print("Equity list fetch failed:", e)
    return [], "not available"


def _collect_symbols(obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.lower() == "symbol" and isinstance(v, str):
                out.add(v.strip())
            else:
                _collect_symbols(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _collect_symbols(v, out)


def get_asm_gsm():
    """Best effort: NSE's ASM and GSM lists (JSON endpoints). Returns status per list."""
    result = {}
    for name, url in (("asm", "https://www.nseindia.com/api/reportASM"),
                      ("gsm", "https://www.nseindia.com/api/reportGSM")):
        try:
            syms = set()
            _collect_symbols(json.loads(nse_get(url)), syms)
            result[name] = {"status": "ok" if syms else "empty or unreadable", "symbols": sorted(syms)}
        except Exception as e:
            print(f"{name.upper()} list fetch failed:", e)
            result[name] = {"status": "not available", "symbols": []}
    return result


# ---------------------------------------------------------------- prices
MARKET_DONE_IST = (16, 0)            # before 4:00 PM IST on a weekday, today's prices are live and unfinished


def drop_unfinished_day(df, now=None):
    """A weekday run that starts before 4:00 PM IST must not use today's live, half-day candle
    (the 6:45 AM run on 30 Sep started at 12:09 PM and saved half-day data)."""
    now = now or datetime.now(IST)
    if df.empty or now.weekday() >= 5 or (now.hour, now.minute) >= MARKET_DONE_IST:
        return df
    today = now.strftime("%Y-%m-%d")
    return df[df.index.strftime("%Y-%m-%d") != today]


SCAN_END = os.environ.get("SCAN_END", "").strip()   # one-off re-run of a past day: prices up to (not incl.) this date
PERIOD_DAYS = {"2y": 731, "6mo": 184, "3mo": 92}


def download(tickers, period="2y", min_rows=MIN_HISTORY, chunk_size=40, retries=3):
    frames = {}
    span = {"period": period}
    if SCAN_END:
        end = datetime.strptime(SCAN_END, "%Y-%m-%d")
        span = {"start": (end - timedelta(days=PERIOD_DAYS[period])).strftime("%Y-%m-%d"), "end": SCAN_END}
    for i in range(0, len(tickers), chunk_size):
        chunk = tickers[i:i + chunk_size]
        raw = None
        for attempt in range(retries):
            try:
                raw = yf.download(chunk, **span, interval="1d", group_by="ticker",
                                  auto_adjust=False, threads=True, progress=False)
                break
            except Exception as e:
                print("download error", e)
                raw = None
                time.sleep(5 * (attempt + 1))
        if raw is None or raw.empty:
            continue
        for t in chunk:
            try:
                df = raw[t] if isinstance(raw.columns, pd.MultiIndex) else raw
                df = df[["Open", "High", "Low", "Close", "Volume"]].dropna(subset=["Close"])
                df = drop_unfinished_day(df)
                if len(df) >= min_rows:
                    frames[t] = df
            except Exception:
                pass
        time.sleep(1)
    return frames


def liquid_non_fno(symbols):
    """Quick 3-month download of non-F&O stocks; keep those with 20-day avg traded value >= Rs 50 cr."""
    frames = download([s + ".NS" for s in symbols], period="3mo", min_rows=20, chunk_size=100)
    keep = []
    for t, df in frames.items():
        val_cr = (df["Close"] * df["Volume"]).iloc[-20:].mean() / 1e7
        if val_cr >= MIN_VALUE_CR:
            keep.append(t[:-3])
    return sorted(keep), len(frames)




# ---------------------------------------------------------------- price-action helpers
def r2(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return None if (math.isnan(x) or math.isinf(x)) else round(x, 2)


def pct(a, b):
    """% change from b to a."""
    return (a / b - 1) * 100 if b else np.nan


def swing_points(h, l, w=PIVOT_W):
    """Confirmed swing peaks / troughs as lists of (index, price). A swing needs w days on both sides."""
    peaks, troughs = [], []
    for i in range(w, len(h) - w):
        if h[i] == h[i - w:i + w + 1].max() and h[i] > h[i - w:i].max():
            peaks.append((i, h[i]))
        if l[i] == l[i - w:i + w + 1].min() and l[i] < l[i - w:i].min():
            troughs.append((i, l[i]))
    return peaks, troughs


def vol_ratio_at(v, k):
    """Volume on day k vs the average of the 20 days before it."""
    prior = v[max(0, k - 20):k]
    if len(prior) < 5 or prior.mean() <= 0:
        return np.nan
    return v[k] / prior.mean()


def check_uptrend(peaks, troughs, n, close, window=120, recent_bars=63):
    """A: last 2 peaks and last 2 troughs (within ~6 months) each higher; structure still intact.
    On weekly candles the scan passes window=26, recent_bars=13 (the same ~6 and ~3 months)."""
    rp = [p for p in peaks if p[0] >= n - window]
    rt = [t for t in troughs if t[0] >= n - window]
    if len(rp) < 2 or len(rt) < 2:
        return False, None
    p1, p2 = rp[-2][1], rp[-1][1]
    t1, t2 = rt[-2][1], rt[-1][1]
    recent = max(rp[-1][0], rt[-1][0]) >= n - recent_bars
    return bool(p2 > p1 and t2 > t1 and close > t2 and recent), t2


def weekly_bars(df):
    """Daily candles -> weekly candles (Monday-Friday; the current week may still be in progress).
    Also returns, for every daily row, the index of its week."""
    idx = pd.DatetimeIndex(df.index)
    if idx.tz is not None:
        idx = idx.tz_localize(None)
    monday = (idx - pd.to_timedelta(idx.weekday, unit="D")).normalize()
    w = df[["Open", "High", "Low", "Close", "Volume"]].groupby(monday.values).agg(
        {"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"})
    week_of_day = np.searchsorted(w.index.values, monday.values)
    return w, week_of_day


def weekly_supports(wpeaks, wtroughs, wc, close):
    """Weekly support levels below the latest close, highest first. Each is a dict:
    level, kind ("weekly low" / "old weekly high"), wk (the week of the swing), broke_wk (old highs only).
    - weekly low: a weekly swing low from the last 2 years that no weekly close has broken since
    - old weekly high: a weekly swing high price has since closed above, and no weekly close has lost it"""
    nw, tol = len(wc), 1 - WEEKLY_HOLD_TOL_PCT / 100
    out = []
    for ti, tv in wtroughs:
        if ti >= nw - WEEKLY_LOOKBACK and tv < close and (wc[ti + 1:] >= tv * tol).all():
            out.append({"level": tv, "kind": "weekly low", "wk": ti, "broke_wk": None})
    for pi, pv in wpeaks:
        if pi < nw - WEEKLY_LOOKBACK or pv >= close:
            continue
        above = np.where(wc[pi + 1:] > pv)[0]
        if len(above) == 0:
            continue
        b = pi + 1 + above[0]
        if (wc[b:] >= pv * tol).all():
            out.append({"level": pv, "kind": "old weekly high", "wk": pi, "broke_wk": b})
    out.sort(key=lambda x: -x["level"])
    dedup = []                                              # two levels within 0.5% are one level
    for x in out:
        if not dedup or x["level"] < dedup[-1]["level"] * 0.995:
            dedup.append(x)
    return dedup


def at_support(wsup, l, c):
    """The highest weekly support the daily low came to in the last week (within 3% above it, at most 3% under it)
    while the last 3 daily closes held it."""
    lo = l[-SUPPORT_TOUCH_DAYS:].min()
    for s in wsup:
        S = s["level"]
        if S * 0.97 <= lo <= S * (1 + NEAR_SUPPORT_PCT / 100) and c[-3:].min() >= S * 0.995:
            return s
    return None


def check_pullback(uptrend, touched, h, c):
    """C: in a weekly uptrend, >= 3% off the 20-day high, and back at a weekly support that is holding."""
    if not uptrend or touched is None:
        return None
    off_high = pct(h[-20:].max(), c[-1])
    if off_high < 3:
        return None
    return {"S": touched["level"], "off_high": off_high, "sup": touched}


def check_retest(wpeaks, wl, wc, close):
    """D: an old weekly peak broken (first weekly close above it) 1-4 weeks before this week; a weekly low came
    back within 2% of it since, weekly closes never lost it by more than 2%, and price is no more than 5% above it."""
    nw = len(wc)
    best = None
    for pi, pv in wpeaks:
        above = np.where(wc[pi + 1:] > pv)[0]
        if len(above) == 0:
            continue
        b = pi + 1 + above[0]
        if not (nw - 5 <= b <= nw - 2) or pi < b - WEEKLY_LOOKBACK:
            continue
        if wl[b + 1:].min() > pv * (1 + RETEST_NEAR_PCT / 100):
            continue
        if close < pv or wc[b:].min() < pv * 0.98:
            continue
        if pct(close, pv) > RETEST_MAX_ABOVE_PCT:      # ran away from the level: no longer a retest
            continue
        if best is None or pv > best["P"]:
            best = {"P": pv, "wk": pi, "bwk": b}
    return best


def check_candle(o, h, l, c):
    """E (candle part): hammer, bullish engulfing or inside-day breakout on the latest session."""
    rng = h[-1] - l[-1]
    if rng <= 0:
        return None
    body = abs(c[-1] - o[-1])
    lower = min(o[-1], c[-1]) - l[-1]
    upper = h[-1] - max(o[-1], c[-1])
    if lower >= 2 * max(body, rng * 0.05) and upper <= max(body, rng * 0.1) and (c[-1] - l[-1]) / rng >= 0.67:
        return "Hammer"
    if c[-2] < o[-2] and c[-1] > o[-1] and o[-1] <= c[-2] and c[-1] >= o[-2]:
        return "Bullish engulfing"
    if h[-2] <= h[-3] and l[-2] >= l[-3] and c[-1] > h[-2]:
        return "Inside-day breakout"
    return None


def next_resistance(peaks, h, above):
    """Nearest swing peak (last year) or 52-week high above the entry; NaN = nothing overhead."""
    n = len(h)
    levels = [pv for pi, pv in peaks if pi >= n - 250 and pv > above * 1.001]
    hi52 = h[-252:].max()
    if hi52 > above * 1.001:
        levels.append(hi52)
    return min(levels) if levels else np.nan


# ---------------------------------------------------------------- Smart Money Concepts (points only)
def check_sweep(troughs, supports, l, c, n):
    """SWEEP (liquidity grab): in the last 3 sessions the low dipped under a known low (swing trough or support)
    by at most 3%, and the latest close is back above it. The level had held until then."""
    levels = {tv for ti, tv in troughs if n - 250 <= ti <= n - 6} | {S for S in supports}
    best = None
    for L in levels:
        if (c[max(0, n - 60):n - 3] < L).any():            # it had already broken before: not a fresh sweep
            continue
        dip = l[-3:].min()
        if dip < L * 0.998 and pct(L, dip) <= SWEEP_MAX_PCT and c[-1] > L:
            if best is None or L > best["L"]:
                best = {"L": L, "depth": pct(L, dip)}
    return best


def check_order_block(o, h, l, c, v, n):
    """OB (demand zone): the last red candle before a strong move up (closes 5%+ above its high within 3 sessions,
    with 1.5x volume on one of those days). Price has dipped back to the zone in the last 3 sessions and holds above it."""
    for k in range(n - 5, max(0, n - SMC_LOOKBACK) - 1, -1):       # most recent zone first
        if c[k] >= o[k]:
            continue
        nxt = range(k + 1, min(k + 4, n - 3))
        if not nxt or max(c[j] for j in nxt) < h[k] * (1 + OB_MOVE_PCT / 100):
            continue
        if max((vol_ratio_at(v, j) for j in nxt), default=0) < VOL_MULT:
            continue
        zl, zh = l[k], h[k]
        if (c[k + 1:] < zl).any():                                 # zone already broken
            return None
        if l[-3:].min() <= zh * (1 + NEAR_SUPPORT_PCT / 100) and c[-1] >= zl:
            return {"k": k, "zl": zl, "zh": zh}
        return None                                                # nearest zone not being tested
    return None


def check_fvg(h, l, c, n):
    """FVG: a bullish fair value gap (day 3's low at least 1% above day 1's high) left in the last 60 sessions.
    Price ran at least 3% above it, came back into the gap for the first time in the last 3 sessions and holds above its bottom."""
    for i in range(n - 6, max(1, n - SMC_LOOKBACK) - 1, -1):
        bot, top = h[i - 1], l[i + 1]
        if top <= bot or pct(top, bot) < FVG_MIN_PCT:
            continue
        if l[i + 2:n - 3].min() <= top or h[i + 1:n - 3].max() < top * (1 + NEAR_SUPPORT_PCT / 100):
            continue                                               # already filled before, or never left it
        if l[-3:].min() <= top and l[-3:].min() >= bot * 0.995 and c[-1] >= bot:
            return {"i": i, "bot": bot, "top": top}
    return None


def check_choch(troughs, c):
    """CHOCH (minus points): after higher lows, the latest close is below the last higher low: the uptrend may be ending."""
    if len(troughs) < 2:
        return None
    (_, t1), (_, t2) = troughs[-2], troughs[-1]
    if t2 > t1 and c[-1] < t2:
        return {"L": t2}
    return None


def trailing_return(c, days):
    return pct(c[-1], c[-days - 1]) if len(c) > days else np.nan


# ---------------------------------------------------------------- per-stock analysis
def analyse(sym, df, bands, banned, nifty, segment="F&O", surveillance=None, in_mid150=False):
    surveillance = surveillance or {}
    o, h, l, c, v = (df[k].to_numpy(dtype=float) for k in ("Open", "High", "Low", "Close", "Volume"))
    n = len(c)
    dates = df.index
    fmt = lambda i: dates[i].strftime("%d %b")  # noqa: E731

    peaks, troughs = swing_points(h, l)                     # daily swings: resistance, SMC, chart
    wk, week_of_day = weekly_bars(df)
    wh, wl, wc = (wk[k].to_numpy(dtype=float) for k in ("High", "Low", "Close"))
    nw = len(wc)
    wdates = wk.index
    wfmt = lambda k: "week of " + wdates[k].strftime("%d %b %Y")  # noqa: E731
    wpeaks, wtroughs = swing_points(wh, wl, WEEKLY_PIVOT_W)
    A, last_trough = check_uptrend(wpeaks, wtroughs, nw, c[-1], window=26, recent_bars=13)
    wsup = weekly_supports(wpeaks, wtroughs, wc, c[-1])
    supports = [x["level"] for x in wsup]
    touched = at_support(wsup, l, c)
    C = check_pullback(A, touched, h, c)
    D = check_retest(wpeaks, wl, wc, c[-1])
    candle = check_candle(o, h, l, c)
    near_S = touched["level"] if touched else None
    E = bool(candle and (C or D or near_S is not None))

    # A fall of more than 15% from the 20-day high is not a dip: dip-style setups (C, D, E) don't count
    drop_from_high = pct(h[-20:].max(), c[-1])
    deep_drop = bool(drop_from_high > MAX_PULLBACK_PCT and (C or D or E))
    if deep_drop:
        C, D, E = None, None, False

    SW = check_sweep(troughs, supports, l, c, n)
    OB = check_order_block(o, h, l, c, v, n)
    FV = None if OB else check_fvg(h, l, c, n)       # an order block and its gap are one zone: count it once
    CH = check_choch(troughs, c)
    if deep_drop:
        SW, OB, FV = None, None, None                # a fall, not a dip: no buy-side SMC points either

    ret1, ret3 = trailing_return(c, 21), trailing_return(c, 63)
    G = bool(ret1 == ret1 and ret3 == ret3 and ret1 > nifty["ret_1m"] and ret3 > nifty["ret_3m"])

    vr_today = vol_ratio_at(v, n - 1)
    trig_vr = vr_today
    VOL = bool(trig_vr == trig_vr and trig_vr >= VOL_MULT and (C or D or E))

    # ---- entry style and levels (support trades only; priority: retest > pullback > candle)
    zone_status = ""
    if D or C or E:
        S = D["P"] if D else (C["S"] if C else near_S)
        style = "Retest" if D else ("Pullback" if C else "Candle at support")
        entry_low, entry_high = S, S * (1 + BUY_ZONE_PCT / 100)     # buy near support only
        support = S
        zone_status = ("In buy zone" if c[-1] <= entry_high
                       else f"Above buy zone by {pct(c[-1], entry_high):.1f}%: wait for a dip into the zone")
    else:
        style = ""
        entry_low, entry_high = np.nan, np.nan
        support = supports[0] if supports else np.nan
    entry_ref = entry_high if style else c[-1]
    t1, t2 = entry_ref * (1 + T1_PCT), entry_ref * (1 + T2_PCT)
    res = next_resistance(peaks, h, entry_ref)
    room = pct(res, entry_ref) if res == res else np.nan
    F = bool(res != res or room >= MIN_ROOM_PCT)

    has_setup = bool(C or D or E)
    # a bounce off weekly support that has already run past T1 is a missed trade, not a setup
    ran_away = bool(has_setup and c[-1] > t1)
    eligible = has_setup and F and not ran_away
    # which weekly support the trade is built on (for the reason, the report and the chart)
    if D:
        sup_info = {"level": D["P"], "kind": "old weekly high", "wk": D["wk"], "broke_wk": D["bwk"]}
    elif style:
        sup_info = (C["sup"] if C else touched)
    else:
        sup_info = wsup[0] if wsup else None
    if sup_info:
        support_kind = (f"weekly swing low, {wfmt(sup_info['wk'])}" if sup_info["kind"] == "weekly low" else
                        f"old weekly high, {wfmt(sup_info['wk'])}, broken {wfmt(sup_info['broke_wk'])}")
    else:
        support_kind = ""
    pats = {"A": bool(A), "C": bool(C), "D": bool(D), "E": E, "G": G, "VOL": VOL,
            "SWEEP": bool(SW), "OB": bool(OB), "FVG": bool(FV), "CHOCH": bool(CH)}
    score = sum(SCORE[k] for k, on in pats.items() if on)
    names = {"VOL": "Vol", "SWEEP": "Sweep", "CHOCH": "CHoCH"}
    setups = "+".join(names.get(k, k) for k in ("D", "C", "E", "A", "G", "VOL", "SWEEP", "OB", "FVG", "CHOCH")
                      if pats[k])

    # ---- plain-English reason
    why = []
    if D:
        why.append(f"Retesting ₹{D['P']:.2f}, an old weekly high ({wfmt(D['wk'])}) it broke in the "
                   f"{wfmt(D['bwk'])}, now holding as weekly support")
    if C:
        why.append(f"Pulled back {C['off_high']:.1f}% from its 20-day high to weekly support at ₹{C['S']:.2f} "
                   f"({support_kind}) and holding")
    if E:
        why.append(f"{candle} at weekly support")
    if A:
        why.append("Weekly uptrend: higher weekly highs and higher weekly lows")
    if G:
        why.append(f"Beating Nifty: 1M {ret1:+.1f}% vs {nifty['ret_1m']:+.1f}%, 3M {ret3:+.1f}% vs {nifty['ret_3m']:+.1f}%")
    if VOL:
        why.append(f"Volume {vr_today:.1f}× normal on the latest session")
    if SW:
        why.append(f"Liquidity sweep: dipped {SW['depth']:.1f}% under ₹{SW['L']:.2f} and closed back above it")
    if OB:
        why.append(f"Back at a demand zone (order block) ₹{OB['zl']:.2f}–₹{OB['zh']:.2f} from {fmt(OB['k'])} and holding")
    if FV:
        why.append(f"Filling a fair value gap ₹{FV['bot']:.2f}–₹{FV['top']:.2f} from {fmt(FV['i'])} and holding")
    if CH:
        why.append(f"Change of character: closed below its last higher low ₹{CH['L']:.2f} (minus {-SCORE['CHOCH']} points)")
    if res == res:
        why.append(f"Next resistance ₹{res:.2f} ({room:.1f}% above entry)")
    else:
        why.append("No resistance overhead (at or near its 52-week high)")

    missing = []
    if deep_drop:
        missing.append(f"Fell {drop_from_high:.1f}% from its 20-day high (more than {MAX_PULLBACK_PCT:.0f}%: a fall, not a dip)")
    if not has_setup and not deep_drop:
        missing.append("Not at a weekly support (no retest, pullback or candle at weekly support)")
    if ran_away:
        missing.append(f"Already bounced to ₹{c[-1]:.2f}, above T1 ₹{t1:.2f}: the move off weekly support is done")
    if not F:
        missing.append(f"Room to next resistance only {room:.1f}% (need {MIN_ROOM_PCT:.0f}%)")

    # ---- warning flags (information only, never exclusions)
    band = bands.get(sym, "unknown")
    value20 = (c[-20:] * v[-20:]).mean() / 1e7
    flags, tags = [], []
    if sym in banned:
        flags.append("F&O ban list (no new F&O positions; cash buying allowed)")
        tags.append("F&O ban")
    for name, syms in surveillance.items():
        if sym in syms:
            flags.append(f"On NSE {name} list (surveillance; higher margin / trade restrictions possible)")
            tags.append(name)
    if band in ("2", "5", "2.0", "5.0"):
        flags.append(f"{band}% price band (daily move capped at {band}%)")
        tags.append(f"{band.split('.')[0]}% band")
    if n < SHORT_HISTORY_FLAG:
        flags.append(f"Short history: {n} sessions, limited price structure")
        tags.append("New listing")
    if segment == "Midcap 150" and value20 < MIN_VALUE_CR:
        flags.append(f"Thin liquidity: Rs {value20:.0f} cr/day avg")
        tags.append("Low volume")

    hi52 = h[-252:].max()
    return {
        "symbol": sym, "segment": segment, "in_midcap150": bool(in_mid150),
        "date": dates[-1].strftime("%Y-%m-%d"), "history_sessions": n,
        "eligible": eligible, "score": score, "setups": setups, "entry_style": style,
        "reason": "; ".join(why), "not_eligible_because": "; ".join(missing),
        "warning": ", ".join(tags),
        "flags": "; ".join(flags), "n_flags": len(flags),
        "zone_status": zone_status, "deep_pullback": deep_drop, "drop_from_20d_high_pct": r2(drop_from_high),
        "close": r2(c[-1]), "chg_pct": r2(pct(c[-1], c[-2])),
        "entry_low": r2(entry_low), "entry_high": r2(entry_high),
        "t1": r2(t1) if style else None, "t2": r2(t2) if style else None, "time_exit_days": TIME_EXIT_DAYS,
        "support": r2(support), "support_kind": support_kind, "resistance": r2(res), "room_pct": r2(room),
        "weekly_supports": " ".join(f"{x['level']:.2f}" for x in wsup[:5]),
        "pat_A_uptrend": pats["A"], "pat_C_pullback": pats["C"],
        "pat_D_retest": pats["D"], "pat_E_candle": pats["E"], "pat_F_room": F, "pat_G_rel_strength": pats["G"],
        "vol_ok": pats["VOL"],
        "smc_sweep": pats["SWEEP"], "smc_order_block": pats["OB"], "smc_fvg": pats["FVG"], "smc_choch": pats["CHOCH"],
        "sweep_level": r2(SW["L"]) if SW else None,
        "ob_low": r2(OB["zl"]) if OB else None, "ob_high": r2(OB["zh"]) if OB else None,
        "ob_date": dates[OB["k"]].strftime("%Y-%m-%d") if OB else None,
        "fvg_low": r2(FV["bot"]) if FV else None, "fvg_high": r2(FV["top"]) if FV else None,
        "fvg_date": dates[FV["i"]].strftime("%Y-%m-%d") if FV else None,
        "choch_level": r2(CH["L"]) if CH else None, "vol_ratio_today": r2(vr_today), "trigger_vol_ratio": r2(trig_vr),
        "candle": candle or "", "ret_1m": r2(ret1), "ret_3m": r2(ret3),
        "rs_3m_vs_nifty": r2(ret3 - nifty["ret_3m"]) if ret3 == ret3 else None,
        "high52": r2(hi52), "pct_below_high52": r2(pct(hi52, c[-1])),
        "retest_level": r2(D["P"]) if D else None,
        "retest_break_date": (dates[np.where((week_of_day == D["bwk"]) & (c > D["P"]))[0][0]].strftime("%Y-%m-%d")
                              if D else None),
        "pullback_support": r2(C["S"]) if C else None,
        "last_swing_trough": r2(last_trough), "last_weekly_swing_low": r2(wtroughs[-1][1]) if wtroughs else None, "price_band": band, "avg_value20_cr": r2(value20),
    }


# ---------------------------------------------------------------- track record
def update_picks_log(table, list_date):
    """Save today's top 10 eligible picks to the permanent log (a re-run on the same date replaces them)."""
    top = table[table["eligible"]].head(TOP_N)
    new = pd.DataFrame({
        "list_date": list_date, "list_rank": range(1, len(top) + 1),
        "symbol": top["symbol"].values, "entry_style": top["entry_style"].values,
        "entry_low": top["entry_low"].values, "entry_high": top["entry_high"].values,
        "t1": top["t1"].values, "t2": top["t2"].values,
        "close_at_list": top["close"].values, "warning": top["warning"].values,
    })
    if os.path.exists(PICKS_LOG):
        log = pd.read_csv(PICKS_LOG, dtype={"list_date": str})
        log = pd.concat([log[log["list_date"] != list_date], new], ignore_index=True)
    else:
        log = new
    log.to_csv(PICKS_LOG, index=False, encoding="utf-8")
    return log


def evaluate_pick(p, df):
    """Replay real prices after the list date: entry (within 3 sessions), then T1/T2 within 30 days."""
    out = {"status": "Waiting for entry", "fill_date": None, "fill_price": None, "t1_date": None,
           "t2_date": None, "exit_date": None, "result_pct": None, "max_dip_pct": None,
           "last_close": None, "days_held": None, "event_date": None}
    if df is None:
        out["status"] = "No price data"
        return out
    ds = df.index.strftime("%Y-%m-%d")
    after = df[ds > p["list_date"]]
    ads = after.index.strftime("%Y-%m-%d")
    lo, hi = float(p["entry_low"]), float(p["entry_high"])

    fill_i, fill_price = None, None
    for i in range(min(ENTRY_WINDOW_SESSIONS, len(after))):
        row = after.iloc[i]
        touched = row["Low"] <= hi and row["High"] >= lo
        if p["entry_style"] == "Breakout":
            touched = touched and row["Open"] <= hi          # opened above the range = skipped that day
        if touched:
            fill_i, fill_price = i, min(max(row["Open"], lo), hi)
            break
    if fill_i is None:
        if len(after) >= ENTRY_WINDOW_SESSIONS:
            out.update(status="Not bought", event_date=ads[ENTRY_WINDOW_SESSIONS - 1])
        return out

    fill_date = ads[fill_i]
    deadline = (pd.Timestamp(fill_date) + pd.Timedelta(days=TIME_EXIT_DAYS)).strftime("%Y-%m-%d")
    hold = after.iloc[fill_i + 1:]
    hds = hold.index.strftime("%Y-%m-%d")
    hold = hold[hds <= deadline]
    hds = hold.index.strftime("%Y-%m-%d")
    window_over = ds[-1] >= deadline
    t1_hits = np.where(hold["High"].to_numpy() >= p["t1"])[0]
    t2_hits = np.where(hold["High"].to_numpy() >= p["t2"])[0]
    t1_date = hds[t1_hits[0]] if len(t1_hits) else None
    t2_date = hds[t2_hits[0]] if len(t2_hits) else None

    end = t2_hits[0] + 1 if t2_date else len(hold)
    lows = np.r_[after.iloc[fill_i]["Low"], hold["Low"].to_numpy()[:end]]
    last_close = float(hold["Close"].iloc[-1]) if len(hold) else float(after.iloc[fill_i]["Close"])
    out.update(fill_date=fill_date, fill_price=r2(fill_price), t1_date=t1_date, t2_date=t2_date,
               max_dip_pct=r2(pct(lows.min(), fill_price)), last_close=r2(last_close),
               days_held=(pd.Timestamp(hds[end - 1] if len(hold) else fill_date) - pd.Timestamp(fill_date)).days)
    if t2_date:
        out.update(status="Full win (T2 hit)", exit_date=t2_date, event_date=t2_date,
                   result_pct=r2(pct(p["t2"], fill_price)))
    elif window_over and t1_date:
        out.update(status="Partial win (T1 hit)", exit_date=hds[-1], event_date=hds[-1],
                   result_pct=r2(pct(p["t1"], fill_price)))
    elif window_over:
        out.update(status="Failed (30 days, no target)", exit_date=hds[-1] if len(hds) else fill_date,
                   event_date=hds[-1] if len(hds) else fill_date, result_pct=r2(pct(last_close, fill_price)))
    elif t1_date:
        out.update(status="T1 hit, running for T2", event_date=t1_date,
                   result_pct=r2(pct(last_close, fill_price)))
    else:
        out.update(status="Running", event_date=fill_date, result_pct=r2(pct(last_close, fill_price)))
    return out


def track_record(log, frames, latest_date):
    """Evaluate every logged pick; return the status table and a summary for meta.json."""
    rows = []
    for _, p in log.iterrows():
        res = evaluate_pick(p, frames.get(p["symbol"] + ".NS"))
        rows.append({**p.to_dict(), **res, "new_today": res["event_date"] == latest_date})
    st = pd.DataFrame(rows)
    st.to_csv(PICKS_STATUS, index=False, encoding="utf-8")
    cnt = st["status"].value_counts().to_dict() if not st.empty else {}
    full = cnt.get("Full win (T2 hit)", 0)
    part = cnt.get("Partial win (T1 hit)", 0)
    fail = cnt.get("Failed (30 days, no target)", 0)
    finished = full + part + fail
    bought = st["fill_date"].notna().sum() if not st.empty else 0
    failed_rows = st[st["status"] == "Failed (30 days, no target)"] if not st.empty else st
    return {
        "since": log["list_date"].min() if not log.empty else None,
        "total_picks": int(len(st)), "bought": int(bought),
        "not_bought": int(cnt.get("Not bought", 0)), "waiting_for_entry": int(cnt.get("Waiting for entry", 0)),
        "running": int(cnt.get("Running", 0)), "t1_hit_running_for_t2": int(cnt.get("T1 hit, running for T2", 0)),
        "full_wins": int(full), "partial_wins": int(part), "failed": int(fail), "finished": int(finished),
        "win_rate_pct": r2(100 * (full + part) / finished) if finished else None,
        "full_win_rate_pct": r2(100 * full / finished) if finished else None,
        "partial_win_rate_pct": r2(100 * part / finished) if finished else None,
        "avg_failed_result_pct": r2(failed_rows["result_pct"].astype(float).mean()) if len(failed_rows) else None,
        "avg_max_dip_pct": r2(st["max_dip_pct"].astype(float).mean()) if bought else None,
        "new_results_today": int(st["new_today"].sum()) if not st.empty else 0,
    }


# ---------------------------------------------------------------- track record
def _naive(df):
    if getattr(df.index, "tz", None) is not None:
        df = df.copy()
        df.index = df.index.tz_localize(None)
    return df


def replay_pick(p, df):
    """Replay one pick against the prices after its list date.
    Entry: within ENTRY_WINDOW sessions. Breakout = stop-limit (skip a day that opens above entry_high);
    buy zone = limit order, filled when the day trades inside the zone. Targets checked from the day after
    the fill (plus the fill day's close). T2 = full win; T1 only by day 30 = partial win; neither = failed."""
    df = _naive(df)
    out = {"status": "Waiting for entry", "fill_date": None, "fill_price": None, "t1_date": None,
           "t2_date": None, "close_date": None, "exit_price": None, "return_pct": None,
           "current_pct": None, "max_dip_pct": None, "days_held": None,
           "last_event": "Listed", "last_event_date": p["list_date"]}
    after = df[df.index > pd.Timestamp(p["list_date"])]
    if after.empty:
        return out
    lo, hi = float(p["entry_low"]), float(p["entry_high"])
    fill_i, fill = None, None
    for i in range(min(ENTRY_WINDOW, len(after))):
        r = after.iloc[i]
        if p["entry_style"] == "Breakout":
            if r["Open"] > hi:
                continue
            if r["High"] >= lo:
                fill_i, fill = i, max(r["Open"], lo)
                break
        elif r["Low"] <= hi and r["High"] >= lo:
            fill_i, fill = i, min(max(r["Open"], lo), hi)
            break
    if fill_i is None:
        if len(after) >= ENTRY_WINDOW:
            out.update(status="Not bought", last_event="Not bought (entry never reached)",
                       last_event_date=str(after.index[ENTRY_WINDOW - 1].date()))
        return out

    fd = after.index[fill_i]
    out.update(status="Running", fill_date=str(fd.date()), fill_price=round(float(fill), 2),
               last_event="Bought", last_event_date=str(fd.date()))
    expiry = fd + pd.Timedelta(days=TIME_EXIT_DAYS)
    hold = after.iloc[fill_i:]
    hold = hold[hold.index <= expiry]
    t1, t2 = float(p["t1"]), float(p["t2"])
    t1d = t2d = None
    for j in range(len(hold)):
        r = hold.iloc[j]
        reach = r["Close"] if j == 0 else r["High"]
        if t1d is None and reach >= t1:
            t1d = hold.index[j]
        if reach >= t2:
            t2d = hold.index[j]
            break
    end = t2d if t2d is not None else hold.index[-1]
    path = hold[hold.index <= end]
    lows = path["Low"].iloc[1:] if len(path) > 1 else path["Close"]
    out["max_dip_pct"] = r2(min(0.0, pct(lows.min(), fill))) or 0.0
    if t1d is not None:
        out.update(t1_date=str(t1d.date()), last_event="T1 hit (+3%)", last_event_date=str(t1d.date()))

    expired = df.index[-1] >= expiry
    if t2d is not None:
        out.update(status="Full win (T2)", t2_date=str(t2d.date()), close_date=str(t2d.date()),
                   exit_price=round(t2, 2), return_pct=r2(pct(t2, fill)),
                   last_event="T2 hit (+6%)", last_event_date=str(t2d.date()),
                   days_held=(t2d - fd).days)
    elif expired:
        ev = df.index[df.index >= expiry][0]
        if t1d is not None:
            out.update(status="Partial win (T1)", close_date=str(ev.date()), exit_price=round(t1, 2),
                       return_pct=r2(pct(t1, fill)), last_event="Closed: partial win (30 days, T1 only)")
        else:
            px = float(hold["Close"].iloc[-1])
            out.update(status="Failed", close_date=str(ev.date()), exit_price=round(px, 2),
                       return_pct=r2(pct(px, fill)), last_event="Failed (30 days, no target)")
        out.update(last_event_date=str(ev.date()), days_held=(ev - fd).days)
    else:
        out.update(status="Running (T1 hit)" if t1d is not None else "Running",
                   current_pct=r2(pct(float(df["Close"].iloc[-1]), fill)),
                   days_held=(df.index[-1] - fd).days)
    return out


def _replay_all(log, frames):
    missing = [s + ".NS" for s in log["symbol"].unique() if s + ".NS" not in frames]
    if missing:
        frames.update(download(missing, period="6mo", min_rows=1))
    rows = []
    for _, p in log.iterrows():
        df = frames.get(p["symbol"] + ".NS")
        res = replay_pick(p, df) if df is not None else {"status": "Price data unavailable"}
        rows.append({**p.to_dict(), **res})
    return pd.DataFrame(rows)


def update_track_record(table, frames, data_date):
    """Add today's top 10 to the picks log, replay every pick, and summarise the record.
    A stock that already has an open pick (waiting for entry or running) is not logged again,
    so one trade is never counted twice."""
    if os.path.exists(PICKS_FILE):
        log = pd.read_csv(PICKS_FILE, dtype={"list_date": str})
        log = log[[c for c in PICK_STATIC if c in log.columns]]
        log = log[~log["list_date"].isin(BAD_LIST_DATES)]
    else:
        log = pd.DataFrame(columns=PICK_STATIC)
    if data_date and not table.empty:
        log = log[log["list_date"] != data_date]            # idempotent: rebuild today's entries
        prior = _replay_all(log, frames) if not log.empty else pd.DataFrame(columns=["symbol", "status"])
        active = set(prior.loc[prior["status"].astype(str).str.startswith(("Running", "Waiting")), "symbol"])
        top = table[table["eligible"]].head(TOP_N)
        top = top[~top["symbol"].isin(active)]
        today = pd.DataFrame({
            "list_date": data_date, "rank": top["rank"], "symbol": top["symbol"], "segment": top["segment"],
            "entry_style": top["entry_style"], "entry_low": top["entry_low"], "entry_high": top["entry_high"],
            "t1": top["t1"], "t2": top["t2"], "warning_at_listing": top["warning"].fillna(""),
            "sector": top["sector"], "sector_tag": top["sector_tag"],
        })
        log = pd.concat([log, today], ignore_index=True)

    full = _replay_all(log, frames) if not log.empty else pd.DataFrame()
    if not full.empty:
        full = full.sort_values(["list_date", "rank"], ascending=[False, True])
    full.to_csv(PICKS_FILE, index=False, encoding="utf-8")

    st = full["status"] if not full.empty else pd.Series(dtype=str)
    fw, pw, fl = int((st == "Full win (T2)").sum()), int((st == "Partial win (T1)").sum()), int((st == "Failed").sum())
    closed = fw + pw + fl
    done = full[full["status"].isin(["Full win (T2)", "Partial win (T1)", "Failed"])] if not full.empty else full
    new = full[full["last_event_date"] == data_date] if not full.empty else full
    return {
        "since": str(full["list_date"].min()) if not full.empty else None,
        "picks": int(len(full)),
        "bought": int(full["fill_date"].notna().sum()) if not full.empty else 0,
        "not_bought": int((st == "Not bought").sum()),
        "waiting_for_entry": int((st == "Waiting for entry").sum()),
        "running": int(st.str.startswith("Running").sum()),
        "running_t1_hit": int((st == "Running (T1 hit)").sum()),
        "full_wins_t2": fw, "partial_wins_t1": pw, "failed": fl, "closed": closed,
        "win_rate_t1_or_better_pct": r2(100 * (fw + pw) / closed) if closed else None,
        "full_win_rate_t2_pct": r2(100 * fw / closed) if closed else None,
        "avg_return_closed_pct": r2(done["return_pct"].mean()) if closed else None,
        "avg_max_dip_closed_pct": r2(done["max_dip_pct"].mean()) if closed else None,
        "new_events_today": int(len(new)),
        "file": PICKS_FILE,
    }


def draw_charts(table, frames, data_date):
    """Annotated candlestick PNG for the top eligible stocks; the path goes in the "chart" column.
    A chart that fails is skipped: charts never block the daily list."""
    table["chart"] = ""
    for idx, r in table[table["eligible"]].head(CHART_N).iterrows():
        df = frames.get(r["symbol"] + ".NS")
        if df is None:
            continue
        try:
            h, l = df["High"].to_numpy(dtype=float), df["Low"].to_numpy(dtype=float)
            peaks, troughs = swing_points(h, l)
            path = os.path.join(CHART_DIR, str(data_date), f"{r['symbol']}.png")
            charts.draw(r["symbol"], df, r.to_dict(), peaks, troughs, path)
            table.at[idx, "chart"] = path.replace(os.sep, "/")
        except Exception as e:
            print("chart failed", r["symbol"], e)
    try:
        charts.prune(CHART_DIR, CHART_KEEP_DAYS, data_date)
    except Exception as e:
        print("chart prune failed:", e)
    print(f"Charts drawn: {int((table['chart'] != '').sum())}")
    return table


def nifty_context(df):
    """Nifty's own price action: returns, structure, distance from 52-week high (context only)."""
    h, l, c = (df[k].to_numpy(dtype=float) for k in ("High", "Low", "Close"))
    peaks, troughs = swing_points(h, l)
    up, last_trough = check_uptrend(peaks, troughs, len(c), c[-1])
    last_peak = peaks[-1][1] if peaks else np.nan
    return {
        "date": df.index[-1].strftime("%Y-%m-%d"), "close": r2(c[-1]),
        "ret_1m": trailing_return(c, 21), "ret_3m": trailing_return(c, 63),
        "uptrend_structure": bool(up),
        "last_swing_peak": r2(last_peak), "last_swing_trough": r2(troughs[-1][1] if troughs else np.nan),
        "above_last_trough": bool(troughs and c[-1] > troughs[-1][1]),
        "pct_below_high52": r2(pct(h[-252:].max(), c[-1])),
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    fno, fno_src = get_fno_universe()
    fno_set = set(fno)
    ban = get_ban_list()
    banned = set(ban["symbols"])
    bands = get_price_bands()
    eq_syms, eq_src = get_eq_symbols(bands)
    surv = get_asm_gsm()
    surveillance = {"ASM": set(surv["asm"]["symbols"]), "GSM": set(surv["gsm"]["symbols"])}
    mid150, mid150_src = get_index_members("ind_niftymidcap150list.csv")
    industry, industry_src = get_industry_map()
    mid_set = set(mid150)
    mid_only = [s for s in mid150 if s not in fno_set]

    others = [s for s in eq_syms if s not in fno_set and s not in mid_set]
    liquid, screened = liquid_non_fno(others) if others else ([], 0)
    print(f"F&O: {len(fno)} | Midcap 150 (non-F&O): {len(mid_only)} | others screened: {screened} "
          f"| liquid others: {len(liquid)}")

    segment_of = {s: "F&O" for s in fno}
    segment_of.update({s: "Midcap 150" for s in mid_only})
    segment_of.update({s: "Cash (non-F&O)" for s in liquid})
    universe = fno + mid_only + liquid
    frames = download([s + ".NS" for s in universe] + ["^NSEI"])
    if "^NSEI" not in frames:
        frames.update(download(["^NSEI"]))
    if "^NSEI" not in frames:
        raise SystemExit("Nifty 50 data unavailable; cannot compute relative strength")
    nifty = nifty_context(frames["^NSEI"])

    rows, failed = [], []
    for s in universe:
        df = frames.get(s + ".NS")
        if df is None:
            failed.append(s)
            continue
        try:
            rows.append(analyse(s, df, bands, banned, nifty, segment=segment_of[s],
                                surveillance=surveillance, in_mid150=s in mid_set))
        except Exception as e:
            print("analyse failed", s, e)
            failed.append(s)

    table = pd.DataFrame(rows)
    if not table.empty:
        latest_date = table["date"].mode().iloc[0]
        table["stale"] = table["date"] != latest_date
        prev_date, prev_fresh = None, 0.0
        try:
            with open(os.path.join(OUT_DIR, "meta.json")) as f:
                prev_date = json.load(f).get("data_date")
            old = pd.read_csv(os.path.join(OUT_DIR, "latest.csv"), usecols=["date"])
            prev_fresh = float((old["date"].astype(str) == str(prev_date)).mean())
        except Exception:
            pass
        if SCAN_END and prev_date == latest_date and table["stale"].any():
            # Re-run of a past day: Yahoo leaves out that day for some stocks during market hours.
            # Keep their saved rows (old scoring) instead of throwing the whole re-run away.
            try:
                saved = pd.read_csv(os.path.join(OUT_DIR, "latest.csv"), dtype={"date": str})
                saved = saved[saved["date"] == str(prev_date)].set_index("symbol")
                swap = table["stale"] & table["symbol"].isin(saved.index)
                keep = [k for k in table.columns if k in saved.columns]
                old_rows = saved.loc[table.loc[swap, "symbol"], keep].reset_index()
                for k in table.columns:
                    if k.startswith("smc_"):
                        old_rows[k] = False
                # saved rows were scored by an earlier run, maybe under older rules (e.g. breakouts before
                # 8 Oct 2026), so they can't go on the list or into the picks log
                old_rows["eligible"] = False
                old_rows["not_eligible_because"] = (f"Yahoo had no fresh {latest_date} prices in this re-run, "
                                                    f"so it wasn't re-scored with the current rules")
                table = pd.concat([table[~swap], old_rows], ignore_index=True)
                table["stale"] = table["date"].astype(str) != str(latest_date)
                print(f"Re-run: kept saved rows for {int(swap.sum())} stocks Yahoo left without {latest_date} prices")
            except Exception as e:
                print("re-run merge failed:", e)
        new_fresh = float((~table["stale"]).mean())
        # Yahoo sometimes drops the last session for some or all stocks for a few hours after
        # midnight IST. Never replace good saved data with older or patchier data.
        if prev_date and str(latest_date) < str(prev_date):
            print(f"STALE: Yahoo returned data up to {latest_date}, but the saved files are from "
                  f"{prev_date}. Keeping the saved files; nothing written.")
            return
        if prev_date and str(latest_date) == str(prev_date) and new_fresh < prev_fresh - 0.02:
            print(f"PATCHY: only {new_fresh:.0%} of stocks have {latest_date} prices this run vs "
                  f"{prev_fresh:.0%} in the saved files. Keeping the saved files; nothing written.")
            return
        # A stock whose latest price is missing is judged on old prices, so it can't be on today's list.
        gap = table["stale"] & table["eligible"]
        table.loc[gap, "not_eligible_because"] = (f"price for {latest_date} missing from Yahoo, "
                                                  f"so the setup can't be confirmed")
        table.loc[gap, "eligible"] = False
        print(f"Stocks with {latest_date} prices: {new_fresh:.0%}; eligible but dropped for missing price: {int(gap.sum())}")
        table = table.sort_values(["eligible", "score", "rs_3m_vs_nifty", "trigger_vol_ratio"],
                                  ascending=[False, False, False, False], na_position="last")
        table.insert(0, "rank", range(1, len(table) + 1))
        try:                                   # sectors for stocks outside the index list
            extra, sector_lookup = fill_missing_sectors(list(table["symbol"]), industry)
        except Exception as e:                 # never let this block the daily list
            print("sector lookup failed:", e)
            extra, sector_lookup = {}, {"error": str(e)}
        sector_of = {**extra, **industry}
        table.insert(4, "sector", table["symbol"].map(sector_of).fillna("Unknown"))
        table, sector_stats = add_sector_strength(table, nifty)
        table = draw_charts(table, frames, latest_date)
    else:
        latest_date, sector_stats, sector_lookup = None, [], {}
    table.to_csv(os.path.join(OUT_DIR, "latest.csv"), index=False, encoding="utf-8")

    try:
        track = update_track_record(table, frames, latest_date)
    except Exception as e:                     # tracking must never block the daily list
        print("track record failed:", e)
        track = {"error": str(e)}

    elig = table[table["eligible"]] if not table.empty else table
    meta = {
        "generated_at_ist": datetime.now(IST).strftime("%Y-%m-%d %H:%M"),
        "data_date": latest_date,
        "method": ("price action + volume only; no indicators; no stop-loss; support trades only "
                   "(no breakouts), support read from weekly candles"),
        "universe_source": (f"F&O: {fno_src}; Nifty Midcap 150: {mid150_src}; others: {eq_src} "
                            f"filtered to 20-day avg traded value >= Rs 50 cr"),
        "fno_count": len(fno), "midcap150_count": len(mid150),
        "midcap150_non_fno_count": len(mid_only), "liquid_non_fno_count": len(liquid),
        "universe_count": len(universe), "stocks_analysed": len(rows),
        "stocks_failed_download": failed,
        "note_failed": f"Listed fewer than {MIN_HISTORY} sessions ago or no Yahoo data",
        "eligible_count": int(len(elig)),
        "pattern_counts": {k: int(table[k].sum()) for k in table.columns if k.startswith(("pat_", "smc_")) or k == "vol_ok"}
        if not table.empty else {},
        "score_points": SCORE, "targets_pct": [T1_PCT * 100, T2_PCT * 100], "time_exit_days": TIME_EXIT_DAYS,
        "nifty": {k: (r2(v) if isinstance(v, float) else v) for k, v in nifty.items()},
        "fno_ban": ban,
        "asm_gsm": {k: {"status": v["status"], "count": len(v["symbols"])} for k, v in surv.items()},
        "price_band_source": "NSE sec_list.csv" if bands else "not available",
        "flags_not_rejections": ["F&O ban", "ASM/GSM list", "2%/5% price band", "short price history",
                                 "thin liquidity (Midcap 150)"],
        "price_source": "Yahoo Finance via yfinance (unofficial)",
        "track_record": track,
        "sector_source": (f"{industry_src}; stocks outside it: NSE stock quote page "
                          f"(cached in data/sector_map.csv)"),
        "sector_lookup": sector_lookup,
        "sectors": sector_stats,
        "charts": {"count": int((table["chart"] != "").sum()) if "chart" in table else 0,
                   "base_url": "https://raw.githubusercontent.com/Parth1501/nse-swing-data/main/",
                   "note": "latest.csv column 'chart' = path under base_url; 1-year candles + last 3 months zoomed"},
    }
    with open(os.path.join(OUT_DIR, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
    print(json.dumps({k: meta[k] for k in ("data_date", "stocks_analysed", "eligible_count",
                                           "pattern_counts", "nifty")}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
