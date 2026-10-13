"""
Feedback for the evening trade review (runs on GitHub Actions after scan_data.py).

The tracker (data/picks_log.csv) says what happened to every pick, but not what the setup
looked like when it was listed. This script:
  1. keeps the listing-day setup details of every pick in data/pick_features.csv
     (score, patterns, entry style, volume, room, relative strength, warnings ...), taken
     from that day's data/latest.csv, so they survive the next day's overwrite;
  2. joins them to the tracker results and compares groups of picks (by entry style, rank,
     score, each pattern, warning, sector tag ...): how often they fill, how often they reach
     T1, how deep they dip, how fast T1 comes;
  3. writes data/feedback.json: today's events with their setup, the group table, and
     "signals" where a group does clearly better or worse than all picks.

Nothing here changes the scan or the rules. The evening review reads feedback.json, explains
the day's results and proposes rule changes to the user; the user decides.
Results are simulated from daily prices, like the tracker.
"""
import json
import os
import subprocess
import sys
from io import StringIO

import pandas as pd

DATA = "data"
PICKS = os.path.join(DATA, "picks_log.csv")
LATEST = os.path.join(DATA, "latest.csv")
META = os.path.join(DATA, "meta.json")
FEATURES = os.path.join(DATA, "pick_features.csv")
OUT = os.path.join(DATA, "feedback.json")

# Listing-day columns kept for each pick (any that the scan stops writing are simply skipped)
FEATURE_COLS = [
    "score", "setups", "entry_style", "zone_status", "deep_pullback", "drop_from_20d_high_pct",
    "close", "support", "resistance", "room_pct", "pat_A_uptrend", "pat_B_base_breakout",
    "pat_C_pullback", "pat_D_retest", "pat_E_candle", "pat_F_room", "pat_G_rel_strength",
    "vol_ok", "smc_sweep", "smc_order_block", "smc_fvg", "smc_choch", "vol_ratio_today",
    "trigger_vol_ratio", "candle", "ret_1m", "ret_3m", "rs_3m_vs_nifty", "pct_below_high52",
    "base_days", "base_range_pct", "warning", "n_flags", "price_band", "avg_value20_cr",
    "segment", "in_midcap150", "sector_tag", "support_kind",
]

CLOSED = ["Full win (T2)", "Partial win (T1)", "Failed"]
MIN_GROUP = 8          # a group needs this many decided trades before it can raise a signal
GAP_PTS = 20           # T1-rate or fill-rate gap (percentage points) that counts as a signal
DIP_GAP_PTS = 2.0      # average worst dip this much deeper than all picks counts as a signal


def r2(x):
    return None if x is None or pd.isna(x) else round(float(x), 2)


def snapshot(latest, data_date, picks):
    """Listing-day features of the picks listed on data_date, from that day's latest.csv."""
    syms = picks.loc[picks["list_date"] == data_date, "symbol"]
    cols = ["symbol"] + [c for c in FEATURE_COLS if c in latest.columns]
    snap = latest.loc[latest["symbol"].isin(syms), cols].copy()
    snap.insert(0, "list_date", data_date)
    return snap


def backfill(picks):
    """One-off: rebuild features for past list dates from the git history of latest.csv.
    For each list date, the newest commit whose meta.json carries that data_date is used."""
    log = subprocess.run(["git", "log", "--format=%H", "--", LATEST],
                         capture_output=True, text=True, check=True).stdout.split()
    frames, done = [], set()
    wanted = set(picks["list_date"])
    for sha in log:                                           # newest first
        try:
            meta = json.loads(subprocess.run(["git", "show", f"{sha}:{META}"], capture_output=True,
                                             text=True, check=True).stdout)
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            continue
        d = meta.get("data_date")
        if d not in wanted or d in done:
            continue
        csv = subprocess.run(["git", "show", f"{sha}:{LATEST}"], capture_output=True,
                             text=True, check=True).stdout
        frames.append(snapshot(pd.read_csv(StringIO(csv)), d, picks))
        done.add(d)
    print(f"backfill: found {sorted(done)}; missing {sorted(wanted - done)}")
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def update_features(picks, latest, data_date, rebuild=False):
    old = pd.read_csv(FEATURES, dtype={"list_date": str}) if os.path.exists(FEATURES) and not rebuild \
        else pd.DataFrame(columns=["list_date", "symbol"])
    new = backfill(picks) if rebuild else snapshot(latest, data_date, picks)
    if not new.empty:                                         # a re-run of the same day replaces it
        key = set(zip(new["list_date"], new["symbol"]))
        old = old[[k not in key for k in zip(old["list_date"], old["symbol"])]]
    feats = pd.concat([old, new], ignore_index=True)
    feats = feats.sort_values(["list_date", "symbol"], ascending=[False, True])
    feats.to_csv(FEATURES, index=False, encoding="utf-8")
    return feats


