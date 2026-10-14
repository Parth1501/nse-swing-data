"""
Nifty option chain pattern log, for option trading with hedged positions (spreads, condors).

Learns only from the live 30-minute snapshots in data/option_chain/ (option_chain.py), going
forward from 14 Oct 2026; no historical backtest. Never changes the snapshot files.

Each snapshot, for the weekly and the monthly expiry, is turned into a PATTERN: a short label
for how the chain changed since the previous snapshot (near-money PCR up or down, whether the
new OI near the money was put or call writing, whether the put and call walls moved, where spot
sits between the walls). The day's last snapshot gives a second, day-level pattern (changes since
the previous day). Every pattern is stored with what Nifty did afterwards: the day's close
(intraday), the next day (day level), and up to expiry (did spot stay between the walls, how the
move compared with what the ATM straddle priced in). Outcomes fill in on later runs as they happen.

The pattern library then says, for each pattern seen before, how often and how far Nifty went
up or down after it. When the latest snapshot shows a pattern with enough history, the report
names the hedged structure that history points to; with too little history it says so.

Writes data/oc_learning/: pattern_log.csv (every observation with its pattern and outcomes),
pattern_library.csv, latest.json and report.md. Analysis only, not trading advice.
"""
import glob
import json
import math
import os
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

IST = timezone(timedelta(hours=5, minutes=30))
SNAP_DIR = os.path.join("data", "option_chain")
OUT = os.path.join("data", "oc_learning")
NEAR = 0.03                   # "near the money": strikes within 3% of spot
MIN_GAP_MIN = 10              # snapshots closer than this to the previous one are dropped
PCR_STEP = {"intraday": 0.02, "day": 0.05}     # smaller PCR changes count as "flat"
FLOW_STEP = 0.005             # new OI near the money below 0.5% of near OI counts as "quiet"
SEEN_MIN = 10                 # past outcomes a pattern needs before it shows a lean
TRADE_MIN = 20                # ... and before it can point to a structure
# Strong vs weak writers: how far spot is from the writers' break-even (strike +/- their average
# selling price), in % of spot. ~0.45% is about 100 Nifty points, ~0.22% about 50.
STRONG_CUSHION = 0.45
WEAK_CUSHION = 0.22


# ---------- loading ----------

def load_snapshots():
    files = sorted(glob.glob(os.path.join(SNAP_DIR, "*.csv")))
    if not files:
        return pd.DataFrame()
    d = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    d = d[d["expiry_type"].isin(["weekly", "monthly"])]
    d["obs"] = pd.to_datetime(d["nse_time"])
    d["date"] = d["obs"].dt.strftime("%Y-%m-%d")
    # GitHub starts runs at odd times, so two snapshots can be a minute apart: keep the first of
    # any cluster, per expiry.
    keep = []
    for exp, g in d.groupby("expiry"):
        last = None
        for t in sorted(g["obs"].unique()):
            if last is None or (t - last) >= pd.Timedelta(minutes=MIN_GAP_MIN):
                keep.append((exp, t))
                last = t
    return d.merge(pd.DataFrame(keep, columns=["expiry", "obs"]), on=["expiry", "obs"])


# ---------- one chain -> numbers ----------

def max_pain(strikes, ce_oi, pe_oi):
    k = strikes[:, None]
    pain = (ce_oi[None, :] * np.maximum(0, k - strikes[None, :])
            + pe_oi[None, :] * np.maximum(0, strikes[None, :] - k)).sum(axis=1)
    return float(strikes[int(np.argmin(pain))])


