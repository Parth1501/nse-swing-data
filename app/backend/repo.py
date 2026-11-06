"""Reads the nse-swing-data repo checkout: syncs it and turns its files into API data."""
import csv
import glob
import json
import logging
import os
import subprocess
from functools import lru_cache

log = logging.getLogger("repo")

REPO_DIR = os.environ.get("REPO_DIR", "/data/repo")
REPO_URL = os.environ.get("REPO_URL", "https://github.com/Parth1501/nse-swing-data.git")
REPO_BRANCH = os.environ.get("REPO_BRANCH", "main")
DATA = lambda *p: os.path.join(REPO_DIR, "data", *p)  # noqa: E731

FEED_KINDS = {
    "morning_list": "Morning list",
    "trade_review": "Trade review",
    "value_pick": "Value pick",
    "option_trade": "Option trade",
    "oc_read": "Option chain",
    "trade_event": "Trade update",
    "alert": "Alert",
    "note": "Note",
}


# ---------- sync ----------
def _git(*args: str) -> str:
    return subprocess.run(["git", "-C", REPO_DIR, *args], check=True, capture_output=True,
                          text=True, timeout=300).stdout.strip()


def sync() -> bool:
    """Clones or fast-forwards the repo. Returns True when HEAD moved."""
    if not os.path.isdir(os.path.join(REPO_DIR, ".git")):
        os.makedirs(os.path.dirname(REPO_DIR) or ".", exist_ok=True)
        subprocess.run(["git", "clone", "--depth", "1", "--branch", REPO_BRANCH, REPO_URL, REPO_DIR],
                       check=True, capture_output=True, text=True, timeout=600)
        return True
    before = _git("rev-parse", "HEAD")
    _git("fetch", "--depth", "1", "origin", REPO_BRANCH)
    _git("reset", "--hard", f"origin/{REPO_BRANCH}")
    return _git("rev-parse", "HEAD") != before


def head() -> str:
    try:
        return _git("log", "-1", "--format=%h %cI %s")
    except Exception:
        return ""


# ---------- cached file readers ----------
def _mtime(path: str) -> float:
    try:
        return os.path.getmtime(path)
    except OSError:
        return 0.0


@lru_cache(maxsize=64)
def _read_csv(path: str, mtime: float) -> list[dict]:
    if not mtime:
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@lru_cache(maxsize=64)
def _read_json(path: str, mtime: float):
    if not mtime:
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def read_csv(path: str) -> list[dict]:
    return _read_csv(path, _mtime(path))


def read_json(path: str):
    return _read_json(path, _mtime(path))


def num(v, default=None):
    try:
        if v in ("", None):
            return default
        return float(v)
    except (TypeError, ValueError):
        return default


def truthy(v) -> bool:
    return str(v).strip().lower() in ("true", "1", "yes")


# ---------- feed ----------
def feed_files() -> list[dict]:
    """All feed items committed under data/feed/, oldest first."""
    items = []
    for path in sorted(glob.glob(DATA("feed", "**", "*.json"), recursive=True)):
        try:
            item = read_json(path)
        except Exception as e:  # bad file should not stop the sync
            log.warning("bad feed file %s: %s", path, e)
            continue
        if not isinstance(item, dict) or not item.get("id") or not item.get("title"):
            continue
        item.setdefault("kind", "note")
        item.setdefault("created_at", "")
        items.append(item)
    items.sort(key=lambda i: i["created_at"])
    return items


# ---------- picks / trades ----------
OPEN_STATUSES = {"Waiting for entry", "Running", "Running (T1 hit)"}

PICK_FIELDS = ["list_date", "rank", "symbol", "segment", "entry_style", "entry_low", "entry_high", "t1", "t2",
               "warning_at_listing", "sector", "status", "fill_date", "fill_price", "t1_date", "t2_date",
               "close_date", "exit_price", "return_pct", "current_pct", "max_dip_pct", "max_rise_pct",
               "days_held", "last_event", "last_event_date"]


def picks() -> list[dict]:
    return read_csv(DATA("picks_log.csv"))


def pick_key(p: dict) -> str:
    return f"{p.get('list_date')}|{p.get('symbol')}"


