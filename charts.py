"""
Annotated candlestick chart for each stock on the daily list (price action + volume only, no indicators).

One PNG per stock, sized for a phone email (shown about 340-600 px wide; tap opens it full size):
  top strip    - 1 year of daily candles for context, with support / next resistance and the zoom window shaded
  main panel   - the last ~3 months zoomed in, with everything the scanner used:
                 support, next resistance, base box (breakout) or old peak (retest), swing highs/lows (HH/HL/LH/LL),
                 buy zone and T1/T2 bands, order block, fair value gap, liquidity sweep, change of character
  volume panel - daily volume of the zoom window, trigger day highlighted with its x-normal ratio
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
from matplotlib.patches import Rectangle            # noqa: E402
import numpy as np                                  # noqa: E402
import pandas as pd                                 # noqa: E402

YEAR = 250            # sessions in the top strip
ZOOM = 66             # sessions in the main panel (about 3 months); widened to show an older zone
ZOOM_MAX = 95
FUTURE = 9            # empty sessions on the right for the zone / target labels

INK, INK2, MUTED, GRID = "#1f2328", "#57606a", "#8c959f", "#eaeef2"
UP, DOWN = "#1a7f37", "#cf222e"
C_ZONE, C_TGT, C_SUP, C_RES = "#2da44e", "#d4a72c", "#0969da", "#953800"
C_BASE, C_OB, C_FVG, C_SWEEP, C_CHOCH = "#0969da", "#8250df", "#1b7c83", "#bf3989", "#cf222e"


def _num(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return None if x != x else x


def _idx(dates, d):
    """Position of date string d in the index (None if missing)."""
    if not d or d != d:
        return None
    hit = np.where(dates.strftime("%Y-%m-%d") == str(d)[:10])[0]
    return int(hit[0]) if len(hit) else None


def _candles(ax, o, h, l, c, x0, width):
    up = c >= o
    xs = np.arange(len(c)) + x0
    for sel, col in ((up, UP), (~up, DOWN)):
        ax.vlines(xs[sel], l[sel], h[sel], color=col, linewidth=max(0.6, width * 1.1), zorder=3)
        body = np.maximum(np.abs(c - o), (h.max() - l.min()) * 0.0015)
        ax.bar(xs[sel], body[sel], bottom=np.minimum(o, c)[sel], width=width, color=col,
               edgecolor=col, linewidth=0.3, zorder=4)


def _hline(ax, y, x0, x1, color, style="-", lw=1.4, z=2):
    ax.hlines(y, x0, x1, colors=color, linestyles=style, linewidth=lw, zorder=z)


def _tag(ax, x, y, text, color, size=10.5, ha="left", va="center", bold=True):
    ax.text(x, y, text, color=color, fontsize=size, ha=ha, va=va, fontweight="bold" if bold else "normal",
            zorder=9, bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.85))


def _fmt(v):
    return f"{v:,.0f}" if v >= 1000 else f"{v:,.1f}"


def draw(sym, df, row, peaks, troughs, path):
    """Draw one chart. row = the stock's latest.csv row (dict); peaks/troughs = swing points (index, price)."""
    df = df.tail(YEAR + 40)
    o, h, l, c, v = (df[k].to_numpy(dtype=float) for k in ("Open", "High", "Low", "Close", "Volume"))
    dates = df.index
    n = len(c)
    full_n = int(row.get("history_sessions") or n)
    off = full_n - n                                  # swing indexes are on the full history; shift them
    peaks = [(i - off, p) for i, p in peaks if i - off >= 0]
    troughs = [(i - off, p) for i, p in troughs if i - off >= 0]

    g = {k: _num(row.get(k)) for k in ("entry_low", "entry_high", "t1", "t2", "support", "resistance", "close",
                                         "base_high", "base_low", "base_days", "retest_level", "sweep_level",
                                         "ob_low", "ob_high", "fvg_low", "fvg_high", "choch_level",
                                         "trigger_vol_ratio", "score", "rank")}
    style = row.get("entry_style") or ""
    bo = _idx(dates, row.get("breakout_date"))
    rb = _idx(dates, row.get("retest_break_date"))
    obk = _idx(dates, row.get("ob_date"))
    fvi = _idx(dates, row.get("fvg_date"))

    # ---- zoom window: last ~3 months, widened (up to ~4.5 months) to show an older base / zone / retest break
    starts = [n - ZOOM]
    if bo is not None and g["base_days"]:
        starts.append(bo - int(g["base_days"]) - 3)
    for k in (obk, fvi, rb):
        if k is not None:
            starts.append(k - 5)
    z0 = max(0, min(max(min(starts), n - ZOOM_MAX), n - ZOOM))
    zs = slice(z0, n)
    zn = n - z0

    fig = plt.figure(figsize=(4.4, 6.8), dpi=170)
    gs = fig.add_gridspec(3, 1, height_ratios=[2.1, 5.2, 1.5], hspace=0.12,
                          left=0.03, right=0.775, top=0.905, bottom=0.10)
    ax1, ax2, ax3 = (fig.add_subplot(gs[i]) for i in range(3))

    rank = f"#{int(g['rank'])} " if g["rank"] else ""
    score = f" · score {int(g['score'])}" if g["score"] is not None else ""
    fig.text(0.03, 0.972, f"{rank}{sym}", fontsize=14, fontweight="bold", color=INK, va="center")
    fig.text(0.97, 0.972, f"{style or 'Watch'}{score}", fontsize=8.5, color=INK2, ha="right", va="center")
    fig.text(0.03, 0.937, f"Close ₹{_fmt(c[-1])} on {dates[-1].strftime('%d %b %Y')} · daily candles",
             fontsize=8.5, color=INK2, va="center")

    # ---- top strip: 1 year
    y0 = max(0, n - YEAR)
    _candles(ax1, o[y0:], h[y0:], l[y0:], c[y0:], y0, 0.62)
    ax1.axvspan(z0 - 0.5, n - 0.5, color="#ddf4ff", zorder=0)
    lo1, hi1 = l[y0:].min(), h[y0:].max()
    if g["support"] and lo1 * 0.9 < g["support"] < hi1 * 1.1:
        _hline(ax1, g["support"], y0, n + 2, C_SUP, lw=1.1)
    if g["resistance"] and g["resistance"] < hi1 * 1.15:
        _hline(ax1, g["resistance"], y0, n + 2, C_RES, "--", lw=1.1)
    k52 = y0 + int(np.argmax(h[y0:]))
    ax1.annotate(f"52w high {_fmt(h[k52])}", (k52, h[k52]), xytext=(-6, 2), textcoords="offset points",
                 fontsize=8, color=INK2, ha="right", va="bottom", zorder=9)
    ax1.set_xlim(y0 - 1, n + 2)
    ax1.set_ylim(lo1 - (hi1 - lo1) * 0.05, hi1 + (hi1 - lo1) * 0.18)
    ax1.text(0.01, 0.95, "1 year", transform=ax1.transAxes, fontsize=8.5, color=INK2, va="top", fontweight="bold")
    ticks1 = [i for i in range(y0, n) if i == y0 or dates[i].month != dates[i - 1].month][1::2]
    ax1.set_xticks(ticks1, [dates[i].strftime("%b") for i in ticks1])

    # ---- main panel: last ~3 months
    xr = n - 1 + FUTURE
    _candles(ax2, o[zs], h[zs], l[zs], c[zs], z0, 0.66)
    levels = [l[zs].min(), h[zs].max()] + [g[k] for k in ("entry_low", "entry_high", "t1", "t2", "support")
                                             if g[k]]
    lo, hi = min(levels), max(levels)
    if g["resistance"] and g["resistance"] <= hi * 1.06:
        hi = max(hi, g["resistance"])
    pad = (hi - lo) * 0.06
    ax2.set_ylim(lo - pad, hi + pad * 1.6)
    ax2.set_xlim(z0 - 1, xr + 0.5)
    right_tags = []                                   # (y, text, colour) labels in the right margin

    if g["entry_low"] and g["entry_high"]:
        zx0 = n - 4
        ax2.add_patch(Rectangle((zx0, g["entry_low"]), xr - zx0, g["entry_high"] - g["entry_low"],
                                fc=C_ZONE, alpha=0.22, ec=C_ZONE, lw=1.2, zorder=1))
        lab = "Buy >" if style == "Breakout" else "Zone"
        if not (g["support"] and abs(g["support"] / g["entry_low"] - 1) < 0.003):   # same line as support
            right_tags += [(g["entry_low"], f"{lab} {_fmt(g['entry_low'])}", "#116329")]
    if g["t1"] and g["t2"]:
        ax2.add_patch(Rectangle((n - 4, g["t1"]), xr - n + 4, g["t2"] - g["t1"],
                                fc=C_TGT, alpha=0.22, ec="none", zorder=1))
        _hline(ax2, g["t1"], n - 4, xr, C_TGT, lw=1.2)
        _hline(ax2, g["t2"], n - 4, xr, C_TGT, lw=1.2)
        right_tags += [(g["t1"], f"T1 {_fmt(g['t1'])}", "#7d4e00"), (g["t2"], f"T2 {_fmt(g['t2'])}", "#7d4e00")]

    if g["support"]:
        _hline(ax2, g["support"], z0, xr, C_SUP, lw=1.5)
        right_tags.append((g["support"], f"Supp {_fmt(g['support'])}", C_SUP))
    if g["resistance"]:
        if g["resistance"] <= ax2.get_ylim()[1]:
            _hline(ax2, g["resistance"], z0, xr, C_RES, "--", lw=1.5)
            right_tags.append((g["resistance"], f"Wall {_fmt(g['resistance'])}", C_RES))
        else:
            _tag(ax2, xr, ax2.get_ylim()[1], f"Wall {_fmt(g['resistance'])} ↑", C_RES, size=8.5, ha="right",
                 va="top")
    else:
        _tag(ax2, xr, ax2.get_ylim()[1], "No wall overhead", C_RES, size=8.5, ha="right", va="top")

    # base box (breakout) or old peak (retest)
    if bo is not None and g["base_high"] and g["base_low"] and g["base_days"]:
        bs = bo - int(g["base_days"])
        ax2.add_patch(Rectangle((bs - 0.5, g["base_low"]), bo - bs, g["base_high"] - g["base_low"],
                                fc=C_BASE, alpha=0.07, ec=C_BASE, lw=1.6, ls="--", zorder=2))
        _tag(ax2, bs, g["base_high"], f"{int(g['base_days'])}-day base", C_BASE, size=8.5, va="bottom")
        ax2.annotate("Breakout", (bo, l[bo]), xytext=(0, -26), textcoords="offset points", ha="center",
                     fontsize=8.5, color=C_BASE, fontweight="bold", zorder=9,
                     arrowprops=dict(arrowstyle="-|>", color=C_BASE, lw=1.2))
    if g["retest_level"]:
        pk = next((i for i, p in reversed(peaks) if abs(p - g["retest_level"]) < 0.01 * g["retest_level"]), None)
        x_from = max(z0, pk) if pk is not None else z0
        _hline(ax2, g["retest_level"], x_from, n - 1, C_BASE, (0, (5, 3)), lw=1.6, z=3)
        if rb is not None and rb >= z0:
            ax2.annotate("Broke old peak", (rb, l[rb]), xytext=(0, -44), textcoords="offset points",
                         ha="center", fontsize=9, color=C_BASE, fontweight="bold", zorder=9,
                         arrowprops=dict(arrowstyle="-|>", color=C_BASE, lw=1.1))
        _tag(ax2, n - 2, g["retest_level"], "Retest", C_BASE, size=8.5, ha="right", va="top")

    # SMC zones
    if obk is not None and g["ob_low"] and g["ob_high"]:
        ax2.add_patch(Rectangle((obk - 0.5, g["ob_low"]), n - 0.5 - obk, g["ob_high"] - g["ob_low"],
                                fc=C_OB, alpha=0.16, ec=C_OB, lw=1.1, zorder=1))
        _tag(ax2, obk, g["ob_low"], "Order block", C_OB, size=8.5, va="top")
    if fvi is not None and g["fvg_low"] and g["fvg_high"]:
        ax2.add_patch(Rectangle((fvi - 0.5, g["fvg_low"]), n - 0.5 - fvi, g["fvg_high"] - g["fvg_low"],
                                fc=C_FVG, alpha=0.16, ec=C_FVG, lw=1.1, ls=":", zorder=1))
        _tag(ax2, fvi, g["fvg_high"], "Fair value gap", C_FVG, size=8.5, va="bottom")
    if g["sweep_level"]:
        k = n - 3 + int(np.argmin(l[-3:]))
        _hline(ax2, g["sweep_level"], max(z0, n - 25), n - 1, C_SWEEP, ":", lw=1.4, z=3)
        ax2.annotate("Sweep", (k, l[k]), xytext=(-18, -24), textcoords="offset points", ha="center",
                     fontsize=8.5, color=C_SWEEP, fontweight="bold", zorder=9,
                     arrowprops=dict(arrowstyle="-|>", color=C_SWEEP, lw=1.2))
    if g["choch_level"]:
        _hline(ax2, g["choch_level"], max(z0, n - 30), n - 1, C_CHOCH, (0, (2, 2)), lw=1.6, z=3)
        _tag(ax2, max(z0, n - 30), g["choch_level"], "CHoCH (trend may be ending)", C_CHOCH, size=9,
             va="bottom")

    # swing highs / lows in view: HH / LH and HL / LL against the previous swing
    for pts, above in ((peaks, True), (troughs, False)):
        for j, (i, p) in enumerate(pts):
            if i < z0 or j == 0 or j < len(pts) - 2:      # the last 2 swing highs and lows: what the trend check uses
                continue
            prev = pts[j - 1][1]
            txt = ("HH" if p > prev else "LH") if above else ("HL" if p > prev else "LL")
            good = txt in ("HH", "HL")
            ax2.annotate(txt, (i, p), xytext=(0, 7 if above else -7), textcoords="offset points",
                         ha="center", va="bottom" if above else "top", fontsize=8.5, fontweight="bold",
                         color=UP if good else DOWN, zorder=8)

    # right-margin price labels, nudged apart so they never overlap
    ymin, ymax = ax2.get_ylim()
    gap = (ymax - ymin) * 0.045
    placed = []
    for y, txt, col in sorted(right_tags, key=lambda t: t[0]):
        yy = max(y, placed[-1] + gap) if placed else y
        placed.append(yy)
        ax2.text(1.012, (yy - ymin) / (ymax - ymin), txt, transform=ax2.transAxes, fontsize=8.5, color=col,
                 fontweight="bold", va="center", ha="left", clip_on=False)
    ax2.text(0.01, 0.985, "Last 3 months", transform=ax2.transAxes, fontsize=8.5, color=INK2, va="top",
             fontweight="bold")

    # ---- volume
    vv = v[zs]
    trig = bo if (style == "Breakout" and bo is not None) else n - 1
    cols = ["#afb8c1"] * zn
    if trig >= z0:
        cols[trig - z0] = "#0969da"
    ax3.bar(np.arange(z0, n), vv, width=0.7, color=cols, zorder=3)
    ax3.set_xlim(ax2.get_xlim())
    ax3.set_ylim(0, vv.max() * 1.3 if vv.max() > 0 else 1)
    if trig >= z0 and g["trigger_vol_ratio"]:
        when = "breakout day" if trig != n - 1 else "last day"
        ax3.text(trig, v[trig], f"{when} {g['trigger_vol_ratio']:.1f}× usual", fontsize=8.5, color="#0969da",
                 fontweight="bold", ha="right" if trig > n - 6 else "center", va="bottom", zorder=9)
    ax3.text(0.01, 0.95, "Volume", transform=ax3.transAxes, fontsize=8.5, color=INK2, va="top", fontweight="bold")
    ticks = [i for i in range(z0, n) if i == z0 or dates[i].month != dates[i - 1].month]
    ticks = [i for i in ticks if i - z0 > 3]
    ax3.set_xticks(ticks, [dates[i].strftime("%b") for i in ticks])

    for ax in (ax1, ax2, ax3):
        ax.yaxis.tick_right()
        ax.tick_params(axis="both", labelsize=7.5, colors=MUTED, length=0)
        ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_facecolor("white")
    ax2.set_yticklabels([])
    ax2.set_xticks([])
    ax3.set_yticks([])
    ax1.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, _: f"{y:,.0f}"))

    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    keys = [Patch(fc=C_ZONE, alpha=0.35, label="buy zone"), Patch(fc=C_TGT, alpha=0.45, label="T1→T2"),
            Line2D([], [], color=C_SUP, lw=1.6, label="support"),
            Line2D([], [], color=C_RES, lw=1.6, ls="--", label="next wall"),
            Patch(fc="#ddf4ff", label="zoomed part")]
    fig.legend(handles=keys, loc="lower left", bbox_to_anchor=(0.01, 0.02), ncol=3, fontsize=7.5, frameon=False,
               handlelength=1.3, columnspacing=0.9, handletextpad=0.4)
    fig.text(0.03, 0.008, "Price action + volume only, no indicators. Research, not advice.",
             fontsize=6.5, color=MUTED)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=170, facecolor="white")
    plt.close(fig)
    _shrink(path)
    return path


def _shrink(path, colours=96):
    """Cut the PNG to a small palette so each chart stays around 40-70 KB."""
    try:
        from PIL import Image
        im = Image.open(path).convert("RGB")
        im.quantize(colors=colours, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(
            path, optimize=True)
    except Exception as e:
        print("chart shrink skipped:", e)


def prune(root, keep_days=45, today=None):
    """Delete chart folders older than keep_days (folder names are data dates, YYYY-MM-DD)."""
    if not os.path.isdir(root):
        return
    cutoff = (pd.Timestamp(today) if today else pd.Timestamp.now()) - pd.Timedelta(days=keep_days)
    for d in os.listdir(root):
        try:
            if pd.Timestamp(d) < cutoff:
                for f in os.listdir(os.path.join(root, d)):
                    os.remove(os.path.join(root, d, f))
                os.rmdir(os.path.join(root, d))
        except (ValueError, OSError):
            pass