def bucket(s, edges, labels):
    return pd.cut(pd.to_numeric(s, errors="coerce"), edges, labels=labels).astype(object)


def add_groups(df):
    """Grouping columns used for the comparison table."""
    g = pd.DataFrame(index=df.index)
    g["entry style"] = df["entry_style"]
    g["rank"] = bucket(df["rank"], [0, 3, 6, 99], ["1-3", "4-6", "7-10"])
    if "score" in df:
        g["score"] = bucket(df["score"], [-99, 7, 9, 99], ["7 or less", "8-9", "10+"])
    g["warning"] = df["warning_at_listing"].fillna("").astype(str).replace("", "none")
    g["sector tag"] = df["sector_tag"]
    g["segment"] = df["segment"]
    for col, name in [("pat_A_uptrend", "A uptrend"), ("pat_B_base_breakout", "B base breakout"),
                      ("pat_C_pullback", "C pullback"), ("pat_D_retest", "D retest"),
                      ("pat_E_candle", "E candle"), ("pat_G_rel_strength", "G rel. strength"),
                      ("smc_sweep", "Sweep"), ("smc_order_block", "Order block"),
                      ("smc_fvg", "FVG"), ("smc_choch", "CHoCH"), ("vol_ok", "Volume")]:
        if col in df:
            g[f"pattern {name}"] = df[col].map({True: "yes", False: "no", "True": "yes", "False": "no"})
    if "trigger_vol_ratio" in df:
        g["trigger volume"] = bucket(df["trigger_vol_ratio"], [-1, 1.5, 2.5, 999],
                                     ["below 1.5x", "1.5-2.5x", "above 2.5x"])
    if "room_pct" in df:
        g["room to resistance"] = bucket(df["room_pct"], [-999, 8, 15, 999],
                                         ["under 8%", "8-15%", "over 15%"])
    if "rs_3m_vs_nifty" in df:
        g["3M vs Nifty"] = bucket(df["rs_3m_vs_nifty"], [-999, 0, 10, 999],
                                  ["behind", "0-10 pts ahead", "10+ pts ahead"])
    if "pct_below_high52" in df:
        g["below 52W high"] = bucket(df["pct_below_high52"], [-1, 5, 15, 999],
                                     ["within 5%", "5-15%", "over 15%"])
    if "support_kind" in df:                                  # weekly support picks (from 8 Oct)
        k = df["support_kind"].fillna("").astype(str).str.split(",").str[0].str.strip()
        g["support kind"] = k.where(k != "", None)
    if "zone_status" in df:
        z = df["zone_status"].fillna("").astype(str)
        g["zone at listing"] = z.where(~z.str.startswith("Above"), "Above zone").replace("", "n/a")
    return g