def trades() -> dict:
    rows = [{k: p.get(k, "") for k in PICK_FIELDS} for p in picks()]
    open_ = [r for r in rows if r["status"] in OPEN_STATUSES]
    closed = [r for r in rows if r["status"] not in OPEN_STATUSES]
    closed.sort(key=lambda r: r["close_date"] or r["last_event_date"] or r["list_date"], reverse=True)
    open_.sort(key=lambda r: r["list_date"], reverse=True)
    meta = read_json(DATA("meta.json")) or {}
    return {"track_record": meta.get("track_record", {}), "open": open_, "closed": closed[:40]}


# ---------- ideas ----------
IDEA_FIELDS = ["rank", "symbol", "segment", "sector", "date", "eligible", "score", "setups", "entry_style",
               "reason", "not_eligible_because", "warning", "flags", "zone_status", "close", "chg_pct",
               "entry_low", "entry_high", "t1", "t2", "support", "support_kind", "resistance", "room_pct",
               "candle", "ret_1m", "ret_3m", "rs_3m_vs_nifty", "sector_tag", "chart"]


def ideas(limit: int = 15) -> dict:
    rows = read_csv(DATA("latest.csv"))
    out = []
    for r in rows[:limit]:
        d = {k: r.get(k, "") for k in IDEA_FIELDS}
        d["eligible"] = truthy(d["eligible"])
        if d["chart"]:
            d["chart"] = "/files/" + d["chart"].removeprefix("data/")
        out.append(d)
    meta = read_json(DATA("meta.json")) or {}
    value_rows = read_csv(DATA("value", "shortlist.csv"))
    value_meta = read_json(DATA("value", "meta.json")) or {}
    value = [{k: v.get(k, "") for k in ("symbol", "company", "industry", "mcap_cr", "roce_pct", "roe_pct",
                                         "sales_cagr_pct", "profit_cagr_pct", "debt_equity", "pe",
                                         "industry_median_pe", "close", "pct_below_high52", "score")}
             for v in value_rows]
    return {
        "data_date": meta.get("data_date"),
        "generated_at_ist": meta.get("generated_at_ist"),
        "eligible_count": meta.get("eligible_count"),
        "stocks_analysed": meta.get("stocks_analysed"),
        "ideas": out,
        "value": {"data_date": value_meta.get("data_date"), "shortlist": value},
    }


# ---------- option chain ----------
def latest_oc_file() -> str | None:
    files = sorted(glob.glob(DATA("option_chain", "*.csv")))
    return files[-1] if files else None


def live_features(rs: list[dict], snapshot_ist: str) -> dict:
    """Same numbers oc_learn.py computes, but straight from the newest snapshot, so the app
    updates every 30 minutes instead of waiting for the hourly pattern run."""
    from datetime import datetime
    rs = sorted(rs, key=lambda r: num(r["strike"], 0))
    spot = num(rs[0]["spot"], 0)
    k = [num(r["strike"], 0) for r in rs]
    ce = [num(r["ce_oi"], 0) for r in rs]
    pe = [num(r["pe_oi"], 0) for r in rs]
    near = [abs(x / spot - 1) <= 0.03 if spot else False for x in k]
    ce_near = sum(c for c, n in zip(ce, near) if n)
    pe_near = sum(p for p, n in zip(pe, near) if n)
    pain = [sum(c * max(0, kk - s) + p * max(0, s - kk) for s, c, p in zip(k, ce, pe)) for kk in k]
    above = [i for i, x in enumerate(k) if x >= spot]
    below = [i for i, x in enumerate(k) if x <= spot]
    atm = rs[min(range(len(rs)), key=lambda i: abs(k[i] - spot))]
    ivs = [v for v in (num(atm["ce_iv"], 0), num(atm["pe_iv"], 0)) if v > 0]
    ce_l, pe_l = num(atm["ce_ltp"], 0), num(atm["pe_ltp"], 0)
    straddle = ce_l + pe_l if ce_l > 0 and pe_l > 0 else None
    try:
        exp_t = datetime.fromisoformat(rs[0]["expiry"] + " 15:30:00")
        dte = round(max((exp_t - datetime.fromisoformat(snapshot_ist)).total_seconds() / 86400, 0), 2)
    except ValueError:
        dte = None
    return {
        "expiry": rs[0]["expiry"], "type": rs[0]["expiry_type"], "dte": dte, "spot": spot,
        "pcr_near": round(pe_near / ce_near, 3) if ce_near else None,
        "max_pain": k[pain.index(min(pain))] if pain else None,
        "call_wall": k[max(above, key=lambda i: ce[i])] if above else None,
        "put_wall": k[max(below, key=lambda i: pe[i])] if below else None,
        "implied_move_pct": round(100 * straddle / spot, 2) if straddle and spot else None,
        "implied_range": [round(spot - straddle), round(spot + straddle)] if straddle else None,
        "atm_iv": round(sum(ivs) / len(ivs), 2) if ivs else None,
    }


