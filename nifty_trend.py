"""Nifty trend on three timeframes, used to tag the option chain readings in oc_learn.py.

  weekly   - the big trend, from 10 years of weekly candles
  125 min  - the smaller trend inside it (3 candles a day: 9:15, 11:20, 13:25)
  25 min   - the timing view for entries (15 candles a day)

Each timeframe is called up, down or sideways by the same rule: up when the close is above its fast
average and the fast average is above the slow one, down when both are the other way round,
sideways otherwise. Only candles that had finished by a reading's time are used for that reading.

Prices come from Yahoo Finance (^NSEI) and are kept in data/nifty_trend/, so the 5-minute history
keeps growing past the 60 days Yahoo serves, and a failed fetch falls back to what is saved.
This is price context only; the option learning itself still uses only the live snapshots.
"""

import os

import numpy as np
import pandas as pd

DIR = os.path.join("data", "nifty_trend")
WEEKLY = os.path.join(DIR, "weekly.csv")
FIVE_MIN = os.path.join(DIR, "nifty_5m.csv")
OPEN = pd.Timedelta(hours=9, minutes=15)
CLOSE = pd.Timedelta(hours=15, minutes=30)
# timeframe: (candle minutes, fast average, slow average), in candles
FRAMES = {"weekly": (None, 20, 50), "125m": (125, 6, 15), "25m": (25, 6, 15)}
WORDS = {"weekly": ("bullish", "bearish", "sideways"), "125m": ("up", "down", "sideways"),
         "25m": ("up", "down", "sideways")}


def _merge_save(new, path):
    old = pd.read_csv(path, parse_dates=["start"]) if os.path.exists(path) else pd.DataFrame()
    d = pd.concat([old, new], ignore_index=True)
    if d.empty:
        return d
    d = d.drop_duplicates("start", keep="last").sort_values("start").reset_index(drop=True)
    d.to_csv(path, index=False)
    return d


def _clean(h):
    """Yahoo history -> start (naive IST), close."""
    h = h.dropna(subset=["Close"])
    idx = h.index.tz_convert("Asia/Kolkata").tz_localize(None) if h.index.tz is not None else h.index
    return pd.DataFrame({"start": idx, "close": h["Close"].to_numpy(float)})


def fetch():
    """Updates the saved weekly and 5-minute candles. Returns (weekly, five_min)."""
    os.makedirs(DIR, exist_ok=True)
    w = m = pd.DataFrame()
    try:
        import yfinance as yf
        t = yf.Ticker("^NSEI")
        w = _clean(t.history(period="10y", interval="1wk", auto_adjust=False))
        m = _clean(t.history(period="60d", interval="5m", auto_adjust=False))
    except Exception as e:          # no network or no yfinance: use what is saved
        print(f"nifty_trend: fetch failed ({e}); using saved candles")
    if not w.empty:
        w["start"] = w["start"].dt.normalize()
        w.to_csv(WEEKLY, index=False)          # weekly candles get revised, so take Yahoo's whole set
    else:
        w = pd.read_csv(WEEKLY, parse_dates=["start"]) if os.path.exists(WEEKLY) else w
    if not m.empty:
        t = m["start"] - m["start"].dt.normalize()
        m = m[(t >= OPEN) & (t < CLOSE)]
    m = _merge_save(m, FIVE_MIN)
    return w, m


def candles(five_min, minutes):
    """5-minute closes -> candles of `minutes`, starting at 9:15 each day, with their end time."""
    if five_min.empty:
        return pd.DataFrame(columns=["end", "close"])
    s = five_min["start"]
    day = s.dt.normalize()
    k = ((s - day - OPEN) // pd.Timedelta(minutes=minutes)).astype(int)
    g = five_min.assign(day=day, k=k).groupby(["day", "k"])
    c = g["close"].last().reset_index()
    last5 = g["start"].max().reset_index(drop=True)
    c["end"] = c["day"] + OPEN + pd.to_timedelta((c["k"] + 1) * minutes, unit="min")
    c["end"] = c["end"].where(c["end"] <= c["day"] + CLOSE, c["day"] + CLOSE)
    # keep only candles whose data reaches their end (the in-progress one at fetch time is dropped)
    full = last5 + pd.Timedelta(minutes=5) >= c["end"]
    return c.loc[full, ["end", "close"]].reset_index(drop=True)


def label(c, frame):
    """Adds the trend word to each candle."""
    _, fast, slow = FRAMES[frame]
    up_w, down_w, side_w = WORDS[frame]
    c = c.copy()
    f = c["close"].rolling(fast).mean()
    s = c["close"].rolling(slow).mean()
    c["trend"] = np.select([(c["close"] > f) & (f > s), (c["close"] < f) & (f < s)], [up_w, down_w], side_w)
    c.loc[s.isna(), "trend"] = "unknown"
    return c


def trends_at(times, weekly, five_min):
    """For each reading time: the trend on each timeframe from the candles finished by then."""
    times = pd.Series(pd.to_datetime(times)).reset_index(drop=True)
    out = pd.DataFrame(index=times.index)
    frames = {"weekly": weekly.assign(end=weekly["start"] + pd.Timedelta(days=4) + CLOSE)[["end", "close"]]
              if not weekly.empty else pd.DataFrame(columns=["end", "close"])}
    for f in ("125m", "25m"):
        frames[f] = candles(five_min, FRAMES[f][0])
    q = pd.DataFrame({"t": times.astype("datetime64[ns]"), "i": times.index}).sort_values("t")
    for f, c in frames.items():
        col = f"trend_{f}"
        if c.empty:
            out[col] = "unknown"
            continue
        c = label(c.sort_values("end").reset_index(drop=True), f)
        m = pd.merge_asof(q, c[["end", "trend"]].astype({"end": "datetime64[ns]"}), left_on="t",
                          right_on="end", direction="backward")
        out.loc[m["i"].to_numpy(), col] = m["trend"].fillna("unknown").to_numpy()
    return out