def chain_features(g):
    g = g.sort_values("strike")
    spot = float(g["spot"].iloc[0])
    obs = g["obs"].iloc[0]
    expiry = pd.Timestamp(g["expiry"].iloc[0]) + pd.Timedelta(hours=15, minutes=30)
    k = g["strike"].to_numpy(float)
    ce_oi, pe_oi = g["ce_oi"].to_numpy(float), g["pe_oi"].to_numpy(float)
    near = np.abs(k / spot - 1) <= NEAR
    above, below = k >= spot, k <= spot
    atm = g.iloc[int(np.argmin(np.abs(k - spot)))]
    ivs = [v for v in (atm["ce_iv"], atm["pe_iv"]) if v > 0]
    straddle = atm["ce_ltp"] + atm["pe_ltp"] if atm["ce_ltp"] > 0 and atm["pe_ltp"] > 0 else np.nan
    return {
        "obs": obs, "date": g["date"].iloc[0], "expiry": g["expiry"].iloc[0],
        "expiry_type": g["expiry_type"].iloc[0],
        "dte": round(max((expiry - obs).total_seconds() / 86400, 0.0), 2), "spot": spot,
        "pcr": pe_oi.sum() / ce_oi.sum() if ce_oi.sum() else np.nan,
        "pcr_near": pe_oi[near].sum() / ce_oi[near].sum() if ce_oi[near].sum() else np.nan,
        "max_pain": max_pain(k, ce_oi, pe_oi),
        "call_wall": float(k[above][np.argmax(ce_oi[above])]) if above.any() else np.nan,
        "put_wall": float(k[below][np.argmax(pe_oi[below])]) if below.any() else np.nan,
        "implied_move_pct": 100 * straddle / spot,      # ATM straddle ~ expected move to expiry
        "atm_iv": float(np.mean(ivs)) if ivs else np.nan,
        "oi_near": ce_oi[near].sum() + pe_oi[near].sum(),
        # chg_oi is change since yesterday's close
        "ce_chg_near": g.loc[near, "ce_chg_oi"].sum(), "pe_chg_near": g.loc[near, "pe_chg_oi"].sum(),
    }


def build(raw):
    rows = [chain_features(g) for _, g in raw.groupby(["obs", "expiry"])]
    return pd.DataFrame(rows).sort_values(["expiry", "obs"]).reset_index(drop=True)


# ---------- strong vs weak writers ----------

def writer_book(raw):
    """Follows the OI at every strike through the snapshots to estimate, for the OI added while
    we were watching, the average premium it was sold at and where spot was then. OI that grew
    between two snapshots is counted as sold at the later snapshot's price; OI that fell is taken
    out pro rata. OI already open when a contract was first seen has no known price and is left
    out of the strong/weak split (tracked_share says how much is covered).

    Option data can't tell a writer from a buyer: every open contract has both. Following the
    usual reading, new OI is treated as writing. Returns one row per snapshot, expiry, strike
    and side, near the money."""
    rows = []
    for exp, g in raw.sort_values("obs").groupby("expiry"):
        book = {}
        for t, snap in g.groupby("obs", sort=True):
            spot = float(snap["spot"].iloc[0])
            for side in ("ce", "pe"):
                for k, oi, ltp in zip(snap["strike"], snap[f"{side}_oi"], snap[f"{side}_ltp"]):
                    oi, ltp = float(oi), float(ltp)
                    b = book.get((side, k))
                    if b is None:                      # first sight: price unknown
                        book[(side, k)] = b = {"oi": oi, "untracked": oi, "tracked": 0.0,
                                               "prem": 0.0, "spot": 0.0}
                    else:
                        d = oi - b["oi"]
                        if d > 0 and ltp > 0:
                            w = b["tracked"] + d
                            b["prem"] = (b["prem"] * b["tracked"] + ltp * d) / w
                            b["spot"] = (b["spot"] * b["tracked"] + spot * d) / w
                            b["tracked"] = w
                        elif d < 0 and b["oi"] > 0:
                            keep = max(oi, 0) / b["oi"]
                            b["tracked"] *= keep
                            b["untracked"] *= keep
                        b["oi"] = oi
                    if abs(k / spot - 1) > NEAR or b["tracked"] <= 0:
                        continue
                    be = k + b["prem"] if side == "ce" else k - b["prem"]
                    cushion = (be - spot) if side == "ce" else (spot - be)
                    pnl = b["prem"] - ltp
                    c = 100 * cushion / spot
                    strength = ("weak" if c < WEAK_CUSHION else
                                "strong" if c >= STRONG_CUSHION else "medium")
                    rows.append({"obs": t, "expiry": exp, "spot": spot, "side": side, "strike": k,
                                 "oi": oi, "tracked_oi": round(b["tracked"]),
                                 "tracked_share": b["tracked"] / oi if oi else 0.0,
                                 "avg_sell_price": b["prem"], "avg_spot_at_sale": b["spot"],
                                 "ltp": ltp, "break_even": be, "cushion_pts": cushion,
                                 "writer_pnl_pts": pnl, "strength": strength})
    return pd.DataFrame(rows)


