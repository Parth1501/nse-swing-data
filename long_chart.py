"""
Long-term chart for an investment note: price action and volume only, no indicators.

    python long_chart.py ACUTAAS --zones "3000-3150:Add zone 1,2650-2750:Add zone 2"

Writes data/charts/<date>/<SYM>_long.png (shown in the app through /files/charts/...) and
<SYM>_long.json with the levels and numbers the note's chart section is written from.

  top panel     - about 3 years of weekly candles: weekly swing highs/lows, all-time high,
                  major weekly supports, and the buy zones passed with --zones
  middle panel  - the last 6 months of daily candles with the same levels
  bottom panel  - weekly volume
"""
import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt          # noqa: E402
import numpy as np                       # noqa: E402
import pandas as pd                      # noqa: E402

IST = timezone(timedelta(hours=5, minutes=30))
ROOT = os.path.dirname(os.path.abspath(__file__))
INK, MUTED, GRID = "#1f2328", "#57606a", "#eaeef2"
UP, DOWN, C_SUP, C_RES, C_ZONE, C_ATH = "#1a7f37", "#cf222e", "#0969da", "#953800", "#2da44e", "#8250df"


def load(sym: str) -> pd.DataFrame:
    import yfinance as yf
    for attempt in range(3):
        try:
            df = yf.download(f"{sym}.NS", period="5y", interval="1d", auto_adjust=False, progress=False)
            if df is not None and not df.empty:
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.get_level_values(0)
                return df[["Open", "High", "Low", "Close", "Volume"]].dropna(subset=["Close"])
        except Exception as e:  # noqa: BLE001
            print("download error", e)
    sys.exit(f"no price data for {sym}")


def weekly(df: pd.DataFrame) -> pd.DataFrame:
    w = df.resample("W-FRI").agg({"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"})
    return w.dropna(subset=["Close"])


def swings(h, l, w=3):
    """Swing highs/lows: the bar's high (low) is the highest (lowest) of w bars either side."""
    peaks, troughs = [], []
    for i in range(w, len(h) - w):
        if h[i] == max(h[i - w:i + w + 1]):
            peaks.append(i)
        if l[i] == min(l[i - w:i + w + 1]):
            troughs.append(i)
    return peaks, troughs


def candles(ax, d, width):
    o, h, l, c = (d[k].to_numpy(float) for k in ("Open", "High", "Low", "Close"))
    xs = np.arange(len(c))
    up = c >= o
    for sel, col in ((up, UP), (~up, DOWN)):
        ax.vlines(xs[sel], l[sel], h[sel], color=col, linewidth=0.9, zorder=3)
        body = np.maximum(np.abs(c - o), (h.max() - l.min()) * 0.002)
        ax.bar(xs[sel], body[sel], bottom=np.minimum(o, c)[sel], width=width, color=col, edgecolor=col,
               linewidth=0.3, zorder=4)


def month_ticks(ax, idx, every):
    pos, lab, last = [], [], None
    for i, d in enumerate(idx):
        key = (d.year, d.month)
        if key != last and (d.month - 1) % every == 0:
            pos.append(i)
            lab.append(d.strftime("%b %y"))
        last = key
    ax.set_xticks(pos)
    ax.set_xticklabels(lab, fontsize=9, color=MUTED)


