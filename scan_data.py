"""
Daily NSE swing-scan data builder (runs on GitHub Actions).

Downloads ~2 years of daily prices for the NSE F&O stock universe plus
Nifty 50 and India VIX, calculates every indicator used by the swing-trade
rules, applies the mechanical checks, and writes:
  data/latest.csv  - one row per stock with indicators, levels and pass/fail reasons
  data/meta.json   - data date, market filter numbers, F&O ban list, run stats
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
INDEX_SYMBOLS = {"NIFTY", "BANKNIFTY", "FINNIFTY", "MIDCPNIFTY", "NIFTYNXT50", "SENSEX", "BANKEX"}

# ---- Rule parameters (from the trade plan) ----
T1_PCT, T2_PCT = 0.03, 0.05
MAX_STOP_PCT = 0.02
MIN_RR_T1 = 1.5
ATR_MULT_MIN_STOP = 0.75
MAX_EXT_ABOVE_EMA20 = 6.0
RSI_LO, RSI_HI = 55, 70
BREAKOUT_VOL_MULT = 1.5
TRIGGER_VOL_MULT = 1.3
CLOSE_TOP_OF_RANGE = 0.70
MIN_VALUE_CR = 50
ENTRY_BUFFER = 0.005          # entry range = trigger high .. trigger high +0.5%
RISK_PER_LAKH = 1000          # 1% of Rs 1,00,000

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


# ---------------------------------------------------------------- prices
def download(tickers, retries=3):
    frames = {}
    for i in range(0, len(tickers), 40):
        chunk = tickers[i:i + 40]
        for attempt in range(retries):
            try:
                raw = yf.download(chunk, period="2y", interval="1d", group_by="ticker",
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
                if len(df) >= 210:
                    frames[t] = df
            except Exception:
                pass
        time.sleep(1)
    return frames


# ---------------------------------------------------------------- indicators
def ema(s, n):
    return s.ewm(span=n, adjust=False).mean()


def rsi(close, n=14):
    d = close.diff()
    gain = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    loss = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return (100 - 100 / (1 + rs)).fillna(100)


def atr(df, n=14):
    pc = df["Close"].shift(1)
    tr = pd.concat([df["High"] - df["Low"], (df["High"] - pc).abs(), (df["Low"] - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def nearest_resistance(df, above, lookback=250, w=5):
    """Nearest pivot high (higher than 5 bars each side) above `above`, within the lookback."""
    h = df["High"].values[-lookback:]
    levels = []
    for i in range(w, len(h) - w):
        if h[i] == h[i - w:i + w + 1].max() and h[i] > above:
            levels.append(h[i])
    hi52 = df["High"].values[-252:].max()
    if hi52 > above:
        levels.append(hi52)
    return min(levels) if levels else np.nan


def r2(x):
    return None if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))) else round(float(x), 2)


def analyse(sym, df, bands, banned):
    c, h, l, v = df["Close"], df["High"], df["Low"], df["Volume"]
    e20, e50, e200 = ema(c, 20), ema(c, 50), ema(c, 200)
    r = rsi(c)
    macd = ema(c, 12) - ema(c, 26)
    sig = ema(macd, 9)
    hist = macd - sig
    a = atr(df)
    avg_vol20 = v.shift(1).rolling(20).mean()          # prior 20 sessions (excludes trigger day)
    value20_cr = (c * v).rolling(20).mean() / 1e7

    C, H, L, V = c.iloc[-1], h.iloc[-1], l.iloc[-1], v.iloc[-1]
    E20, E50, E200 = e20.iloc[-1], e50.iloc[-1], e200.iloc[-1]
    RSI = r.iloc[-1]
    ATR = a.iloc[-1]
    AV = avg_vol20.iloc[-1]
    vol_ratio = V / AV if AV and AV > 0 else np.nan
    pull_vol_ratio = v.iloc[-4:-1].mean() / AV if AV and AV > 0 else np.nan   # 3 sessions before trigger
    rng = H - L
    range_pos = (C - L) / rng if rng > 0 else np.nan
    ext = (C / E20 - 1) * 100
    prior20_high = h.shift(1).rolling(20).max().iloc[-1]
    prev_high = h.iloc[-2]
    hi52 = h.iloc[-252:].max()

    trend_ok = C > E20 > E50 and C > E200
    ext_ok = ext <= MAX_EXT_ABOVE_EMA20
    rsi_ok = RSI_LO <= RSI <= RSI_HI
    macd_ok = macd.iloc[-1] > sig.iloc[-1] and hist.iloc[-1] > hist.iloc[-2]
    value_ok = value20_cr.iloc[-1] >= MIN_VALUE_CR  # info only: F&O stocks pass the universe rule anyway

    is_breakout = C > prior20_high and vol_ratio >= BREAKOUT_VOL_MULT and range_pos >= CLOSE_TOP_OF_RANGE
    is_pullback = (not is_breakout) and pull_vol_ratio < 1 and vol_ratio >= TRIGGER_VOL_MULT and C > prev_high
    setup = "Breakout" if is_breakout else ("Pullback trigger" if is_pullback else "")

    # ---- levels, all from the TOP of the entry range
    entry_low = H
    entry_top = H * (1 + ENTRY_BUFFER)
    t1, t2 = entry_top * (1 + T1_PCT), entry_top * (1 + T2_PCT)
    min_dist = ATR_MULT_MIN_STOP * ATR
    atr_too_high = min_dist / entry_top > MAX_STOP_PCT
    cands = {
        "5-day swing low": l.iloc[-5:].min(),
        "10-day swing low": l.iloc[-10:].min(),
        "20 EMA": E20,
    }
    stop, stop_basis = np.nan, ""
    for name, lvl in sorted(cands.items(), key=lambda kv: -kv[1]):
        dist = entry_top - lvl
        if dist >= min_dist and dist / entry_top <= MAX_STOP_PCT:
            stop, stop_basis = lvl, name
            break
    stop_pct = (entry_top - stop) / entry_top * 100 if not np.isnan(stop) else np.nan
    rr1 = (t1 - entry_top) / (entry_top - stop) if not np.isnan(stop) else np.nan
    rr2 = (t2 - entry_top) / (entry_top - stop) if not np.isnan(stop) else np.nan
    res = nearest_resistance(df, entry_top)
    targets_ok = bool(np.isnan(res) or t2 < res)
    shares = math.floor(RISK_PER_LAKH / (entry_top - stop)) if not np.isnan(stop) else None

    band = bands.get(sym, "unknown")
    reasons = []
    if sym in banned:
        reasons.append("In F&O ban list")
    if band in ("2", "5", "2.0", "5.0"):
        reasons.append(f"{band}% price band")
    if not trend_ok:
        reasons.append("Trend fail (need Close>20EMA>50EMA and >200EMA)")
    if not ext_ok:
        reasons.append(f"Extended {ext:.1f}% above 20 EMA")
    if not rsi_ok:
        reasons.append(f"RSI {RSI:.1f} outside 55-70")
    if not macd_ok:
        reasons.append("MACD not above signal with rising histogram")
    if not setup:
        reasons.append("No breakout/pullback trigger today")
    if atr_too_high:
        reasons.append(f"Too volatile: 0.75xATR = {min_dist / entry_top * 100:.2f}% > 2%")
    elif np.isnan(stop):
        reasons.append("No structural stop between 0.75xATR and 2%")
    elif rr1 < MIN_RR_T1:
        reasons.append(f"R:R to T1 {rr1:.2f} < 1.5")
    if not targets_ok:
        reasons.append(f"T2 not below resistance {res:.2f}")

    return {
        "symbol": sym,
        "date": df.index[-1].strftime("%Y-%m-%d"),
        "passes_all_rules": len(reasons) == 0,
        "n_fails": len(reasons),
        "reject_reasons": "; ".join(reasons),
        "setup": setup,
        "open": r2(df["Open"].iloc[-1]), "high": r2(H), "low": r2(L), "close": r2(C),
        "chg_pct": r2((C / c.iloc[-2] - 1) * 100),
        "volume": int(V), "avg_vol20": int(AV) if AV == AV else None,
        "vol_ratio": r2(vol_ratio), "pullback_vol_ratio": r2(pull_vol_ratio),
        "close_range_pos": r2(range_pos),
        "ema20": r2(E20), "ema50": r2(E50), "ema200": r2(E200), "pct_above_ema20": r2(ext),
        "rsi14": r2(RSI), "macd": r2(macd.iloc[-1]), "macd_signal": r2(sig.iloc[-1]),
        "macd_hist": r2(hist.iloc[-1]), "macd_hist_prev": r2(hist.iloc[-2]),
        "atr14": r2(ATR), "atr_pct": r2(ATR / C * 100),
        "avg_value20_cr": r2(value20_cr.iloc[-1]), "value_ok": bool(value_ok),
        "high52": r2(hi52), "prior20_high": r2(prior20_high),
        "swing_low5": r2(cands["5-day swing low"]), "swing_low10": r2(cands["10-day swing low"]),
        "nearest_resistance": r2(res),
        "entry_low": r2(entry_low), "entry_top": r2(entry_top),
        "t1": r2(t1), "t2": r2(t2), "stop": r2(stop), "stop_basis": stop_basis,
        "stop_pct": r2(stop_pct), "rr_t1": r2(rr1), "rr_t2": r2(rr2),
        "shares_per_lakh": shares, "price_band": band,
        "trend_ok": bool(trend_ok), "ext_ok": bool(ext_ok), "rsi_ok": bool(rsi_ok), "macd_ok": bool(macd_ok),
    }


def market_filter(frames):
    out = {}
    n = frames.get("^NSEI")
    if n is not None:
        c = n["Close"]
        out["nifty_date"] = n.index[-1].strftime("%Y-%m-%d")
        out["nifty_close"] = r2(c.iloc[-1])
        out["nifty_ema20"] = r2(ema(c, 20).iloc[-1])
        out["nifty_ema50"] = r2(ema(c, 50).iloc[-1])
        out["nifty_above_20_50"] = bool(c.iloc[-1] > ema(c, 20).iloc[-1] and c.iloc[-1] > ema(c, 50).iloc[-1])
    vx = frames.get("^INDIAVIX")
    if vx is not None:
        c = vx["Close"]
        out["vix_close"] = r2(c.iloc[-1])
        out["vix_5d_change_pct"] = r2((c.iloc[-1] / c.iloc[-6] - 1) * 100)
        out["vix_ok"] = bool(c.iloc[-1] < 20 and (c.iloc[-1] / c.iloc[-6] - 1) * 100 < 15)
    out["market_ok"] = bool(out.get("nifty_above_20_50") and out.get("vix_ok"))
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    universe, universe_src = get_fno_universe()
    ban = get_ban_list()
    banned = set(ban["symbols"])
    bands = get_price_bands()

    tickers = [s + ".NS" for s in universe] + ["^NSEI", "^INDIAVIX"]
    frames = download(tickers)

    # Retry the two indices on their own if the batch missed them
    for idx in ("^NSEI", "^INDIAVIX"):
        if idx not in frames:
            f = download([idx])
            frames.update(f)

    rows, failed = [], []
    for s in universe:
        df = frames.get(s + ".NS")
        if df is None:
            failed.append(s)
            continue
        try:
            rows.append(analyse(s, df, bands, banned))
        except Exception as e:
            print("analyse failed", s, e)
            failed.append(s)

    table = pd.DataFrame(rows)
    if not table.empty:
        table = table.sort_values(["passes_all_rules", "n_fails", "vol_ratio"], ascending=[False, True, False])
        latest_date = table["date"].mode().iloc[0]
        table["stale"] = table["date"] != latest_date
    else:
        latest_date = None
    table.to_csv(os.path.join(OUT_DIR, "latest.csv"), index=False)

    meta = {
        "generated_at_ist": datetime.now(IST).strftime("%Y-%m-%d %H:%M"),
        "data_date": latest_date,
        "universe_source": universe_src,
        "universe_count": len(universe),
        "stocks_analysed": len(rows),
        "stocks_failed_download": failed,
        "valid_setups": int(table["passes_all_rules"].sum()) if not table.empty else 0,
        "fno_ban": ban,
        "price_band_source": "NSE sec_list.csv" if bands else "not available",
        "market": market_filter(frames),
        "rules_not_checked_here": ["ASM/GSM framework", "upcoming events (results, board meetings, ex-dates)"],
        "price_source": "Yahoo Finance via yfinance (unofficial)",
    }
    with open(os.path.join(OUT_DIR, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2)
    print(json.dumps({k: meta[k] for k in ("data_date", "stocks_analysed", "valid_setups", "market")}, indent=2))


if __name__ == "__main__":
    main()