def writer_summary(w):
    """Per snapshot and expiry: tracked strong and weak OI on each side, the strongest call and put
    strikes, and a short label for the pattern log."""
    out = []
    for (t, exp), g in w.groupby(["obs", "expiry"]):
        r = {"obs": t, "expiry": exp}
        for side, name in (("ce", "call"), ("pe", "put")):
            x = g[g["side"] == side]
            for st in ("strong", "weak"):
                r[f"{st}_{name}_oi"] = x.loc[x["strength"] == st, "tracked_oi"].sum()
            s = x[x["strength"] == "strong"]
            r[f"strong_{name}_strike"] = float(s.loc[s["tracked_oi"].idxmax(), "strike"]) if len(s) else np.nan
            wk = x[x["strength"] == "weak"]
            r[f"weak_{name}_strike"] = float(wk.loc[wk["tracked_oi"].idxmax(), "strike"]) if len(wk) else np.nan
            tot = x["oi"].sum()
            r[f"{name}_tracked_share"] = x["tracked_oi"].sum() / tot if tot else 0.0
        sc, sp = r["strong_call_oi"], r["strong_put_oi"]
        bal = (sp - sc) / (sp + sc) if sp + sc else 0.0
        stronger = "put writers stronger" if bal > 0.2 else "call writers stronger" if bal < -0.2 else "writers even"
        wc, wp = r["weak_call_oi"], r["weak_put_oi"]
        tracked = g["tracked_oi"].sum()
        if wc + wp < 0.1 * tracked:
            weak = "few weak writers"
        elif wc > 1.5 * wp:
            weak = "weak calls"
        elif wp > 1.5 * wc:
            weak = "weak puts"
        else:
            weak = "weak on both sides"
        r["writers"] = f"{stronger} · {weak}"
        out.append(r)
    return pd.DataFrame(out)


# ---------- patterns ----------

def label_changes(f, layer):
    """Adds the change columns and the pattern label. f is sorted by expiry, obs, and holds one
    layer: every snapshot (intraday) or each day's last snapshot (day)."""
    prev = f.groupby("expiry").shift(1)
    ok = prev["date"].eq(f["date"]) if layer == "intraday" else prev["date"].notna()
    f["d_pcr_near"] = np.where(ok, f["pcr_near"] - prev["pcr_near"], np.nan)
    f["d_put_wall"] = np.where(ok, f["put_wall"] - prev["put_wall"], np.nan)
    f["d_call_wall"] = np.where(ok, f["call_wall"] - prev["call_wall"], np.nan)
    f["d_atm_iv"] = np.where(ok, f["atm_iv"] - prev["atm_iv"], np.nan)
    if layer == "intraday":   # OI written during this half hour
        ce = f["ce_chg_near"] - prev["ce_chg_near"]
        pe = f["pe_chg_near"] - prev["pe_chg_near"]
    else:                     # OI written during the day
        ce, pe = f["ce_chg_near"], f["pe_chg_near"]
    f["new_ce_oi"] = np.where(ok, ce, np.nan)
    f["new_pe_oi"] = np.where(ok, pe, np.nan)

    def pattern(r):
        if pd.isna(r["d_pcr_near"]):
            return ""
        step = PCR_STEP[layer]
        pcr = "PCR up" if r["d_pcr_near"] >= step else "PCR down" if r["d_pcr_near"] <= -step else "PCR flat"
        big = FLOW_STEP * r["oi_near"]
        pw, cw = r["new_pe_oi"] >= big, r["new_ce_oi"] >= big
        pu, cu = r["new_pe_oi"] <= -big, r["new_ce_oi"] <= -big
        flow = ("put and call writing" if pw and cw else "put writing" if pw else "call writing" if cw
                else "unwinding" if pu or cu else "quiet OI")
        up = np.sign(r["d_put_wall"]) + np.sign(r["d_call_wall"])
        walls = "walls up" if up > 0 else "walls down" if up < 0 else "walls same"
        p = (r["spot"] - r["put_wall"]) / (r["call_wall"] - r["put_wall"]) if r["call_wall"] > r["put_wall"] else 0.5
        where = ("below put wall" if p < 0 else "above call wall" if p > 1 else "near put wall" if p < 0.33
                 else "near call wall" if p > 0.67 else "mid walls")
        return " · ".join((pcr, flow, walls, where))

    f["pattern"] = f.apply(pattern, axis=1)
    f["layer"] = layer
    return f


