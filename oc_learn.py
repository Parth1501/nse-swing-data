"""
Learning how Nifty moves after changes in its option chain (weekly and monthly expiry).

Reads two kinds of data, never changes them:
  data/option_chain_eod/*.csv   one end-of-day chain per trading day (oc_history.py, NSE bhavcopy)
  data/option_chain/*.csv       30-minute intraday snapshots (option_chain.py)

For every observation (a day, or a snapshot) and expiry it measures the chain (PCR, max pain,
call and put walls, ATM straddle and the move it implies, ATM IV, put-call skew, where new OI was
written near the money), how each changed since the previous observation of the same expiry, and
what Nifty did afterwards (next day / next snapshot, to expiry, whether it stayed between the
walls, how the real move compared with the move the straddle priced in).

Then it tests a fixed list of ideas (HYPOTHESES below) and says, for each, whether there is
enough data yet and whether an edge shows up. An idea only counts as an edge when it has enough
observations, is statistically clear, and points the same way in the first and second half of
the history (so one lucky stretch can't make it). Only edges feed the "today's read" section,
which maps them to hedged structures (spreads, condors), never naked options.

Writes data/oc_learning/: daily_features.csv, intraday_features.csv, hypotheses.csv (this run),
hypotheses_history.csv (one block per run, so the learning can be followed over time),
latest.json and report.md. Analysis only, not trading advice.
"""
import glob
import json
import math
import os
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

IST = timezone(timedelta(hours=5, minutes=30))
EOD_DIR = os.path.join("data", "option_chain_eod")
SNAP_DIR = os.path.join("data", "option_chain")
OUT = os.path.join("data", "oc_learning")
RATE = 0.065                  # risk-free rate for Black-Scholes IV on end-of-day prices
NEAR = 0.03                   # "near the money" band for OI flow: +-3% of spot
PCR_NEAR = 0.05               # band for near-money PCR
MIN_GAP_MIN = 10              # intraday snapshots closer than this to the previous one are dropped
SIDE = ("ltp", "oi", "chg_oi", "volume")


# ---------- loading ----------

def load_eod():
    files = sorted(glob.glob(os.path.join(EOD_DIR, "*.csv")))
    if not files:
        return pd.DataFrame()
    d = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    d["obs"] = pd.to_datetime(d["date"]) + pd.Timedelta(hours=15, minutes=30)
    return d


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
    for _, g in d.groupby("expiry"):
        last = None
        for t in sorted(g["obs"].unique()):
            if last is None or (t - last) >= pd.Timedelta(minutes=MIN_GAP_MIN):
                keep.append((g["expiry"].iloc[0], t))
                last = t
    k = pd.DataFrame(keep, columns=["expiry", "obs"])
    return d.merge(k, on=["expiry", "obs"])


# ---------- option maths ----------

def _ncdf(x):
    return 0.5 * (1 + np.vectorize(math.erf)(x / math.sqrt(2)))