def stats(df):
    """Fill, T1 and dip numbers for one set of picks."""
    st = df["status"].astype(str)
    listed_done = df[st != "Waiting for entry"]
    bought = df[df["fill_date"].notna()]
    t1 = bought["t1_date"].notna()
    failed = bought["status"] == "Failed"
    decided = bought[t1 | bought["status"].isin(CLOSED)]
    days_t1 = (pd.to_datetime(bought.loc[t1, "t1_date"]) - pd.to_datetime(bought.loc[t1, "fill_date"])).dt.days
    return {
        "picks": int(len(df)),
        "fill_rate_pct": r2(100 * len(bought) / len(listed_done)) if len(listed_done) else None,
        "fill_base": int(len(listed_done)),
        "bought": int(len(bought)),
        "t1_hit": int(t1.sum()),
        "t2_hit": int((bought["status"] == "Full win (T2)").sum()),
        "failed": int(failed.sum()),
        "open_no_t1": int(len(bought) - len(decided)),
        "t1_rate_decided_pct": r2(100 * t1.sum() / len(decided)) if len(decided) else None,
        "running": int(bought["status"].astype(str).str.startswith("Running").sum()),
        "success_pct": r2(100 * (bought["status"] == "Full win (T2)").sum() / len(bought)) if len(bought) else None,
        "decided": int(len(decided)),
        "avg_worst_dip_pct": r2(bought["max_dip_pct"].mean()) if len(bought) else None,
        "avg_days_to_t1": r2(days_t1.mean()) if len(days_t1) else None,
        "avg_return_closed_pct": r2(bought.loc[bought["status"].isin(CLOSED), "return_pct"].mean()),
    }


def compare(df):
    groups = add_groups(df)
    overall = stats(df)
    table, signals = [], []
    for dim in groups.columns:
        for val, idx in groups.groupby(dim, dropna=True).groups.items():
            s = stats(df.loc[idx])
            row = {"group": dim, "value": str(val), **s}
            table.append(row)
            label = f"{dim} = {val}"
            if s["decided"] >= MIN_GROUP and overall["t1_rate_decided_pct"] is not None:
                gap = s["t1_rate_decided_pct"] - overall["t1_rate_decided_pct"]
                if abs(gap) >= GAP_PTS:
                    signals.append({"group": label, "kind": "T1 rate", "value": s["t1_rate_decided_pct"],
                                    "all_picks": overall["t1_rate_decided_pct"], "gap_pts": r2(gap),
                                    "sample": s["decided"], "direction": "better" if gap > 0 else "worse"})
            if s["fill_base"] >= MIN_GROUP and overall["fill_rate_pct"] is not None:
                gap = s["fill_rate_pct"] - overall["fill_rate_pct"]
                if abs(gap) >= GAP_PTS + 5:
                    signals.append({"group": label, "kind": "fill rate", "value": s["fill_rate_pct"],
                                    "all_picks": overall["fill_rate_pct"], "gap_pts": r2(gap),
                                    "sample": s["fill_base"], "direction": "better" if gap > 0 else "worse"})
            if s["bought"] >= MIN_GROUP and overall["avg_worst_dip_pct"] is not None:
                gap = s["avg_worst_dip_pct"] - overall["avg_worst_dip_pct"]
                if abs(gap) >= DIP_GAP_PTS:
                    signals.append({"group": label, "kind": "worst dip", "value": s["avg_worst_dip_pct"],
                                    "all_picks": overall["avg_worst_dip_pct"], "gap_pts": r2(gap),
                                    "sample": s["bought"], "direction": "better" if gap > 0 else "worse"})
    signals.sort(key=lambda x: -abs(x["gap_pts"]))
    return overall, table, signals


def todays_events(df, data_date):
    keep = ["list_date", "rank", "symbol", "status", "last_event", "last_event_date", "entry_low",
            "entry_high", "fill_date", "fill_price", "t1_date", "t2_date", "return_pct", "current_pct",
            "max_dip_pct", "days_held", "warning_at_listing"]
    keep += [c for c in FEATURE_COLS if c in df.columns and c not in keep]
    ev = df[(df["last_event_date"] == data_date) & (df["last_event"] != "Listed")]   # new listings are not results
    ev = ev[[c for c in keep if c in ev.columns]]
    return json.loads(ev.to_json(orient="records"))