def add_outcomes(f, layer, closes):
    """closes: the day's last spot per date (from the snapshots)."""
    days = list(closes.index)
    if layer == "intraday":
        nxt = f.groupby("expiry").shift(-1)
        f["move_next"] = np.where(nxt["date"].eq(f["date"]), 100 * (nxt["spot"] / f["spot"] - 1), np.nan)
        last_obs = f.groupby(["expiry", "date"])["obs"].transform("max")
        last_spot = f.groupby(["expiry", "date"])["spot"].transform("last")
        f["move_close"] = np.where(f["obs"] < last_obs, 100 * (last_spot / f["spot"] - 1), np.nan)
    else:
        nxt = {d: days[i + 1] for i, d in enumerate(days[:-1])}
        f["move_next"] = [100 * (closes[nxt[d]] / s - 1) if d in nxt else np.nan
                          for d, s in zip(f["date"], f["spot"])]
        f["move_close"] = np.nan
    held, to_exp, ratio = [], [], []
    for _, r in f.iterrows():
        path = closes[(closes.index > r["date"]) & (closes.index <= r["expiry"])]
        if r["expiry"] not in closes.index or path.empty:
            held.append(np.nan), to_exp.append(np.nan), ratio.append(np.nan)
            continue
        mv = 100 * (closes[r["expiry"]] / r["spot"] - 1)
        to_exp.append(mv)
        held.append(float(((path >= r["put_wall"]) & (path <= r["call_wall"])).all()))
        ratio.append(abs(mv) / r["implied_move_pct"] if r["implied_move_pct"] > 0 else np.nan)
    f["move_to_expiry"], f["held_walls"], f["move_vs_implied"] = to_exp, held, ratio
    return f


# ---------- library ----------

def wilson(k, n):
    if n == 0:
        return (np.nan, np.nan)
    p, z = k / n, 1.96
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (c - h, c + h)


def library(log, key="pattern"):
    """key: "pattern" (the chain pattern) or "writers" (the strong/weak writer label)."""
    out = []
    use = log[log[key].fillna("").ne("")]
    for (layer, kind, pat), g in use.groupby(["layer", "expiry_type", key]):
        mv = g["move_close" if layer == "intraday" else "move_next"].dropna()
        mv = mv[mv != 0]
        n, up = len(mv), int((mv > 0).sum())
        lo, hi = wilson(up, n)
        # to-expiry numbers: one observation per contract, so a long expiry isn't counted many times
        e = g.dropna(subset=["held_walls"]).sort_values("obs").groupby("expiry").head(1)
        hlo, _ = wilson(int(e["held_walls"].sum()), len(e))
        if n < SEEN_MIN:
            lean = f"too few ({n}/{SEEN_MIN})"
        elif lo > 0.5:
            lean = "up"
        elif hi < 0.5:
            lean = "down"
        else:
            lean = "no clear direction"
        out.append({
            "group": key, "layer": layer, "expiry_type": kind, "pattern": pat, "seen": len(g), "with_outcome": n,
            "up_share": up / n if n else np.nan, "up_low": lo, "up_high": hi,
            "avg_move": mv.mean() if n else np.nan, "median_move": mv.median() if n else np.nan,
            "worst_down": mv.min() if n else np.nan, "best_up": mv.max() if n else np.nan,
            "expiries_seen": len(e), "held_walls_share": e["held_walls"].mean() if len(e) else np.nan,
            "held_low": hlo,
            "median_move_vs_implied": e["move_vs_implied"].median() if len(e) else np.nan,
            "lean": lean, "last_seen": str(g["obs"].max()),
        })
    return pd.DataFrame(out)


def structure_for(row, lib, key="pattern"):
    """What the history of this pattern points to. Only hedged structures, never naked options."""
    if not isinstance(row[key], str) or row[key] == "":
        return ("No pattern yet (needs an earlier snapshot to compare with)." if key == "pattern"
                else "No writer data yet (needs OI added while being watched).")
    m = lib[(lib["group"] == key) & (lib["layer"] == row["layer"]) & (lib["expiry_type"] == row["expiry_type"])
            & (lib["pattern"] == row[key])] if not lib.empty else lib
    if m.empty:
        return "New pattern, never seen before. Logged; nothing to go on yet."
    m = m.iloc[0]
    n = int(m["with_outcome"])
    seen = (f"Seen {int(m['seen'])} times before"
            + (f"; Nifty was up after it {m['up_share']:.0%} of the time, average {m['avg_move']:+.2f}%." if n else "."))
    if n < TRADE_MIN:
        return f"{seen} Too few outcomes ({n}/{TRADE_MIN}) to trade on."
    premium_rich = m["expiries_seen"] >= 8 and m["median_move_vs_implied"] < 1
    walls_hold = m["expiries_seen"] >= 8 and m["held_low"] >= 0.7
    pw, cw = row["put_wall"], row["call_wall"]
    if m["lean"] == "up":
        s = (f"bull put spread, short put at or below the put wall {pw:.0f}" if premium_rich
             else f"bull call debit spread, ATM to about the call wall {cw:.0f}")
    elif m["lean"] == "down":
        s = (f"bear call spread, short call at or above the call wall {cw:.0f}" if premium_rich
             else f"bear put debit spread, ATM to about the put wall {pw:.0f}")
    elif walls_hold:
        s = f"iron condor, short strikes at the walls {pw:.0f} / {cw:.0f}"
    else:
        return f"{seen} No direction and the walls have not held reliably: no structure."
    return f"{seen} History points to a {s}."


