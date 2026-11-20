"""
Sensex option chain snapshot, read through Upstox's API (BSE's own site refuses GitHub's servers).
Runs in the same GitHub Actions job as option_chain.py, right after the Nifty snapshot, so both
indices are captured at about :16 and :46.

Needs one repository secret, passed in by the workflow as an environment variable:
  UPSTOX_ACCESS_TOKEN  an access token for your Upstox API app
Without it this script prints a note and saves nothing (the Nifty snapshot is never affected).
An Upstox token stops working at about 3:30 AM the next day, so it must be renewed daily (or use a
long-lived read-only token if Upstox has given one); a rejected token is printed in the job log.

Saves two Sensex expiries (the nearest weekly one, and the monthly one, the last expiry of its
calendar month) to data/sensex_chain/<IST date>.csv with the same columns as the Nifty files, so
the same analysis code works on both. Upstox gives no exchange timestamp, so "nse_time" holds the
snapshot time rounded to the minute; change in OI is OI minus Upstox's prev_oi (yesterday's).

CHAIN_INDEX=banknifty (or midcpselect) reads that index instead into data/<index>_chain/.

`python sensex_chain.py --probe` prints the expiry list and one sample strike, for checking the
mapping.
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
API = "https://api.upstox.com/v2"
# The same code reads other indexes through Upstox: set CHAIN_INDEX to one of these keys.
INDEXES = {
    "sensex": ("BSE_INDEX|SENSEX", "sensex_chain"),
    "banknifty": ("NSE_INDEX|Nifty Bank", "banknifty_chain"),
    "midcpselect": ("NSE_INDEX|NIFTY MID SELECT", "midcpselect_chain"),
}
INDEX = os.environ.get("CHAIN_INDEX", "sensex").strip().lower() or "sensex"
SENSEX, _dir = INDEXES[INDEX]
OUT_DIR = os.path.join("data", _dir)
PENDING = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), f"{_dir}_pending.json")


def creds():
    tok = os.environ.get("UPSTOX_ACCESS_TOKEN", "").strip()
    if not tok:
        print("UPSTOX_ACCESS_TOKEN secret is not set; no Sensex snapshot")
        return None
    return {"Authorization": f"Bearer {tok}", "Accept": "application/json"}


def get(headers, path, params, tries=3):
    for i in range(tries):
        try:
            r = requests.get(f"{API}{path}", headers=headers, params=params, timeout=30)
            if r.status_code != 200:
                print(f"Upstox {path}: HTTP {r.status_code}: {r.text[:300]}")
                if r.status_code == 401:
                    raise SystemExit("Upstox rejected the token (expired?); renew UPSTOX_ACCESS_TOKEN")
            r.raise_for_status()
            j = r.json()
            if str(j.get("status", "success")).lower() != "success":
                raise RuntimeError(f"Upstox said: {json.dumps(j)[:300]}")
            return j
        except SystemExit:
            raise
        except Exception as e:
            print(f"try {i + 1} failed: {path}: {e}")
            time.sleep(4 * (i + 1))
    raise RuntimeError(f"Upstox did not answer: {path}")


def expiries(headers):
    rows = get(headers, "/option/contract", {"instrument_key": SENSEX}).get("data", [])
    return sorted({r["expiry"] for r in rows if r.get("expiry")})


def pick_expiries(dates):
    """[(YYYY-MM-DD, 'weekly'|'monthly')]: nearest expiry, and the first monthly after it.
    Indexes with monthly expiries only (Bank Nifty, Midcap Select) give this month's and next month's."""
    today = f"{datetime.now(IST):%Y-%m-%d}"
    ds = sorted(d for d in dates if d >= today)
    last_of_month = {}
    for d in ds:
        last_of_month[d[:7]] = d
    monthlies = set(last_of_month.values())
    monthly = next(d for d in sorted(monthlies) if d > ds[0])
    first = "monthly" if INDEX != "sensex" and ds[0] in monthlies else "weekly"  # Sensex keeps its old labels
    return [(ds[0], first), (monthly, "monthly")]


def chain(headers, expiry):
    """(spot, [strike rows]) for one expiry."""
    rows = get(headers, "/option/chain", {"instrument_key": SENSEX, "expiry_date": expiry}).get("data", [])
    spot = next((r.get("underlying_spot_price") for r in rows if r.get("underlying_spot_price")), "")
    return spot, rows


def leg(side):
    """One side of a strike in our column names."""
    md, gk = (side or {}).get("market_data") or {}, (side or {}).get("option_greeks") or {}
    oi, prev = md.get("oi"), md.get("prev_oi")
    return {"ltp": md.get("ltp", ""), "oi": oi if oi is not None else "", "iv": gk.get("iv", ""),
            "volume": md.get("volume", ""),
            "chg_oi": (oi - prev) if isinstance(oi, (int, float)) and isinstance(prev, (int, float)) else ""}


def probe():
    h = creds()
    if not h:
        return
    dates = expiries(h)
    print("expiries:", dates[:8])
    picks = pick_expiries(dates)
    spot, rows = chain(h, picks[0][0])
    print("spot:", spot, "strikes:", len(rows))
    if rows:
        print("sample strike", json.dumps(rows[len(rows) // 2])[:1500])


def fetch():
    """Read Upstox and write the new rows to PENDING (nothing in the repo changes yet)."""
    now = datetime.now(IST)
    rows, types = [], {}
    h = creds()
    if h:
        stamp = f"{now:%Y-%m-%d %H:%M}:00"
        for expiry, kind in pick_expiries(expiries(h)):
            spot, strikes = chain(h, expiry)
            types[expiry] = kind
            for s in sorted(strikes, key=lambda r: float(r["strike_price"])):
                row = {"snapshot_ist": f"{now:%Y-%m-%d %H:%M:%S}", "nse_time": stamp, "spot": spot,
                       "expiry": expiry, "expiry_type": kind, "strike": float(s["strike_price"])}
                for side, key in (("ce", "call_options"), ("pe", "put_options")):
                    for name, v in leg(s.get(key)).items():
                        row[f"{side}_{name}"] = v
                rows.append(row)
            print(f"{expiry} ({kind}): {len(strikes)} strikes, spot {spot}")
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