def bs_price(S, K, T, sigma, call):
    d1 = (np.log(S / K) + (RATE + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if call:
        return S * _ncdf(d1) - K * math.exp(-RATE * T) * _ncdf(d2)
    return K * math.exp(-RATE * T) * _ncdf(-d2) - S * _ncdf(-d1)


def implied_vol(price, S, K, T, call):
    """IV in % by bisection; NaN when the price says nothing (zero, below intrinsic)."""
    if not (price > 0 and T > 0):
        return np.nan
    intrinsic = max(0.0, S - K * math.exp(-RATE * T)) if call else max(0.0, K * math.exp(-RATE * T) - S)
    if price <= intrinsic + 0.05:
        return np.nan
    lo, hi = 0.01, 3.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if float(bs_price(S, K, T, mid, call)) > price:
            hi = mid
        else:
            lo = mid
    return round(100 * (lo + hi) / 2, 2)


# ---------- one chain -> numbers ----------

def max_pain(strikes, ce_oi, pe_oi):
    k = strikes[:, None]
    pain = (ce_oi[None, :] * np.maximum(0, k - strikes[None, :])
            + pe_oi[None, :] * np.maximum(0, strikes[None, :] - k)).sum(axis=1)
    return float(strikes[int(np.argmin(pain))])


def chain_features(g, has_nse_iv):
    g = g.sort_values("strike")
    spot = float(g["spot"].iloc[0])
    obs = g["obs"].iloc[0]
    expiry = pd.Timestamp(g["expiry"].iloc[0]) + pd.Timedelta(hours=15, minutes=30)
    dte = max((expiry - obs).total_seconds() / 86400, 0.0)
    T = max(dte, 0.04) / 365
    k = g["strike"].to_numpy(float)
    ce_oi, pe_oi = g["ce_oi"].to_numpy(float), g["pe_oi"].to_numpy(float)
    near = (np.abs(k / spot - 1) <= NEAR)
    pnear = (np.abs(k / spot - 1) <= PCR_NEAR)
    above, below = k >= spot, k <= spot
    atm_i = int(np.argmin(np.abs(k - spot)))
    atm = g.iloc[atm_i]
    straddle = float(atm["ce_ltp"]) + float(atm["pe_ltp"]) if atm["ce_ltp"] > 0 and atm["pe_ltp"] > 0 else np.nan

    def side_iv(target, call):
        i = int(np.argmin(np.abs(k - target)))
        r = g.iloc[i]
        if has_nse_iv:
            v = float(r["ce_iv"] if call else r["pe_iv"])
            return v if v > 0 else np.nan
        return implied_vol(float(r["ce_ltp"] if call else r["pe_ltp"]), spot, float(r["strike"]), T, call)

    if dte >= 0.5:
        atm_iv = np.nanmean([side_iv(spot, True), side_iv(spot, False)])
        skew = side_iv(spot * 0.97, False) - side_iv(spot * 1.03, True)
    else:                                   # expiry day: option prices are mostly intrinsic
        atm_iv = skew = np.nan
    ce_flow, pe_flow = g.loc[near, "ce_chg_oi"].sum(), g.loc[near, "pe_chg_oi"].sum()
    tot = abs(ce_flow) + abs(pe_flow)
    return {
        "obs": obs, "date": g["date"].iloc[0], "expiry": g["expiry"].iloc[0],
        "expiry_type": g["expiry_type"].iloc[0], "dte": round(dte, 2), "spot": spot,
        "pcr": pe_oi.sum() / ce_oi.sum() if ce_oi.sum() else np.nan,
        "pcr_near": pe_oi[pnear].sum() / ce_oi[pnear].sum() if ce_oi[pnear].sum() else np.nan,
        "max_pain": max_pain(k, ce_oi, pe_oi),
        "call_wall": float(k[above][np.argmax(ce_oi[above])]) if above.any() else np.nan,
        "put_wall": float(k[below][np.argmax(pe_oi[below])]) if below.any() else np.nan,
        "straddle": straddle,
        "implied_move_pct": 100 * straddle / spot,
        "atm_iv": atm_iv, "skew": skew,
        # where today's (or this session's) new OI sits near the money; >0 = more put writing
        "ce_flow_near": ce_flow, "pe_flow_near": pe_flow,
        "flow_bias": (pe_flow - ce_flow) / tot if tot else 0.0,
    }


def build(raw, has_nse_iv):
    if raw.empty:
        return pd.DataFrame()
    rows = [chain_features(g, has_nse_iv) for _, g in raw.groupby(["obs", "expiry"])]
    f = pd.DataFrame(rows).sort_values(["expiry_type", "obs"]).reset_index(drop=True)
    f["pos_in_walls"] = (f["spot"] - f["put_wall"]) / (f["call_wall"] - f["put_wall"])
    f["mp_gap_pct"] = 100 * (f["max_pain"] / f["spot"] - 1)
    # changes since the previous observation of the same contract
    f = f.sort_values(["expiry", "obs"])
    prev = f.groupby("expiry").shift(1)
    same_day = prev["date"] == f["date"]
    for c in ("pcr", "pcr_near", "atm_iv", "skew"):
        f[f"d_{c}"] = f[c] - prev[c]
    f["d_call_wall"] = f["call_wall"] - prev["call_wall"]
    f["d_put_wall"] = f["put_wall"] - prev["put_wall"]
    f["d_max_pain"] = f["max_pain"] - prev["max_pain"]
    # intraday: chg_oi is change since yesterday's close, so the flow during the interval is
    # the difference between two snapshots of the same day
    f["d_flow"] = np.where(same_day, (f["pe_flow_near"] - prev["pe_flow_near"])
                           - (f["ce_flow_near"] - prev["ce_flow_near"]), np.nan)
    f["prev_same_day"] = same_day
    return f.sort_values(["expiry_type", "obs"]).reset_index(drop=True)


# ---------- what happened next ----------

def add_outcomes_daily(f):
    spot = f.groupby("date")["spot"].first().sort_index()
    days = list(spot.index)
    idx = {d: i for i, d in enumerate(days)}

    def fwd(d, n):
        i = idx[d] + n
        return 100 * (spot.iloc[i] / spot[d] - 1) if i < len(days) else np.nan

    f["ret_1d"] = [fwd(d, 1) for d in f["date"]]
    f["ret_3d"] = [fwd(d, 3) for d in f["date"]]
    out = {"ret_exp": [], "held_walls": [], "move_ratio": [], "pinned": []}
    for _, r in f.iterrows():
        path = spot[(spot.index > r["date"]) & (spot.index <= r["expiry"])]
        if r["expiry"] not in spot.index or path.empty:
            for v in out.values():
                v.append(np.nan)
            continue
        end = spot[r["expiry"]]
        ret = 100 * (end / r["spot"] - 1)
        out["ret_exp"].append(ret)
        out["held_walls"].append(float(((path >= r["put_wall"]) & (path <= r["call_wall"])).all()))
        out["move_ratio"].append(abs(ret) / r["implied_move_pct"] if r["implied_move_pct"] > 0 else np.nan)
        out["pinned"].append(float(abs(end - r["max_pain"]) < abs(r["spot"] - r["max_pain"])))
    for k, v in out.items():
        f[k] = v
    return f


def add_outcomes_intraday(f):
    f = f.sort_values(["expiry", "obs"])
    nxt = f.groupby("expiry").shift(-1)
    f["ret_next"] = np.where(nxt["date"] == f["date"], 100 * (nxt["spot"] / f["spot"] - 1), np.nan)
    last = f.groupby(["expiry", "date"])["spot"].transform("last")
    is_last = f.groupby(["expiry", "date"])["obs"].transform("max") == f["obs"]
    f["ret_close"] = np.where(is_last, np.nan, 100 * (last / f["spot"] - 1))
    return f.sort_values(["expiry_type", "obs"]).reset_index(drop=True)


# ---------- hypotheses ----------

def wilson(k, n):
    if n == 0:
        return (np.nan, np.nan)
    p, z = k / n, 1.96
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (c - h, c + h)


def two_prop_p(k1, n1, k2, n2):
    if min(n1, n2) == 0:
        return np.nan
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return np.nan
    z = abs(k1 / n1 - k2 / n2) / se
    return math.erfc(z / math.sqrt(2))


def direction_test(df, signal, label, min_n):
    """signal: +1 (expect up), -1 (expect down), 0/NaN (no call). Compares how often Nifty rose
    after +1 versus after -1. Edge = enough data, p < 0.05, a gap of 10+ points, and the same
    sign in both halves of the history."""
    d = df[[signal, label]].dropna()
    d = d[d[signal] != 0]
    d = d[d[label] != 0]

    def split(x):
        up = x[label] > 0
        b, s = x[signal] > 0, x[signal] < 0
        return int(b.sum()), int((up & b).sum()), int(s.sum()), int((up & s).sum())

    nb, kb, ns, ks = split(d)
    res = {"n": nb + ns, "n_bull": nb, "n_bear": ns,
           "up_after_bull": kb / nb if nb else np.nan, "up_after_bear": ks / ns if ns else np.nan}
    res["gap"] = res["up_after_bull"] - res["up_after_bear"]
    res["p_value"] = two_prop_p(kb, nb, ks, ns)
    half = len(d) // 2
    signs = []
    for part in (d.iloc[:half], d.iloc[half:]):
        b1, k1, s1, k2 = split(part)
        signs.append(np.sign((k1 / b1 if b1 else 0.5) - (k2 / s1 if s1 else 0.5)))
    res["halves_agree"] = bool(signs[0] == signs[1] != 0)
    if min(nb, ns) < min_n:
        res["status"] = f"collecting ({min(nb, ns)}/{min_n} on the smaller side)"
    elif res["p_value"] < 0.05 and abs(res["gap"]) >= 0.10 and res["halves_agree"]:
        res["status"] = "edge (works)" if res["gap"] > 0 else "edge (works in reverse)"
    else:
        res["status"] = "no edge so far"
    return res


def rate_test(df, label, min_n, good_above):
    """How often a yes/no outcome happens. 'Usable' when the 95% lower bound clears good_above."""
    x = df[label].dropna()
    n, k = len(x), int(x.sum())
    lo, hi = wilson(k, n)
    res = {"n": n, "rate": k / n if n else np.nan, "ci_low": lo, "ci_high": hi}
    if n < min_n:
        res["status"] = f"collecting ({n}/{min_n})"
    elif lo >= good_above:
        res["status"] = f"usable (reliably above {good_above:.0%})"
    else:
        res["status"] = "not reliable"
    return res


def first_obs_per_expiry(f, kind):
    """One observation per contract (the first day it is in the data as `kind`), so the
    to-expiry outcomes don't count the same week many times."""
    g = f[(f["expiry_type"] == kind)]
    return g.sort_values("obs").groupby("expiry").head(1)


def signals(f):
    f = f.copy()
    f["sig_pcr_rise"] = np.sign(f["d_pcr_near"])
    f["sig_flow"] = np.sign(f["flow_bias"].where(f["flow_bias"].abs() >= 0.2, 0))
    walls = np.sign(f["d_put_wall"].fillna(0)) + np.sign(f["d_call_wall"].fillna(0))
    f["sig_walls_shift"] = np.sign(walls)
    f["sig_max_pain"] = np.sign(f["mp_gap_pct"].where(f["mp_gap_pct"].abs() >= 0.5, 0))
    f["sig_skew_fall"] = -np.sign(f["d_skew"])
    f["sig_iv_fall"] = -np.sign(f["d_atm_iv"])
    if "d_flow" in f:
        f["sig_flow_now"] = np.sign(f["d_flow"])
    return f


DAILY_IDEAS = [
    ("pcr_rise", "sig_pcr_rise", "Near-money PCR rose since yesterday, so Nifty rises next day"),
    ("flow", "sig_flow", "Today's new OI near the money is mostly put writing, so Nifty rises next day"),
    ("walls_shift", "sig_walls_shift", "Put and call walls moved up, so Nifty rises next day"),
    ("max_pain_pull", "sig_max_pain", "Max pain is above spot (0.5%+), so Nifty rises next day"),
    ("skew_fall", "sig_skew_fall", "Put skew eased, so Nifty rises next day"),
    ("iv_fall", "sig_iv_fall", "ATM IV fell, so Nifty rises next day"),
]
INTRADAY_IDEAS = [
    ("pcr_rise", "sig_pcr_rise", "Near-money PCR rose in the last 30 min, so Nifty rises to the close"),
    ("flow_now", "sig_flow_now", "The last 30 min added more put than call OI near the money, so Nifty rises to the close"),
    ("walls_shift", "sig_walls_shift", "Walls moved up in the last 30 min, so Nifty rises to the close"),
]


def run_hypotheses(daily, intra):
    out = []
    if not daily.empty:
        sd = signals(daily)
        for kind in ("weekly", "monthly"):
            g = sd[sd["expiry_type"] == kind]
            for key, sig, text in DAILY_IDEAS:
                r = direction_test(g, sig, "ret_1d", 30)
                out.append({"scope": f"daily/{kind}", "id": key, "idea": text, **r})
            first = first_obs_per_expiry(daily, kind)
            min_n = 20 if kind == "weekly" else 12
            r = rate_test(first, "held_walls", min_n, 0.70)
            out.append({"scope": f"to-expiry/{kind}", "id": "walls_hold",
                        "idea": "Nifty closes every day between the put and call walls until expiry", **r})
            r = rate_test(first.assign(seller=(first["move_ratio"] < 1).where(first["move_ratio"].notna())),
                          "seller", min_n, 0.55)
            r["median_ratio"] = float(first["move_ratio"].median()) if first["move_ratio"].notna().any() else np.nan
            out.append({"scope": f"to-expiry/{kind}", "id": "move_lt_implied",
                        "idea": "The move to expiry is smaller than the ATM straddle priced in", **r})
            r = rate_test(first, "pinned", min_n, 0.60)
            out.append({"scope": f"to-expiry/{kind}", "id": "max_pain_pin",
                        "idea": "Nifty ends nearer max pain at expiry than when the contract started", **r})
    if not intra.empty:
        si = signals(intra)
        si = si[si["prev_same_day"]]
        for kind in ("weekly", "monthly"):
            g = si[si["expiry_type"] == kind]
            for key, sig, text in INTRADAY_IDEAS:
                # 30-minute observations from one day are not independent, so ask for more
                r = direction_test(g, sig, "ret_close", 100)
                out.append({"scope": f"intraday/{kind}", "id": key, "idea": text, **r})
    return pd.DataFrame(out)


# ---------- today's read ----------

def todays_read(daily, intra, hyp):
    src = intra if not intra.empty else daily
    if src.empty:
        return {}
    last_t = src["obs"].max()
    now = signals(src[src["obs"] == last_t])
    read = {"as_of": str(last_t), "source": "intraday snapshot" if src is intra else "end of day", "expiries": []}
    edges = hyp[hyp["status"].str.startswith("edge")] if not hyp.empty else hyp
    # each learned edge is checked on the latest observation of its own kind: next-day ideas on
    # the latest end-of-day chain, intraday ideas on the latest snapshot
    latest = {}
    for scope, f in (("daily", daily), ("intraday", intra)):
        if not f.empty:
            latest[scope] = signals(f[f["obs"] == f["obs"].max()]).set_index("expiry_type")
    sig_of = {"pcr_rise": "sig_pcr_rise", "flow": "sig_flow", "flow_now": "sig_flow_now",
              "walls_shift": "sig_walls_shift", "max_pain_pull": "sig_max_pain",
              "skew_fall": "sig_skew_fall", "iv_fall": "sig_iv_fall"}
    for _, r in now.iterrows():
        kind = r["expiry_type"]
        votes, used = 0, []
        for _, h in edges.iterrows():
            scope, hkind = h["scope"].split("/")
            if hkind != kind or scope not in latest or kind not in latest[scope].index:
                continue
            v = latest[scope].loc[kind].get(sig_of[h["id"]], np.nan)
            if pd.notna(v) and v != 0:
                v = v if h["gap"] > 0 else -v
                votes += v
                used.append(f"{scope} {h['id']} says {'up' if v > 0 else 'down'}")
        bias = "up" if votes > 0 else "down" if votes < 0 else "neutral"

        def status(i):
            x = hyp[(hyp["scope"] == f"to-expiry/{kind}") & (hyp["id"] == i)] if not hyp.empty else hyp
            return x["status"].iloc[0] if len(x) else "no data"

        sellers = status("move_lt_implied").startswith("usable")
        walls = status("walls_hold").startswith("usable")
        spot, im = r["spot"], r["implied_move_pct"]
        lo, hi = spot * (1 - im / 100), spot * (1 + im / 100)
        if not used and not sellers and not walls:
            idea = ("Nothing learned yet is strong enough to lean on, so no structure is favoured. "
                    "Any trade now is a guess; if you trade anyway keep it a defined-risk spread.")
        elif sellers:
            if bias == "up":
                idea = f"Learned bias up and premium has tended to be overpriced: bull put spread, short put at or below the put wall ({r['put_wall']:.0f})."
            elif bias == "down":
                idea = f"Learned bias down and premium has tended to be overpriced: bear call spread, short call at or above the call wall ({r['call_wall']:.0f})."
            else:
                anchor = f"walls {r['put_wall']:.0f} / {r['call_wall']:.0f}" if walls else f"implied range {lo:.0f} / {hi:.0f}"
                idea = f"No direction, premium has tended to be overpriced: iron condor with short strikes at the {anchor}."
        else:
            if bias == "up":
                idea = "Learned bias up, premium not overpriced: bull call debit spread, ATM to about the call wall."
            elif bias == "down":
                idea = "Learned bias down, premium not overpriced: bear put debit spread, ATM to about the put wall."
            else:
                idea = "No direction and no premium edge: stand aside."
        read["expiries"].append({
            "expiry": r["expiry"], "type": kind, "dte": r["dte"], "spot": spot,
            "pcr": round(r["pcr"], 3), "pcr_near": round(r["pcr_near"], 3), "max_pain": r["max_pain"],
            "put_wall": r["put_wall"], "call_wall": r["call_wall"],
            "implied_move_pct": round(im, 2), "implied_range": [round(lo), round(hi)],
            "atm_iv": None if pd.isna(r["atm_iv"]) else round(r["atm_iv"], 2),
            "learned_bias": bias, "signals_used": used, "structure_idea": idea})
    return read


# ---------- report ----------

def pct(x):
    return "" if pd.isna(x) else f"{100 * x:.0f}%"


def write_report(daily, intra, hyp, read):
    now = datetime.now(IST)
    L = [f"# Nifty option chain: what has been learned so far",
         f"Updated {now:%Y-%m-%d %H:%M} IST. Analysis only, not trading advice.", ""]
    nd = daily["date"].nunique() if not daily.empty else 0
    ni = intra["obs"].nunique() if not intra.empty else 0
    ndays_i = intra["date"].nunique() if not intra.empty else 0
    L += ["## Data", f"- End of day history: {nd} trading days"
          + (f" ({daily['date'].min()} to {daily['date'].max()})" if nd else ""),
          f"- Intraday snapshots: {ni} kept, over {ndays_i} days", ""]
    if read:
        L += [f"## Today's read ({read['source']}, {read['as_of']})", "",
              "| Expiry | Days left | Spot | PCR near | Max pain | Put wall | Call wall | Implied range | ATM IV | Learned bias |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for e in read["expiries"]:
            L.append(f"| {e['expiry']} ({e['type']}) | {e['dte']:.1f} | {e['spot']:.0f} | {e['pcr_near']} | "
                     f"{e['max_pain']:.0f} | {e['put_wall']:.0f} | {e['call_wall']:.0f} | "
                     f"{e['implied_range'][0]}-{e['implied_range'][1]} | {e['atm_iv'] or ''} | {e['learned_bias']} |")
        L.append("")
        for e in read["expiries"]:
            L.append(f"- **{e['type'].title()}**: {e['structure_idea']}"
                     + (f" (from {', '.join(e['signals_used'])})" if e["signals_used"] else ""))
        L.append("")
    if not hyp.empty:
        L += ["## Ideas being tested",
              "An idea is an edge only with enough data, p < 0.05, a 10+ point gap and the same "
              "direction in both halves of the history.", ""]
        for scope, g in hyp.groupby("scope", sort=False):
            L.append(f"### {scope}")
            if scope.startswith("to-expiry"):
                L += ["| Idea | n | How often | 95% range | Status |", "|---|---|---|---|---|"]
                for _, h in g.iterrows():
                    extra = f" (median real/implied {h['median_ratio']:.2f})" if pd.notna(h.get("median_ratio", np.nan)) else ""
                    L.append(f"| {h['idea']}{extra} | {h['n']} | {pct(h['rate'])} | "
                             f"{pct(h['ci_low'])}-{pct(h['ci_high'])} | {h['status']} |")
            else:
                L += ["| Idea | n | Up after signal | Up after opposite | p | Status |", "|---|---|---|---|---|---|"]
                for _, h in g.iterrows():
                    p = "" if pd.isna(h["p_value"]) else f"{h['p_value']:.3f}"
                    L.append(f"| {h['idea']} | {h['n']} | {pct(h['up_after_bull'])} | "
                             f"{pct(h['up_after_bear'])} | {p} | {h['status']} |")
            L.append("")
    L += ["## How much data is enough",
          "- Next-day ideas: at least 30 days on each side of the signal; weekly and monthly are tested separately.",
          "- To-expiry ideas count one observation per expiry: 20 weekly expiries (about 5 months) and 12 monthly "
          "expiries (a year). End of day history from Nov 2024 covers most of that from the start.",
          "- Intraday ideas: 100 snapshots on each side, because snapshots from one day move together. "
          "That is roughly 4 to 6 weeks of 30-minute data.",
          "- Testing many ideas means about one in twenty can look like an edge by luck; the both-halves check "
          "and watching an edge survive new data over the next weeks are the guard against that.",
          "- End of day walls-held uses daily closes only, so an intraday breach that closes back inside counts as held."]
    with open(os.path.join(OUT, "report.md"), "w") as f:
        f.write("\n".join(L) + "\n")


def rnd(df):
    return df.assign(**df.select_dtypes("number").round(4))


def main():
    os.makedirs(OUT, exist_ok=True)
    eod, snaps = load_eod(), load_snapshots()
    daily = add_outcomes_daily(build(eod, has_nse_iv=False)) if not eod.empty else pd.DataFrame()
    intra = add_outcomes_intraday(build(snaps, has_nse_iv=True)) if not snaps.empty else pd.DataFrame()
    hyp = run_hypotheses(daily, intra)
    read = todays_read(daily, intra, hyp)
    if not daily.empty:
        rnd(daily).to_csv(os.path.join(OUT, "daily_features.csv"), index=False)
    if not intra.empty:
        rnd(intra).to_csv(os.path.join(OUT, "intraday_features.csv"), index=False)
    if not hyp.empty:
        rnd(hyp).to_csv(os.path.join(OUT, "hypotheses.csv"), index=False)
        hist = os.path.join(OUT, "hypotheses_history.csv")
        h = hyp[["scope", "id", "n", "status"]].assign(run=f"{datetime.now(IST):%Y-%m-%d}")
        if os.path.exists(hist):
            old = pd.read_csv(hist)
            h = pd.concat([old[old["run"] != h["run"].iloc[0]], h], ignore_index=True)
        h.to_csv(hist, index=False)
    with open(os.path.join(OUT, "latest.json"), "w") as f:
        json.dump(read, f, indent=1, default=str)
    write_report(daily, intra, hyp, read)
    print(open(os.path.join(OUT, "report.md")).read())


if __name__ == "__main__":
    main()