def levels(ax, n, sups, res, ath, zones, lo, hi):
    for k, (a, b, name) in enumerate(zones):
        if b >= lo and a <= hi:
            ax.axhspan(a, b, color=C_ZONE, alpha=0.16, zorder=1)
            ax.text(n + 0.5, b if k % 2 == 0 else a, f"{name} {a:,.0f}-{b:,.0f}", color=C_ZONE, fontsize=8.5,
                    fontweight="bold", va="bottom" if k % 2 == 0 else "top")
    for y in sups:
        if lo <= y <= hi:
            ax.axhline(y, color=C_SUP, linestyle="--", linewidth=1, zorder=2)
            ax.text(n + 0.5, y, f"S {y:,.0f}", color=C_SUP, fontsize=8.5, va="center")
    if res and lo <= res <= hi:
        ax.axhline(res, color=C_RES, linestyle="--", linewidth=1, zorder=2)
        ax.text(n + 0.5, res, f"R {res:,.0f}", color=C_RES, fontsize=8.5, va="center")
    if lo <= ath <= hi * 1.02:
        ax.axhline(ath, color=C_ATH, linestyle=":", linewidth=1.2, zorder=2)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("symbol")
    p.add_argument("--zones", default="", help='"low-high:label,low-high:label"')
    p.add_argument("--date", default=datetime.now(IST).strftime("%Y-%m-%d"))
    a = p.parse_args()
    sym = a.symbol.upper()
    zones = []
    for part in filter(None, (s.strip() for s in a.zones.split(","))):
        rng, _, name = part.partition(":")
        lo_, hi_ = (float(x) for x in rng.split("-"))
        zones.append((lo_, hi_, name or "Zone"))

    df = load(sym)
    w = weekly(df).iloc[-160:]            # about 3 years
    d6 = df.iloc[-126:]                   # about 6 months
    wh, wl, wc = (w[k].to_numpy(float) for k in ("High", "Low", "Close"))
    peaks, troughs = swings(wh, wl, 3)
    close = float(df["Close"].iloc[-1])
    ath = float(df["High"].max())
    ath_date = df["High"].idxmax().strftime("%Y-%m-%d")
    yr = df.iloc[-250:]
    # supports: weekly swing lows below price, plus old swing highs below price that were broken (now support)
    cand = [wl[i] for i in troughs] + [wh[i] for i in peaks if wh[i] < close and any(wc[i + 1:] > wh[i])]
    cand = sorted({round(x, 1) for x in cand if x < close}, reverse=True)
    sups = []
    for x in cand:                         # keep levels at least 4% apart
        if all(abs(x - s) / s > 0.04 for s in sups):
            sups.append(x)
        if len(sups) == 4:
            break
    above = [wh[i] for i in peaks if wh[i] > close]
    res = min(above) if above else None

    fig = plt.figure(figsize=(7.6, 8.4), dpi=150)
    gs = fig.add_gridspec(3, 1, height_ratios=[3.2, 2.4, 0.9], hspace=0.32)
    ax1, ax2, ax3 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1]), fig.add_subplot(gs[2])
    for ax in (ax1, ax2, ax3):
        ax.set_facecolor("white")
        ax.grid(True, color=GRID, linewidth=0.7, zorder=0)
        for s in ax.spines.values():
            s.set_color(GRID)
        ax.tick_params(axis="y", labelsize=9, colors=MUTED)

    n = len(w)
    candles(ax1, w, 0.7)
    lo, hi = float(wl.min()), float(wh.max())
    ax1.set_ylim(lo * 0.94, hi * 1.06)
    ax1.set_xlim(-1, n + 14)
    levels(ax1, n, sups, res, ath, zones, lo * 0.94, hi * 1.06)
    for i in peaks[-6:]:
        ax1.annotate(f"{wh[i]:,.0f}", (i, wh[i]), xytext=(0, 6), textcoords="offset points", ha="center",
                     fontsize=7.5, color=C_RES)
    for i in troughs[-6:]:
        ax1.annotate(f"{wl[i]:,.0f}", (i, wl[i]), xytext=(0, -11), textcoords="offset points", ha="center",
                     fontsize=7.5, color=C_SUP)
    month_ticks(ax1, w.index, 6)
    ax1.set_title(f"{sym} weekly, about 3 years  ·  close {close:,.0f}  ·  high {ath:,.0f} ({ath_date})",
                  fontsize=11, color=INK, loc="left", fontweight="bold")

    m = len(d6)
    candles(ax2, d6, 0.65)
    lo2, hi2 = float(d6["Low"].min()), float(d6["High"].max())
    pad = (hi2 - lo2) * 0.08
    ax2.set_ylim(lo2 - pad, hi2 + pad)
    ax2.set_xlim(-1, m + 22)
    levels(ax2, m, sups, res, ath, zones, lo2 - pad, hi2 + pad)
    month_ticks(ax2, d6.index, 1)
    ax2.set_title("Daily, last 6 months", fontsize=10.5, color=INK, loc="left")

    vol = w["Volume"].to_numpy(float)
    ax3.bar(np.arange(n), vol, width=0.7, color=[UP if c >= o else DOWN for c, o in zip(wc, w["Open"])], alpha=0.6)
    ax3.set_xlim(-1, n + 14)
    month_ticks(ax3, w.index, 6)
    ax3.set_yticks([])
    ax3.set_title("Weekly volume", fontsize=9.5, color=MUTED, loc="left")
    fig.text(0.01, 0.005, "Price and volume only. Analysis, not investment advice.", fontsize=8, color=MUTED)

    out = os.path.join(ROOT, "data", "charts", a.date)
    os.makedirs(out, exist_ok=True)
    png = os.path.join(out, f"{sym}_long.png")
    fig.savefig(png, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    def ret(k):
        return round((close / float(df["Close"].iloc[-1 - k]) - 1) * 100, 1) if len(df) > k else None

    info = {
        "symbol": sym, "as_of": df.index[-1].strftime("%Y-%m-%d"), "close": round(close, 2),
        "all_time_high": round(ath, 2), "all_time_high_date": ath_date,
        "pct_below_ath": round((1 - close / ath) * 100, 1),
        "high_52w": round(float(yr["High"].max()), 2), "low_52w": round(float(yr["Low"].min()), 2),
        "low_52w_date": yr["Low"].idxmin().strftime("%Y-%m-%d"),
        "ret_pct": {"1m": ret(21), "3m": ret(63), "6m": ret(126), "1y": ret(250), "3y": ret(750)},
        "supports": sups, "next_resistance": res,
        "weekly_swing_highs": [[w.index[i].strftime("%Y-%m-%d"), round(wh[i], 1)] for i in peaks[-10:]],
        "weekly_swing_lows": [[w.index[i].strftime("%Y-%m-%d"), round(wl[i], 1)] for i in troughs[-10:]],
        "last_12_weeks": [[i.strftime("%Y-%m-%d"), round(r.Open, 1), round(r.High, 1), round(r.Low, 1),
                           round(r.Close, 1), int(r.Volume)] for i, r in w.iloc[-12:].iterrows()],
        "avg_weekly_volume_13w": int(w["Volume"].iloc[-13:].mean()),
        "avg_weekly_volume_52w": int(w["Volume"].iloc[-52:].mean()),
        "zones": [[z[0], z[1], z[2]] for z in zones],
    }
    with open(os.path.join(out, f"{sym}_long.json"), "w") as f:
        json.dump(info, f, indent=1)
    print(os.path.relpath(png, ROOT))
    print(json.dumps(info, indent=1))


if __name__ == "__main__":
    main()
