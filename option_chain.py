"""
Nifty option chain snapshot (runs on GitHub Actions every 30 minutes in market hours).

Reads NSE's own option chain for the two nearest Nifty expiries and appends one row per
strike to data/option_chain/<IST date>.csv. Only what NSE publishes is saved: spot, and for
each CE and PE the last price, OI, change in OI, IV and traded volume. No indicators.

Each row carries two times: when this run took the snapshot, and NSE's own timestamp for the
data. GitHub can start scheduled runs late, so analysis should use nse_time. A run whose NSE
timestamp is already saved for that expiry (market closed, holiday, NSE not updated yet) adds
nothing.
"""
import csv
import os
import time
from datetime import datetime, timedelta, timezone

import requests

IST = timezone(timedelta(hours=5, minutes=30))
OUT_DIR = os.path.join("data", "option_chain")
SYMBOL = "NIFTY"
EXPIRIES = 2                         # nearest expiries to save
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
PAGE = "https://www.nseindia.com/option-chain"
EXPIRY_API = "https://www.nseindia.com/api/option-chain-contract-info?symbol={sym}"
CHAIN_API = "https://www.nseindia.com/api/option-chain-v3?type=Indices&symbol={sym}&expiry={exp}"
SIDE_FIELDS = (("ltp", "lastPrice"), ("oi", "openInterest"), ("chg_oi", "changeinOpenInterest"),
               ("iv", "impliedVolatility"), ("volume", "totalTradedVolume"))
COLUMNS = (["snapshot_ist", "nse_time", "spot", "expiry", "strike"]
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


def saved_times(path):
    """{expiry: set of nse_time} already in today's file."""
    seen = {}
    if os.path.exists(path):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                seen.setdefault(row["expiry"], set()).add(row["nse_time"])
    return seen


def main():
    now = datetime.now(IST)
    path = os.path.join(OUT_DIR, f"{now:%Y-%m-%d}.csv")
    os.makedirs(OUT_DIR, exist_ok=True)
    s = session()
    expiries = get_json(s, EXPIRY_API.format(sym=SYMBOL))["expiryDates"][:EXPIRIES]
    seen = saved_times(path)
    rows = []
    for exp in expiries:
        rec = get_json(s, CHAIN_API.format(sym=SYMBOL, exp=exp))["records"]
        nse_time = datetime.strptime(rec["timestamp"], "%d-%b-%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        expiry = datetime.strptime(exp, "%d-%b-%Y").strftime("%Y-%m-%d")
        if not nse_time.startswith(f"{now:%Y-%m-%d}"):
            print(f"{expiry}: NSE data is from {nse_time}, not today; skipped")
            continue
        if nse_time in seen.get(expiry, set()):
            print(f"{expiry}: {nse_time} already saved; skipped")
            continue
        for d in sorted(rec["data"], key=lambda x: x["strikePrice"]):
            row = {"snapshot_ist": f"{now:%Y-%m-%d %H:%M:%S}", "nse_time": nse_time,
                   "spot": rec["underlyingValue"], "expiry": expiry, "strike": d["strikePrice"]}
            for side in ("CE", "PE"):
                leg = d.get(side) or {}
                for name, key in SIDE_FIELDS:
                    row[f"{side.lower()}_{name}"] = leg.get(key, "")
            rows.append(row)
        print(f"{expiry}: {len(rec['data'])} strikes, spot {rec['underlyingValue']}, NSE time {nse_time}")
        time.sleep(2)
    if rows:
        new = not os.path.exists(path)
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if new:
                w.writeheader()
            w.writerows(rows)
    print(f"{len(rows)} rows added to {path}")


if __name__ == "__main__":
    main()
