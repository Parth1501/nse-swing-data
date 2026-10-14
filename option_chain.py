"""
Nifty option chain snapshot (runs on GitHub Actions every 30 minutes in market hours; each run
is started hourly by a Claude routine and takes a second snapshot 30 minutes later).

Reads NSE's own option chain for two Nifty expiries and appends one row per strike to
data/option_chain/<IST date>.csv: the nearest (weekly) expiry and the monthly expiry, which is
the last expiry of its calendar month. When the nearest expiry is itself the monthly one, the
monthly row comes from next month's monthly expiry instead. Only what NSE publishes is saved: spot, and for
each CE and PE the last price, OI, change in OI, IV and traded volume. No indicators.

Each row carries two times: when this run took the snapshot, and NSE's own timestamp for the
data. GitHub can start scheduled runs late, so analysis should use nse_time. A run whose NSE
timestamp is already saved for that expiry (market closed, holiday, NSE not updated yet) adds
nothing.
"""
import csv
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

IST = timezone(timedelta(hours=5, minutes=30))
OUT_DIR = os.path.join("data", "option_chain")
SYMBOL = "NIFTY"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
PAGE = "https://www.nseindia.com/option-chain"
EXPIRY_API = "https://www.nseindia.com/api/option-chain-contract-info?symbol={sym}"
CHAIN_API = "https://www.nseindia.com/api/option-chain-v3?type=Indices&symbol={sym}&expiry={exp}"
SIDE_FIELDS = (("ltp", "lastPrice"), ("oi", "openInterest"), ("chg_oi", "changeinOpenInterest"),
               ("iv", "impliedVolatility"), ("volume", "totalTradedVolume"))
COLUMNS = (["snapshot_ist", "nse_time", "spot", "expiry", "expiry_type", "strike"]
           + [f"{side}_{name}" for side in ("ce", "pe") for name, _ in SIDE_FIELDS])


def session():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
                      "Referer": PAGE})
    s.get(PAGE, timeout=20)          # sets the cookies the API needs
    return s


def get_json(s, url, tries=3):
    for i in range(tries):
        try:
            r = s.get(url, timeout=30)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            print(f"try {i + 1} failed: {url}: {e}")
            time.sleep(5 * (i + 1))
            try:
                s.get(PAGE, timeout=20)
            except Exception:
                pass
    raise RuntimeError(f"NSE did not answer: {url}")


def pick_expiries(dates):
    """{expiry 'DD-Mon-YYYY': 'weekly'|'monthly'}: the nearest expiry, and the first monthly
    expiry (last expiry of its month) after it."""
    ds = sorted(datetime.strptime(d, "%d-%b-%Y") for d in dates)
    last_of_month = {}
    for d in ds:
        last_of_month[(d.year, d.month)] = d
    monthly = next(d for d in sorted(last_of_month.values()) if d > ds[0])
    return {f"{ds[0]:%d-%b-%Y}": "weekly", f"{monthly:%d-%b-%Y}": "monthly"}


def add_type_column(path, types):
    """Older rows of today's file were saved without expiry_type: rewrite them with it."""
    with open(path, newline="") as f:
        r = csv.DictReader(f)
        if "expiry_type" in r.fieldnames:
            return
        old = list(r)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for row in old:
            row["expiry_type"] = types.get(row["expiry"], "")
            w.writerow(row)


def saved_times(path):
    """{expiry: set of nse_time} already in today's file."""
    seen = {}
    if os.path.exists(path):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                seen.setdefault(row["expiry"], set()).add(row["nse_time"])
    return seen


PENDING = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "option_chain_pending.json")


def fetch():
    """Read NSE and write the new rows to PENDING (nothing in the repo changes yet)."""
    now = datetime.now(IST)
    s = session()
    expiries = pick_expiries(get_json(s, EXPIRY_API.format(sym=SYMBOL))["expiryDates"])
    types = {datetime.strptime(e, "%d-%b-%Y").strftime("%Y-%m-%d"): t for e, t in expiries.items()}
    rows = []
    for exp in expiries:
        rec = get_json(s, CHAIN_API.format(sym=SYMBOL, exp=exp))["records"]
        nse_time = datetime.strptime(rec["timestamp"], "%d-%b-%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        expiry = datetime.strptime(exp, "%d-%b-%Y").strftime("%Y-%m-%d")
        if not nse_time.startswith(f"{now:%Y-%m-%d}"):
            print(f"{expiry}: NSE data is from {nse_time}, not today; skipped")
            continue
        for d in sorted(rec["data"], key=lambda x: x["strikePrice"]):
            row = {"snapshot_ist": f"{now:%Y-%m-%d %H:%M:%S}", "nse_time": nse_time,
                   "spot": rec["underlyingValue"], "expiry": expiry, "expiry_type": expiries[exp], "strike": d["strikePrice"]}
            for side in ("CE", "PE"):
                leg = d.get(side) or {}
                for name, key in SIDE_FIELDS:
                    row[f"{side.lower()}_{name}"] = leg.get(key, "")
            rows.append(row)
        print(f"{expiry} ({expiries[exp]}): {len(rec['data'])} strikes, spot {rec['underlyingValue']}, NSE time {nse_time}")
        time.sleep(2)
    with open(PENDING, "w") as f:
        json.dump({"date": f"{now:%Y-%m-%d}", "types": types, "rows": rows}, f)


def apply():
    """Append PENDING's rows to today's file, skipping any NSE time already saved. Run on a
    fresh copy of main each time, so two runs never fight over the same file."""
    with open(PENDING) as f:
        p = json.load(f)
    path = os.path.join(OUT_DIR, f"{p['date']}.csv")
    os.makedirs(OUT_DIR, exist_ok=True)
    if os.path.exists(path):
        add_type_column(path, p["types"])
    seen = saved_times(path)
    rows = [r for r in p["rows"] if r["nse_time"] not in seen.get(r["expiry"], set())]
    if rows:
        new = not os.path.exists(path)
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if new:
                w.writeheader()
            w.writerows(rows)
    print(f"{len(rows)} rows added to {path}")


if __name__ == "__main__":
    apply() if sys.argv[1:] == ["--apply"] else fetch()
