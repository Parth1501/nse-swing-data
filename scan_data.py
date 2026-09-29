"""
Daily NSE price-action swing list builder (runs on GitHub Actions).

Universe: NSE F&O stocks + Nifty Midcap 150 + every other NSE EQ stock with a
20-day average traded value >= Rs 50 crore.

No indicators (no moving averages, RSI, MACD or ATR). Only price structure and volume:
  A  Uptrend structure    - last 2 swing peaks and last 2 swing troughs each higher
  B  Base breakout        - 2-6 week sideways base (range <= 12%) broken on a close
  C  Pullback to support  - in an uptrend, price back within 3% of support and holding
  D  Retest               - an old peak broken in the last month, revisited, holding as support
  E  Candle at support    - hammer / bullish engulfing / inside-day breakout near support
  F  Room to run          - next resistance at least 6% above entry (REQUIRED)
  G  Relative strength    - beat Nifty over 1 and 3 months
  Volume check            - trigger day volume >= 1.5x its prior 20-day average
Each stock gets a score; the list is ranked. No stop-loss (user's choice).

Writes:
  data/latest.csv  - one row per stock: patterns, score, entry/exit levels, reason, flags
  data/meta.json   - data date, Nifty context, F&O ban list, run stats
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
PIVOT_W = 5                          # swing point = highest/lowest of 5 days either side
BASE_LENGTHS = (30, 20, 15, 10)      # B: 6, 4, 3, 2 week bases (longest preferred)
BASE_MAX_RANGE_PCT = 12.0
BREAKOUT_MAX_EXT_PCT = 5.0           # B: skip if price already > 5% above the base top
NEAR_SUPPORT_PCT = 3.0               # C/E: within 3% of support
RETEST_NEAR_PCT = 2.0                # D: came back within 2% of the broken level
VOL_MULT = 1.5
ENTRY_BUFFER = 0.01                  # breakout entry: trigger high .. +1%
SCORE = {"B": 3, "D": 3, "A": 2, "C": 2, "G": 2, "E": 1, "VOL": 1}
MIN_VALUE_CR = 50
MIN_HISTORY = 40                     # shorter histories can't show any structure
SHORT_HISTORY_FLAG = 120

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
def download(tickers, period="2y", min_rows=MIN_HISTORY, chunk_size=40, retries=3):
    frames = {}
    for i in range(0, len(tickers), chunk_size):
        chunk = tickers[i:i + chunk_size]
        raw = None
        for attempt in range(retries):
            try:
                raw = yf.download(chunk, period=period, interval="1d", group_by="ticker",
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


def check_uptrend(peaks, troughs, n, close):
    """A: last 2 peaks and last 2 troughs (within ~6 months) each higher; structure still intact."""
    rp = [p for p in peaks if p[0] >= n - 120]
    rt = [t for t in troughs if t[0] >= n - 120]
    if len(rp) < 2 or len(rt) < 2:
        return False, None
    p1, p2 = rp[-2][1], rp[-1][1]
    t1, t2 = rt[-2][1], rt[-1][1]
    recent = max(rp[-1][0], rt[-1][0]) >= n - 63
    return bool(p2 > p1 and t2 > t1 and close > t2 and recent), t2


def check_base_breakout(h, l, c, v, n):
    """B: close above a 2-6 week base whose range is <= 12%, in the last 3 sessions, still holding."""
    for bo in (n - 1, n - 2, n - 3):
        for L in BASE_LENGTHS:
            s = bo - L
            if s < 0:
                continue
            bh, bl = h[s:bo].max(), l[s:bo].min()
            rng = pct(bh, bl)
            if rng > BASE_MAX_RANGE_PCT or c[bo] <= bh:
                continue
            if (c[bo:] < bh).any():
                continue
            if pct(c[-1], bh) > BREAKOUT_MAX_EXT_PCT:
                continue
            return {"bo": bo, "L": L, "bh": bh, "bl": bl, "rng": rng, "vr": vol_ratio_at(v, bo)}
    return None


def support_levels(peaks, last_trough, c, n):
    """Support = last swing trough + old peaks (last year) that price has since closed above."""
    levels = []
    if last_trough is not None and last_trough < c[-1]:
        levels.append(last_trough)
    for pi, pv in peaks:
        if pi >= n - 250 and pv < c[-1] and (c[pi + 1:] > pv).any():
            levels.append(pv)
    return sorted(set(levels), reverse=True)


def check_pullback(uptrend, supports, h, l, c):
    """C: in an uptrend, >= 3% off the 20-day high, low came within 3% of support, closes holding."""
    if not uptrend:
        return None
    recent_high = h[-20:].max()
    off_high = pct(recent_high, c[-1])
    if off_high < 3:
        return None
    for S in supports:
        if l[-3:].min() <= S * (1 + NEAR_SUPPORT_PCT / 100) and c[-3:].min() >= S * 0.995:
            return {"S": S, "off_high": off_high}
    return None


def check_retest(peaks, l, c, n):
    """D: an old peak broken 3-20 sessions ago, price came back within 2% of it, still closing above."""
    best = None
    for pi, pv in peaks:
        above = np.where(c[pi + 1:] > pv)[0]
        if len(above) == 0:
            continue
        b = pi + 1 + above[0]
        if not (n - 21 <= b <= n - 4) or pi < b - 250:
            continue
        if l[b + 1:].min() > pv * (1 + RETEST_NEAR_PCT / 100):
            continue
        if c[-1] < pv or c[b:].min() < pv * 0.98:
            continue
        if best is None or pv > best["P"]:
            best = {"P": pv, "b": b}
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


def trailing_return(c, days):
    return pct(c[-1], c[-days - 1]) if len(c) > days else np.nan


# ---------------------------------------------------------------- per-stock analysis
def analyse(sym, df, bands, banned, nifty, segment="F&O", surveillance=None, in_mid150=False):
    surveillance = surveillance or {}
    o, h, l, c, v = (df[k].to_numpy(dtype=float) for k in ("Open", "High", "Low", "Close", "Volume"))
    n = len(c)
    dates = df.index
    fmt = lambda i: dates[i].strftime("%d %b")  # noqa: E731

    peaks, troughs = swing_points(h, l)
    A, last_trough = check_uptrend(peaks, troughs, n, c[-1])
    B = check_base_breakout(h, l, c, v, n)
    supports = support_levels(peaks, last_trough, c, n)
    C = check_pullback(A, supports, h, l, c)
    D = check_retest(peaks, l, c, n)
    candle = check_candle(o, h, l, c)
    near_S = next((S for S in supports if S * 0.97 <= l[-2:].min() <= S * (1 + NEAR_SUPPORT_PCT / 100)), None)
    E = bool(candle and (C or D or near_S is not None))

    ret1, ret3 = trailing_return(c, 21), trailing_return(c, 63)
    G = bool(ret1 == ret1 and ret3 == ret3 and ret1 > nifty["ret_1m"] and ret3 > nifty["ret_3m"])

    vr_today = vol_ratio_at(v, n - 1)
    trig_vr = B["vr"] if B else vr_today
    VOL = bool(trig_vr == trig_vr and trig_vr >= VOL_MULT and (B or C or D or E))

    # ---- entry style and levels (priority: breakout > retest > pullback > candle)
    if B:
        style = "Breakout"
        entry_low, entry_high = h[-1], h[-1] * (1 + ENTRY_BUFFER)
        support = B["bh"]
    elif D or C or E:
        S = D["P"] if D else (C["S"] if C else near_S)
        style = "Retest" if D else ("Pullback" if C else "Candle at support")
        entry_low, entry_high = S, max(c[-1], S * 1.01)
        support = S
    else:
        style = ""
        entry_low, entry_high = np.nan, np.nan
        support = supports[0] if supports else np.nan
    entry_ref = entry_high if style else c[-1]
    t1, t2 = entry_ref * (1 + T1_PCT), entry_ref * (1 + T2_PCT)
    res = next_resistance(peaks, h, entry_ref)
    room = pct(res, entry_ref) if res == res else np.nan
    F = bool(res != res or room >= MIN_ROOM_PCT)

    has_setup = bool(B or C or D or E)
    eligible = has_setup and F
    pats = {"A": bool(A), "B": bool(B), "C": bool(C), "D": bool(D), "E": E, "G": G, "VOL": VOL}
    score = sum(SCORE[k] for k, on in pats.items() if on)
    setups = "+".join({"VOL": "Vol"}.get(k, k) for k in ("B", "D", "C", "E", "A", "G", "VOL") if pats[k])

    # ---- plain-English reason
    why = []
    if B:
        s = f"Broke out of a {B['L']}-day base (₹{B['bl']:.2f}–₹{B['bh']:.2f}, {B['rng']:.1f}% range) on {fmt(B['bo'])}"
        if B["vr"] == B["vr"]:
            s += f" on {B['vr']:.1f}× normal volume"
        why.append(s)
    if D:
        why.append(f"Retesting ₹{D['P']:.2f}, an old peak it broke on {fmt(D['b'])}, now holding as support")
    if C:
        why.append(f"Pulled back {C['off_high']:.1f}% from its 20-day high to support at ₹{C['S']:.2f} and holding")
    if E:
        why.append(f"{candle} at support")
    if A:
        why.append("Uptrend: higher highs and higher lows")
    if G:
        why.append(f"Beating Nifty: 1M {ret1:+.1f}% vs {nifty['ret_1m']:+.1f}%, 3M {ret3:+.1f}% vs {nifty['ret_3m']:+.1f}%")
    if VOL and not B:
        why.append(f"Volume {vr_today:.1f}× normal on the latest session")
    if res == res:
        why.append(f"Next resistance ₹{res:.2f} ({room:.1f}% above entry)")
    else:
        why.append("No resistance overhead (at or near its 52-week high)")

    missing = []
    if not has_setup:
        missing.append("No entry setup (no breakout, retest, pullback or candle at support)")
    if not F:
        missing.append(f"Room to next resistance only {room:.1f}% (need {MIN_ROOM_PCT:.0f}%)")

    # ---- warning flags (information only, never exclusions)
    band = bands.get(sym, "unknown")
    value20 = (c[-20:] * v[-20:]).mean() / 1e7
    flags = []
    if sym in banned:
        flags.append("F&O ban list (no new F&O positions; cash buying allowed)")
    for name, syms in surveillance.items():
        if sym in syms:
            flags.append(f"On NSE {name} list (surveillance; higher margin / trade restrictions possible)")
    if band in ("2", "5", "2.0", "5.0"):
        flags.append(f"{band}% price band (daily move capped at {band}%)")
    if n < SHORT_HISTORY_FLAG:
        flags.append(f"Short history: {n} sessions, limited price structure")
    if segment == "Midcap 150" and value20 < MIN_VALUE_CR:
        flags.append(f"Thin liquidity: Rs {value20:.0f} cr/day avg")

    hi52 = h[-252:].max()
    return {
        "symbol": sym, "segment": segment, "in_midcap150": bool(in_mid150),
        "date": dates[-1].strftime("%Y-%m-%d"), "history_sessions": n,
        "eligible": eligible, "score": score, "setups": setups, "entry_style": style,
        "reason": "; ".join(why), "not_eligible_because": "; ".join(missing),
        "flags": "; ".join(flags), "n_flags": len(flags),
        "close": r2(c[-1]), "chg_pct": r2(pct(c[-1], c[-2])),
        "entry_low": r2(entry_low), "entry_high": r2(entry_high),
        "t1": r2(t1) if style else None, "t2": r2(t2) if style else None, "time_exit_days": TIME_EXIT_DAYS,
        "support": r2(support), "resistance": r2(res), "room_pct": r2(room),
        "pat_A_uptrend": pats["A"], "pat_B_base_breakout": pats["B"], "pat_C_pullback": pats["C"],
        "pat_D_retest": pats["D"], "pat_E_candle": pats["E"], "pat_F_room": F, "pat_G_rel_strength": pats["G"],
        "vol_ok": pats["VOL"], "vol_ratio_today": r2(vr_today), "trigger_vol_ratio": r2(trig_vr),
        "candle": candle or "", "ret_1m": r2(ret1), "ret_3m": r2(ret3),
        "rs_3m_vs_nifty": r2(ret3 - nifty["ret_3m"]) if ret3 == ret3 else None,
        "high52": r2(hi52), "pct_below_high52": r2(pct(hi52, c[-1])),
        "base_days": B["L"] if B else None, "base_high": r2(B["bh"]) if B else None,
        "base_low": r2(B["bl"]) if B else None, "base_range_pct": r2(B["rng"]) if B else None,
        "breakout_date": dates[B["bo"]].strftime("%Y-%m-%d") if B else None,
        "retest_level": r2(D["P"]) if D else None,
        "retest_break_date": dates[D["b"]].strftime("%Y-%m-%d") if D else None,
        "pullback_support": r2(C["S"]) if C else None,
        "last_swing_trough": r2(last_trough), "price_band": band, "avg_value20_cr": r2(value20),
    }


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
        table = table.sort_values(["eligible", "score", "rs_3m_vs_nifty", "trigger_vol_ratio"],
                                  ascending=[False, False, False, False], na_position="last")
        latest_date = table["date"].mode().iloc[0]
        table["stale"] = table["date"] != latest_date
        table.insert(0, "rank", range(1, len(table) + 1))
    else:
        latest_date = None
    table.to_csv(os.path.join(OUT_DIR, "latest.csv"), index=False, encoding="utf-8")

    elig = table[table["eligible"]] if not table.empty else table
    meta = {
        "generated_at_ist": datetime.now(IST).strftime("%Y-%m-%d %H:%M"),
        "data_date": latest_date,
        "method": "price action + volume only; no indicators; no stop-loss",
        "universe_source": (f"F&O: {fno_src}; Nifty Midcap 150: {mid150_src}; others: {eq_src} "
                            f"filtered to 20-day avg traded value >= Rs 50 cr"),
        "fno_count": len(fno), "midcap150_count": len(mid150),
        "midcap150_non_fno_count": len(mid_only), "liquid_non_fno_count": len(liquid),
        "universe_count": len(universe), "stocks_analysed": len(rows),
        "stocks_failed_download": failed,
        "note_failed": f"Listed fewer than {MIN_HISTORY} sessions ago or no Yahoo data",
        "eligible_count": int(len(elig)),
        "pattern_counts": {k: int(table[k].sum()) for k in table.columns if k.startswith("pat_") or k == "vol_ok"}
        if not table.empty else {},
        "score_points": SCORE, "targets_pct": [T1_PCT * 100, T2_PCT * 100], "time_exit_days": TIME_EXIT_DAYS,
        "nifty": {k: (r2(v) if isinstance(v, float) else v) for k, v in nifty.items()},
        "fno_ban": ban,
        "asm_gsm": {k: {"status": v["status"], "count": len(v["symbols"])} for k, v in surv.items()},
        "price_band_source": "NSE sec_list.csv" if bands else "not available",
        "flags_not_rejections": ["F&O ban", "ASM/GSM list", "2%/5% price band", "short price history",
                                 "thin liquidity (Midcap 150)"],
        "price_source": "Yahoo Finance via yfinance (unofficial)",
    }
    with open(os.path.join(OUT_DIR, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
    print(json.dumps({k: meta[k] for k in ("data_date", "stocks_analysed", "eligible_count",
                                           "pattern_counts", "nifty")}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