def latest_snapshot() -> tuple[str | None, dict[str, list[dict]], list[dict]]:
    path = latest_oc_file()
    rows = read_csv(path) if path else []
    last = max((r["snapshot_ist"] for r in rows), default=None)
    by_exp: dict[str, list[dict]] = {}
    for r in rows:
        if r["snapshot_ist"] == last:
            by_exp.setdefault(r["expiry"], []).append(r)
    return last, by_exp, rows


def option_chain(strikes_each_side: int = 10) -> dict:
    learn = read_json(DATA("oc_learning", "latest.json")) or {}
    last, by_exp, rows = latest_snapshot()
    snapshots = sorted({r["snapshot_ist"] for r in rows})
    chains = []
    if last:
        for exp, rs in sorted(by_exp.items()):
            spot = num(rs[0]["spot"], 0)
            rs.sort(key=lambda r: num(r["strike"], 0))
            atm_i = min(range(len(rs)), key=lambda i: abs(num(rs[i]["strike"], 0) - spot))
            window = rs[max(0, atm_i - strikes_each_side): atm_i + strikes_each_side + 1]
            chains.append({
                "live": live_features(rs, last),
                "expiry": exp,
                "type": rs[0]["expiry_type"],
                "spot": spot,
                "nse_time": rs[0]["nse_time"],
                "total_ce_oi": sum(num(r["ce_oi"], 0) for r in rs),
                "total_pe_oi": sum(num(r["pe_oi"], 0) for r in rs),
                "strikes": [{
                    "strike": num(r["strike"]),
                    "ce_ltp": num(r["ce_ltp"]), "ce_oi": num(r["ce_oi"]), "ce_chg_oi": num(r["ce_chg_oi"]),
                    "ce_iv": num(r["ce_iv"]),
                    "pe_ltp": num(r["pe_ltp"]), "pe_oi": num(r["pe_oi"]), "pe_chg_oi": num(r["pe_chg_oi"]),
                    "pe_iv": num(r["pe_iv"]),
                } for r in window],
            })
    # spot path through the day (first expiry's spot per snapshot)
    spot_path = []
    seen = set()
    for r in rows:
        if r["snapshot_ist"] not in seen:
            seen.add(r["snapshot_ist"])
            spot_path.append({"t": r["snapshot_ist"][11:16], "spot": num(r["spot"])})
    return {"learning": learn, "snapshot_ist": last, "snapshots_today": len(snapshots),
            "chains": chains, "spot_path": spot_path}


# ---------- overview ----------
def overview() -> dict:
    meta = read_json(DATA("meta.json")) or {}
    glob_ = read_json(DATA("global.json")) or {}
    learn = read_json(DATA("oc_learning", "latest.json")) or {}
    weekly = (learn.get("expiries") or [{}])[0]
    last, by_exp, _ = latest_snapshot()
    as_of = learn.get("as_of")
    if last and by_exp and (not as_of or last > as_of):  # newer raw snapshot than the pattern run
        exp = weekly.get("expiry") if weekly.get("expiry") in by_exp else sorted(by_exp)[0]
        weekly = live_features(by_exp[exp], last)
        as_of = last
    open_trades = [p for p in picks() if p.get("status") in OPEN_STATUSES]
    return {
        "data_date": meta.get("data_date"),
        "nifty": meta.get("nifty"),
        "track_record": meta.get("track_record", {}),
        "open_trades": len(open_trades),
        "global": {
            "generated_at_ist": glob_.get("generated_at_ist"),
            "items": [{k: i.get(k) for k in ("name", "value", "change_pct", "for_date")}
                      for i in glob_.get("items", [])],
        },
        "oc": {
            "as_of": as_of,
            "trend_weekly": learn.get("trend_weekly"),
            "trend_125m": learn.get("trend_125m"),
            "trend_25m": learn.get("trend_25m"),
            "spot": weekly.get("spot"),
            "pcr_near": weekly.get("pcr_near"),
            "put_wall": weekly.get("put_wall"),
            "call_wall": weekly.get("call_wall"),
            "max_pain": weekly.get("max_pain"),
            "implied_range": weekly.get("implied_range"),
            "expiry": weekly.get("expiry"),
        },
        "repo_head": head(),
    }
