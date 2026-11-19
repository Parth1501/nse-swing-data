"""
Sensex option chain snapshot, read through Dhan's official Data API (BSE's own site refuses
GitHub's servers). Runs in the same GitHub Actions job as option_chain.py, right after the Nifty
snapshot, so both indices are captured at about :16 and :46.

Needs two repository secrets, passed in by the workflow as environment variables:
  DHAN_CLIENT_ID     your Dhan client id
  DHAN_ACCESS_TOKEN  an access token from web.dhan.co > Profile > Access DhanHQ APIs
Without them this script prints a note and saves nothing (the Nifty snapshot is never affected).

Saves two Sensex expiries (the nearest weekly one, and the monthly one, the last expiry of its
calendar month) to data/sensex_chain/<IST date>.csv with the same columns as the Nifty files, so
the same analysis code works on both. Dhan gives no exchange timestamp, so "nse_time" holds the
snapshot time rounded to the minute; change in OI is OI minus Dhan's previous_oi (yesterday's).

`python sensex_chain.py --probe` prints the expiry list and one sample strike, for checking the
mapping. Dhan allows one option chain request every 3 seconds; this script waits 4.
"""
import csv
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

from option_chain import COLUMNS  # same columns as the Nifty files

IST = timezone(timedelta(hours=5, minutes=30))
OUT_DIR = os.path.join("data", "sensex_chain")
API = "https://api.dhan.co/v2"
UNDERLYING = {"UnderlyingScrip": 51, "UnderlyingSeg": "IDX_I"}   # 51 = SENSEX index on Dhan
PENDING = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "sensex_chain_pending.json")
SIDE_FIELDS = (("ltp", "last_price"), ("oi", "oi"), ("iv", "implied_volatility"), ("volume", "volume"))


def creds():
    cid, tok = os.environ.get("DHAN_CLIENT_ID", "").strip(), os.environ.get("DHAN_ACCESS_TOKEN", "").strip()
    if not cid or not tok:
        print("DHAN_CLIENT_ID / DHAN_ACCESS_TOKEN secrets are not set; no Sensex snapshot")
        return None
    return {"access-token": tok, "client-id": cid, "Content-Type": "application/json",
            "Accept": "application/json"}


def post(headers, path, body, tries=3):
    for i in range(tries):
        try:
            r = requests.post(f"{API}{path}", headers=headers, json=body, timeout=30)
            if r.status_code != 200:
                print(f"Dhan {path}: HTTP {r.status_code}: {r.text[:300]}")
            r.raise_for_status()
            j = r.json()
            if str(j.get("status", "success")).lower() != "success":
                raise RuntimeError(f"Dhan said: {json.dumps(j)[:300]}")
            return j
        except Exception as e:
            print(f"try {i + 1} failed: {path}: {e}")
            time.sleep(4 * (i + 1))
    raise RuntimeError(f"Dhan did not answer: {path}")


def pick_expiries(dates):
    """[(YYYY-MM-DD, 'weekly'|'monthly')]: nearest expiry, and the first monthly after it."""
    today = f"{datetime.now(IST):%Y-%m-%d}"
    ds = sorted(d for d in dates if d >= today)
    last_of_month = {}
    for d in ds:
        last_of_month[d[:7]] = d
    monthly = next(d for d in sorted(last_of_month.values()) if d > ds[0])
    return [(ds[0], "weekly"), (monthly, "monthly")]


def chain(headers, expiry):
    j = post(headers, "/optionchain", {**UNDERLYING, "Expiry": expiry})
    data = j.get("data", {})
    return data.get("last_price", ""), data.get("oc", {})


def probe():
    h = creds()
    if not h:
        return
    dates = post(h, "/optionchain/expirylist", UNDERLYING).get("data", [])
    print("expiries:", dates[:8])
    picks = pick_expiries(dates)
    time.sleep(4)
    spot, oc = chain(h, picks[0][0])
    keys = sorted(oc, key=float)
    print("spot:", spot, "strikes:", len(keys))
    if keys:
        k = keys[len(keys) // 2]
        print("sample strike", k, json.dumps(oc[k])[:1200])


def fetch():
    """Read Dhan and write the new rows to PENDING (nothing in the repo changes yet)."""
    now = datetime.now(IST)
    rows, types = [], {}
    h = creds()
    if h:
        dates = post(h, "/optionchain/expirylist", UNDERLYING).get("data", [])
        stamp = f"{now:%Y-%m-%d %H:%M}:00"
        for expiry, kind in pick_expiries(dates):
            time.sleep(4)
            spot, oc = chain(h, expiry)
            types[expiry] = kind
            for k in sorted(oc, key=float):
                row = {"snapshot_ist": f"{now:%Y-%m-%d %H:%M:%S}", "nse_time": stamp, "spot": spot,
                       "expiry": expiry, "expiry_type": kind, "strike": float(k)}
                for side in ("ce", "pe"):
                    leg = oc[k].get(side) or {}
                    for name, key in SIDE_FIELDS:
                        row[f"{side}_{name}"] = leg.get(key, "")
                    oi, prev = leg.get("oi"), leg.get("previous_oi")
                    row[f"{side}_chg_oi"] = (oi - prev) if isinstance(oi, (int, float)) and isinstance(prev, (int, float)) else ""
                rows.append(row)
            print(f"{expiry} ({kind}): {len(oc)} strikes, spot {spot}")
    with open(PENDING, "w") as f:
        json.dump({"date": f"{now:%Y-%m-%d}", "types": types, "rows": rows}, f)


def apply():
    """Append PENDING's rows to today's Sensex file, skipping any time already saved."""
    with open(PENDING) as f:
        p = json.load(f)
    path = os.path.join(OUT_DIR, f"{p['date']}.csv")
    seen = {}
    if os.path.exists(path):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                seen.setdefault(row["expiry"], set()).add(row["nse_time"])
    rows = [r for r in p["rows"] if r["nse_time"] not in seen.get(r["expiry"], set())]
    if rows:
        os.makedirs(OUT_DIR, exist_ok=True)
        new = not os.path.exists(path)
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if new:
                w.writeheader()
            w.writerows(rows)
    print(f"{len(rows)} rows added to {path}")


if __name__ == "__main__":
    arg = sys.argv[1:]
    if arg == ["--apply"]:
        apply()
    elif arg == ["--probe"]:
        probe()
    else:
        fetch()