# ---------------------------------------------------------------- completed wins
def completed_trades(df):
    """Every closed winner (T2, or T1 by day 30) with buy and sell price and days held,
    plus open trades that have already booked T1 (half sold at T1). Newest first."""
    out = {"closed": [], "t1_booked_open": []}
    if "status" not in df:
        return out
    won = df[df["status"].isin(["Full win (T2)", "Partial win (T1)"])].copy()
    for _, p in won.sort_values("close_date", ascending=False).iterrows():
        sell_date = p["t2_date"] if p["status"] == "Full win (T2)" else p["t1_date"]
        out["closed"].append({
            "symbol": p["symbol"], "entry_style": p["entry_style"], "list_date": p["list_date"],
            "result": p["status"], "buy_date": p["fill_date"], "buy_price": r2(p["fill_price"]),
            "sell_date": sell_date, "sell_price": r2(p["exit_price"]), "return_pct": r2(p["return_pct"]),
            "days_held": int((pd.Timestamp(sell_date) - pd.Timestamp(p["fill_date"])).days),
            "closed_on": p["close_date"]})
    t1o = df[df["status"] == "Running (T1 hit)"]
    for _, p in t1o.sort_values("t1_date", ascending=False).iterrows():
        out["t1_booked_open"].append({
            "symbol": p["symbol"], "entry_style": p["entry_style"], "list_date": p["list_date"],
            "buy_date": p["fill_date"], "buy_price": r2(p["fill_price"]), "t1_date": p["t1_date"],
            "t1_price": r2(p["t1"]), "t1_gain_pct": r2((p["t1"] / p["fill_price"] - 1) * 100),
            "days_to_t1": int((pd.Timestamp(p["t1_date"]) - pd.Timestamp(p["fill_date"])).days),
            "current_pct": r2(p["current_pct"])})
    return out


# ---------------------------------------------------------------- missed and better entries
# A fixed, small set of other entry rules, replayed on every support-style pick with the tracker's own
# replay (same 3-session entry window, same T1/T2 price levels, same 30-day exit). Only the buy price
# changes. The set is decided here once, not tuned to the data, so the review cannot curve-fit.
WHATIFS = {
    "Zone bottom only": lambda p: {**p, "entry_high": p["entry_low"]},
    "Zone up to 2% above top": lambda p: {**p, "entry_high": round(p["entry_high"] * 1.02, 2)},
    "Next day's open": lambda p: {**p, "entry_low": 0.0, "entry_high": 1e12},
}


def load_prices(symbols):
    """Daily prices for the picks, the same Yahoo source the tracker uses. Empty on any failure."""
    try:
        import scan_data
        return scan_data, scan_data.download([s + ".NS" for s in symbols], period="6mo", min_rows=1)
    except Exception as e:                                    # no network / module: the review goes on without it
        print("missed-entry prices unavailable:", e)
        return None, {}


def entry_window(p, df, n):
    """The first n sessions after the list date."""
    idx = df.index.tz_localize(None) if getattr(df.index, "tz", None) is not None else df.index
    d = df.copy()
    d.index = idx
    return d[d.index > pd.Timestamp(p["list_date"])].iloc[:n], d