# ---------- report ----------

def pct(x):
    return "" if pd.isna(x) else f"{100 * x:.0f}%"


def write_report(log, lib, read):
    now = datetime.now(IST)
    intra = log[log["layer"] == "intraday"]
    L = ["# Nifty option chain pattern log",
         f"Updated {now:%Y-%m-%d %H:%M} IST. Learns only from live snapshots since 14 Oct 2026. "
         "Analysis only, not trading advice.", "",
         "## Data",
         f"- {intra['obs'].nunique()} snapshots over {intra['date'].nunique()} trading days",
         f"- {int((log['pattern'] != '').sum())} patterns logged; "
         f"{int((lib['group'] == 'pattern').sum()) if not lib.empty else 0} different patterns so far", ""]
    L += [f"## Latest read ({read['as_of']})", "",
          "| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied move | ATM IV |",
          "|---|---|---|---|---|---|---|---|---|"]
    for e in read["expiries"]:
        L.append(f"| {e['expiry']} ({e['type']}) | {e['dte']:.1f} | {e['spot']:.0f} | {e['pcr_near']} | "
                 f"{e['max_pain']:.0f} | {e['put_wall']:.0f} | {e['call_wall']:.0f} | "
                 f"±{e['implied_move_pct']}% ({e['implied_range'][0]}-{e['implied_range'][1]}) | {e['atm_iv'] or ''} |")
    L.append("")
    for e in read["expiries"]:
        for layer, when in (("intraday", "last 30 min"), ("day", "today vs previous day")):
            p = e.get(layer)
            if p:
                L.append(f"- **{e['type'].title()}, {when}**: `{p['pattern'] or '-'}`. {p['verdict']}")
                if p.get("writers"):
                    L.append(f"  - Writers: `{p['writers']}`. {p['writers_verdict']}")
    L.append("")
    for e in read["expiries"]:
        w = e.get("writers")
        if not w or not w["strikes"]:
            continue
        def strike(v):
            return "-" if v is None or pd.isna(v) else f"{v:.0f}"
        L += [f"## Strong vs weak writers, {e['type']} {e['expiry']}", "",
              f"Strongest call writers at {strike(w['strong_call_strike'])}, strongest put writers at "
              f"{strike(w['strong_put_strike'])}; weakest call writers at {strike(w['weak_call_strike'])}, "
              f"weakest put writers at {strike(w['weak_put_strike'])}. Covers {pct(w['call_tracked_share'])} of "
              f"near-money call OI and {pct(w['put_tracked_share'])} of put OI (the rest was open before it was "
              "watched, so its selling price is unknown).", "",
              "| Side | Strike | OI | Of which tracked | Avg sold at | Spot when sold | Now | Break-even | Cushion (pts) | Writer P&L (pts) | Strength |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for x in w["strikes"]:
            if abs(x["strike"] / e["spot"] - 1) > 0.015:
                continue
            L.append(f"| {'Call' if x['side'] == 'ce' else 'Put'} | {x['strike']:.0f} | {x['oi']:.0f} | "
                     f"{x['tracked_oi']:.0f} | {x['avg_sell_price']:.1f} | {x['avg_spot_at_sale']:.0f} | "
                     f"{x['ltp']:.1f} | {x['break_even']:.0f} | {x['cushion_pts']:+.0f} | "
                     f"{x['writer_pnl_pts']:+.1f} | {x['strength']} |")
        L.append("")
    if not lib.empty:
        for layer, title, mv in (("intraday", "30-minute patterns (Nifty move to that day's close)", "to close"),
                                 ("day", "Day patterns (Nifty move next day)", "next day")):
            g = lib[(lib["layer"] == layer) & (lib["group"] == "pattern")].sort_values("seen", ascending=False)
            if g.empty:
                continue
            L += [f"## {title}", "",
                  f"| Expiry | Pattern | Seen | Up after | Avg move {mv} | Range | Walls held to expiry | Lean |",
                  "|---|---|---|---|---|---|---|---|"]
            for _, r in g.iterrows():
                avg = "" if pd.isna(r["avg_move"]) else f"{r['avg_move']:+.2f}%"
                rng = "" if pd.isna(r["worst_down"]) else f"{r['worst_down']:+.2f} to {r['best_up']:+.2f}%"
                held = f"{pct(r['held_walls_share'])} of {int(r['expiries_seen'])}" if r["expiries_seen"] else ""
                L.append(f"| {r['expiry_type']} | {r['pattern']} | {int(r['seen'])} | {pct(r['up_share'])} | "
                         f"{avg} | {rng} | {held} | {r['lean']} |")
            L.append("")
        g = lib[lib["group"] == "writers"].sort_values(["layer", "seen"], ascending=[False, False])
        if not g.empty:
            L += ["## Writer patterns (Nifty move to the close for 30-minute rows, next day for day rows)", "",
                  "| Layer | Expiry | Writers | Seen | Up after | Avg move | Lean |", "|---|---|---|---|---|---|---|"]
            for _, r in g.iterrows():
                avg = "" if pd.isna(r["avg_move"]) else f"{r['avg_move']:+.2f}%"
                L.append(f"| {r['layer']} | {r['expiry_type']} | {r['pattern']} | {int(r['seen'])} | "
                         f"{pct(r['up_share'])} | {avg} | {r['lean']} |")
            L.append("")
    L += ["## How to read this",
          "- A pattern is: near-money PCR change · where new OI near the money went · how the put and call "
          "walls (biggest OI strikes) moved · where spot sits between the walls.",
          f"- A pattern shows a lean only after {SEEN_MIN} outcomes, and only when the 95% range of 'up after' "
          f"sits fully above or below 50%. It points to a structure only after {TRADE_MIN} outcomes.",
          "- Credit spreads and condors are suggested only after 8+ expiries showed the real move smaller than "
          "the straddle priced in (or the walls holding 70%+ of the time); otherwise debit spreads.",
          "- 30-minute patterns from one day move together, so trust a lean more once it has held across "
          "several weeks, not one busy day.",
          "- Roughly: common 30-minute patterns reach 20 outcomes in 3 to 6 weeks, day patterns in 3 to 6 months, "
          "and the walls/expiry numbers need about 5 months of weekly expiries and a year of monthly ones.",
          "- Walls held means every daily close stayed between the walls; an intraday breach that closed back "
          "inside counts as held."]
    with open(os.path.join(OUT, "report.md"), "w") as f:
        f.write("\n".join(L) + "\n")


def clean(x):
    """JSON-safe: NaN -> null, numpy numbers -> plain numbers."""
    if isinstance(x, dict):
        return {k: clean(v) for k, v in x.items()}
    if isinstance(x, list):
        return [clean(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return None if math.isnan(x) else round(float(x), 4)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, pd.Timestamp):
        return str(x)
    return x


def rounded(df):
    return df.assign(**df.select_dtypes("number").round(4))


def main():
    os.makedirs(OUT, exist_ok=True)
    raw = load_snapshots()
    if raw.empty:
        print("no snapshots yet")
        return
    snaps = build(raw)
    wb = writer_book(raw)
    if not wb.empty:
        snaps = snaps.merge(writer_summary(wb), on=["obs", "expiry"], how="left")
    else:
        snaps["writers"] = ""
    closes = snaps.sort_values("obs").groupby("date")["spot"].last()
    intra = add_outcomes(label_changes(snaps.copy(), "intraday"), "intraday", closes)
    day = (snaps.sort_values("obs").groupby(["expiry", "date"]).tail(1)
           .sort_values(["expiry", "obs"]).reset_index(drop=True))
    day = add_outcomes(label_changes(day, "day"), "day", closes)
    log = pd.concat([intra, day], ignore_index=True).sort_values(["obs", "layer", "expiry_type"])
    lib = pd.concat([library(log, "pattern"), library(log, "writers")], ignore_index=True)

    # the weekly and monthly chains are read a few seconds apart, so "latest" is per expiry
    latest = intra.loc[intra.groupby("expiry_type")["obs"].idxmax()].sort_values("expiry")
    read = {"as_of": str(latest["obs"].max()), "expiries": []}
    for _, r in latest.iterrows():
        t = r["obs"]
        before = log[log["obs"] < t]            # judge the latest pattern only by what came before it
        past = pd.concat([library(before, "pattern"), library(before, "writers")], ignore_index=True)
        im = r["implied_move_pct"]
        e = {"expiry": r["expiry"], "type": r["expiry_type"], "dte": r["dte"], "spot": r["spot"],
             "pcr_near": round(r["pcr_near"], 3), "max_pain": r["max_pain"], "put_wall": r["put_wall"],
             "call_wall": r["call_wall"], "implied_move_pct": round(im, 2),
             "implied_range": [round(r["spot"] * (1 - im / 100)), round(r["spot"] * (1 + im / 100))],
             "atm_iv": None if pd.isna(r["atm_iv"]) else round(r["atm_iv"], 2)}
        for layer in ("intraday", "day"):
            x = log[(log["layer"] == layer) & (log["expiry"] == r["expiry"]) & (log["obs"] == t)]
            if len(x):
                e[layer] = {"pattern": x.iloc[0]["pattern"], "verdict": structure_for(x.iloc[0], past),
                            "writers": x.iloc[0]["writers"] if isinstance(x.iloc[0]["writers"], str) else "",
                            "writers_verdict": structure_for(x.iloc[0], past, "writers")}
        if not wb.empty:
            w = wb[(wb["obs"] == t) & (wb["expiry"] == r["expiry"])].sort_values(["side", "strike"])
            e["writers"] = {
                "label": r.get("writers", ""),
                "strong_call_strike": r.get("strong_call_strike"), "strong_put_strike": r.get("strong_put_strike"),
                "weak_call_strike": r.get("weak_call_strike"), "weak_put_strike": r.get("weak_put_strike"),
                "strong_call_oi": r.get("strong_call_oi"), "weak_call_oi": r.get("weak_call_oi"),
                "strong_put_oi": r.get("strong_put_oi"), "weak_put_oi": r.get("weak_put_oi"),
                "call_tracked_share": r.get("call_tracked_share"), "put_tracked_share": r.get("put_tracked_share"),
                "strikes": [{k: (round(v, 2) if isinstance(v, float) else v) for k, v in row.items()
                             if k in ("side", "strike", "oi", "tracked_oi", "tracked_share", "avg_sell_price",
                                      "avg_spot_at_sale", "ltp", "break_even", "cushion_pts",
                                      "writer_pnl_pts", "strength")}
                            for row in w.to_dict("records")]}
        read["expiries"].append(e)

    cols = ["obs", "layer", "expiry", "expiry_type", "dte", "spot", "pattern", "writers", "pcr", "pcr_near",
            "d_pcr_near", "new_pe_oi", "new_ce_oi", "max_pain", "put_wall", "call_wall", "d_put_wall",
            "d_call_wall", "strong_call_strike", "strong_put_strike", "weak_call_strike", "weak_put_strike",
            "strong_call_oi", "weak_call_oi", "strong_put_oi", "weak_put_oi", "atm_iv", "d_atm_iv",
            "implied_move_pct", "move_next", "move_close", "move_to_expiry", "held_walls", "move_vs_implied"]
    rounded(log.reindex(columns=cols)).to_csv(os.path.join(OUT, "pattern_log.csv"), index=False)
    if not wb.empty:
        # one file per day (strikes within 1.5% of spot), so past days never change
        os.makedirs(os.path.join(OUT, "writers"), exist_ok=True)
        near = wb[(wb["strike"] / wb["spot"] - 1).abs() <= 0.015]
        for d, g in near.groupby(near["obs"].dt.strftime("%Y-%m-%d")):
            rounded(g).to_csv(os.path.join(OUT, "writers", f"{d}.csv"), index=False)
    if not lib.empty:
        rounded(lib).to_csv(os.path.join(OUT, "pattern_library.csv"), index=False)
    with open(os.path.join(OUT, "latest.json"), "w") as f:
        json.dump(clean(read), f, indent=1)
    write_report(log, lib, read)
    print(open(os.path.join(OUT, "report.md")).read())


if __name__ == "__main__":
    main()