def missed_entries(df):
    """Per pick: how close the price came to the zone, what a better buy price was, and what the
    fixed what-if entry rules would have done. Plus a table of each rule over all support picks."""
    picks = df[df["status"].astype(str) != "Price data unavailable"]
    sd, frames = load_prices(sorted(picks["symbol"].unique()))
    if sd is None or not frames:
        return None
    per, rows = [], {name: [] for name in ["As listed"] + list(WHATIFS)}
    base_cols = ["list_date", "symbol", "entry_style", "entry_low", "entry_high", "t1", "t2"]
    for _, p in picks.iterrows():
        prices = frames.get(p["symbol"] + ".NS")
        if prices is None or prices.empty:
            continue
        win, full = entry_window(p, prices, sd.ENTRY_WINDOW)
        if win.empty:
            continue
        base = {c: p[c] for c in base_cols}
        hi, lo = float(p["entry_high"]), float(p["entry_low"])
        win_low = float(win["Low"].min())
        rec = {"list_date": p["list_date"], "symbol": p["symbol"], "entry_style": p["entry_style"],
               "status": p["status"], "entry_low": r2(lo), "entry_high": r2(hi),
               "window_sessions": int(len(win)), "window_low": r2(win_low),
               "window_low_vs_zone_top_pct": r2((win_low / hi - 1) * 100)}
        if pd.notna(p.get("fill_price")):
            fill = float(p["fill_price"])
            rec["fill_price"] = r2(fill)
            rec["fill_vs_zone_bottom_pct"] = r2((fill / lo - 1) * 100)
            rec["better_buy_in_window_pct"] = r2(max(0.0, (fill / win_low - 1) * 100))
        else:
            # not bought (or still waiting): what the stock did over the next 30 days from the first session
            after = full[(full.index >= win.index[0]) &
                         (full.index <= win.index[0] + pd.Timedelta(days=sd.TIME_EXIT_DAYS))]
            rec["high_30d_vs_zone_top_pct"] = r2((float(after["High"].max()) / hi - 1) * 100)
        rec["whatif"] = {}
        for name, rule in WHATIFS.items():
            res = sd.replay_pick(rule(base), prices)
            rec["whatif"][name] = {k: res.get(k) for k in ["status", "fill_date", "fill_price", "t1_date",
                                                         "max_dip_pct", "return_pct", "current_pct"]}
            if p["entry_style"] != "Breakout":
                rows[name].append({**base, **res})
        if p["entry_style"] != "Breakout":
            rows["As listed"].append(sd.replay_pick(base, prices) | base)
        per.append(rec)

    table = []
    for name, rs in rows.items():
        if not rs:
            continue
        r = pd.DataFrame(rs)
        s = stats(r)
        bought = r[r["fill_date"].notna()]
        s["avg_buy_vs_zone_top_pct"] = r2(((bought["fill_price"].astype(float) /
                                            bought["entry_high"].astype(float)) - 1).mean() * 100) if len(bought) else None
        table.append({"rule": name, **s})
    missed_winners = [m for m in per if m["status"] == "Not bought"
                      and m["whatif"]["Next day's open"]["t1_date"]]
    return {
        "note": ("Support-style picks only (old breakouts left out). Each rule is replayed like the tracker: "
                 f"same {sd.ENTRY_WINDOW}-session entry window, same T1/T2 price levels, same "
                 f"{sd.TIME_EXIT_DAYS}-day exit; only the buy price changes. A rule needs {MIN_GROUP} decided "
                 "trades and a clear gap that holds over reviews before it is worth proposing."),
        "rules": table,
        "missed_winners": {"count": len(missed_winners),
                           "not_bought": sum(m["status"] == "Not bought" for m in per),
                           "symbols": [m["symbol"] for m in missed_winners]},
        "picks": per,
    }


def main():
    rebuild = "--rebuild" in sys.argv
    if not os.path.exists(PICKS):
        print("no picks log yet")
        return
    picks = pd.read_csv(PICKS, dtype={"list_date": str})
    meta = json.load(open(META, encoding="utf-8")) if os.path.exists(META) else {}
    data_date = meta.get("data_date")
    latest = pd.read_csv(LATEST) if os.path.exists(LATEST) else pd.DataFrame()

    feats = update_features(picks, latest, data_date, rebuild=rebuild)
    df = picks.merge(feats, on=["list_date", "symbol"], how="left", suffixes=("", "_f"))
    overall, table, signals = compare(df)
    missing = int(df["score"].isna().sum()) if "score" in df else len(df)

    out = {
        "data_date": data_date,
        "note": ("Simulated from daily prices, like the tracker. T1 rate counts only decided trades "
                 "(T1 reached, or closed). A group needs at least "
                 f"{MIN_GROUP} decided trades before it can raise a signal; small samples are not lessons."),
        "overall": overall,
        "todays_events": todays_events(df, data_date),
        "signals": signals,
        "groups": table,
        "picks_missing_setup_details": missing,
        "completed_trades": completed_trades(df),
        "missed_entries": missed_entries(picks),
        "files": {"features": FEATURES, "picks": PICKS},
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, default=str)
    print(f"feedback: {len(out['todays_events'])} events today, {len(signals)} signals, "
          f"{missing} picks without setup details")


if __name__ == "__main__":
    main()
