"""
Sensex option chain snapshot (BSE). Runs in the same GitHub Actions job as option_chain.py, right
after the Nifty snapshot, so both indices are captured at about :16 and :46.

Reads BSE's public option chain API for two Sensex expiries (the nearest weekly one and the
monthly one, the last expiry of its calendar month) and appends one row per strike to
data/sensex_chain/<IST date>.csv. The columns are the same as the Nifty files so the same analysis
code works on both; the "nse_time" column holds BSE's own timestamp for the data.

`python sensex_chain.py --probe` prints the raw keys and one sample row of BSE's answer, for
checking the field mapping. A failure here never affects the Nifty snapshot.
"""
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

from option_chain import COLUMNS  # same columns as the Nifty files

IST = timezone(timedelta(hours=5, minutes=30))
OUT_DIR = os.path.join("data", "sensex_chain")
SCRIP = "1"   # BSE scrip code of the Sensex index
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
PAGE = "https://www.bseindia.com/markets/Derivatives/DeriReports/DeriOptionchain.html"
EXPIRY_API = "https://api.bseindia.com/BseIndiaAPI/api/ddlExpiry_IV/w?ProductType=IO&scrip_cd={scrip}"
CHAIN_API = ("https://api.bseindia.com/BseIndiaAPI/api/DerivOptionChain_IV/w"
             "?Expiry={exp}&scrip_cd={scrip}&strprice=0")
PENDING = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "sensex_chain_pending.json")

# BSE field names, tried in order (the API has used slightly different names over time).
STRIKE_KEYS = ("Strike_Price1", "Strike_Price", "StrikePrice", "STRIKE_PRICE")
SPOT_KEYS = ("UlaValue", "ULA_VALUE", "UnderlyingValue")
CE_KEYS = {"ltp": ("C_Last_Trd_Price", "C_LTP"), "oi": ("C_Open_Interest", "C_OI"),
           "chg_oi": ("C_Absolute_Change_OI", "C_Change_OI", "C_Chng_OI"), "iv": ("C_IV",),
           "volume": ("C_Vol_Traded", "C_Volume")}
PE_KEYS = {"ltp": ("Last_Trd_Price", "LTP", "P_Last_Trd_Price"), "oi": ("Open_Interest", "OI", "P_Open_Interest"),
           "chg_oi": ("Absolute_Change_OI", "Change_OI", "P_Absolute_Change_OI"), "iv": ("IV", "P_IV"),
           "volume": ("Vol_Traded", "Volume", "P_Vol_Traded")}
DATE_FORMATS = ("%d %b %Y", "%d-%b-%Y", "%d %B %Y", "%Y-%m-%d", "%d/%m/%Y")


def session():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "application/json, text/plain, */*",
                      "Accept-Language": "en-US,en;q=0.9", "Referer": "https://www.bseindia.com/",
                      "Origin": "https://www.bseindia.com"})
    try:
        s.get(PAGE, timeout=20)
    except Exception as e:
        print(f"BSE page did not load ({e}); trying the API anyway")
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
    raise RuntimeError(f"BSE did not answer: {url}")


def first(d, keys):
    for k in keys:
        if k in d and d[k] not in (None, ""):
            return d[k]
    return ""


def num(v):
    if v in (None, "", "-"):
        return ""
    try:
        return float(str(v).replace(",", "").strip())
    except ValueError:
        return ""


def parse_date(text):
    text = str(text).strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    return None


def table(j):
    """The list of row dicts inside a BSE answer, whatever the table is called."""
    if isinstance(j, list):
        return j
    for k in ("Table", "Table1", "Data", "data"):
        if isinstance(j.get(k), list):
            return j[k]
    for v in j.values():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            return v
    return []


def expiry_list(s):
    rows = table(get_json(s, EXPIRY_API.format(scrip=SCRIP)))
    out = []
    for r in rows:
        for v in r.values():
            d = parse_date(v)
            if d:
                out.append((d, str(v).strip()))
                break
    return sorted(set(out))


def pick_expiries(exps):
    """[(date, BSE text, 'weekly'|'monthly')]: nearest expiry, and the first monthly after it."""
    today = datetime.now(IST).replace(tzinfo=None, hour=0, minute=0, second=0, microsecond=0)
    exps = [e for e in exps if e[0] >= today]
    last_of_month = {}
    for d, t in exps:
        last_of_month[(d.year, d.month)] = (d, t)
    near = exps[0]
    monthly = next(e for e in sorted(last_of_month.values()) if e[0] > near[0])
    return [(near[0], near[1], "weekly"), (monthly[0], monthly[1], "monthly")]


def bse_time(j, now):
    """BSE's own data time as 'YYYY-MM-DD HH:MM:SS', or the snapshot time if it is not given."""
    blob = json.dumps(j.get("ASON", j.get("asOn", ""))) if isinstance(j, dict) else ""
    m = re.search(r"(\d{1,2} \w{3} \d{4})\s*\|?\s*(\d{1,2}:\d{2}(?::\d{2})?)", blob)
    if m:
        t = m.group(2) if m.group(2).count(":") == 2 else m.group(2) + ":00"
        d = parse_date(m.group(1))
        if d:
            return f"{d:%Y-%m-%d} {t}"
    return f"{now:%Y-%m-%d %H:%M:%S}"


def probe():
    s = session()
    raw = get_json(s, EXPIRY_API.format(scrip=SCRIP))
    print("expiry answer:", json.dumps(raw)[:1500])
    exps = expiry_list(s)
    print("expiries:", [t for _, t in exps][:8])
    if not exps:
        return
    picks = pick_expiries(exps)
    j = get_json(s, CHAIN_API.format(exp=picks[0][1].replace(" ", "+"), scrip=SCRIP))
    print("top-level keys:", list(j.keys()) if isinstance(j, dict) else type(j))
    rows = table(j)
    print("rows:", len(rows))
    if rows:
        mid = rows[len(rows) // 2]
        print("row keys:", list(mid.keys()))
        print("sample row:", json.dumps(mid)[:1500])
    print("ASON:", json.dumps(j.get("ASON", ""))[:300] if isinstance(j, dict) else "")


def fetch():
    """Read BSE and write the new rows to PENDING (nothing in the repo changes yet)."""
    now = datetime.now(IST)
    s = session()
    picks = pick_expiries(expiry_list(s))
    types = {f"{d:%Y-%m-%d}": t for d, _, t in picks}
    rows = []
    for d, text, kind in picks:
        j = get_json(s, CHAIN_API.format(exp=text.replace(" ", "+"), scrip=SCRIP))
        data = table(j)
        t = bse_time(j, now)
        expiry = f"{d:%Y-%m-%d}"
        if not t.startswith(f"{now:%Y-%m-%d}"):
            print(f"{expiry}: BSE data is from {t}, not today; skipped")
            continue
        spot = ""
        for r in data:
            spot = num(first(r, SPOT_KEYS))
            if spot != "":
                break
        added = 0
        for r in data:
            strike = num(first(r, STRIKE_KEYS))
            if strike == "":
                continue
            row = {"snapshot_ist": f"{now:%Y-%m-%d %H:%M:%S}", "nse_time": t, "spot": spot,
                   "expiry": expiry, "expiry_type": kind, "strike": strike}
            for side, keys in (("ce", CE_KEYS), ("pe", PE_KEYS)):
                for name, ks in keys.items():
                    row[f"{side}_{name}"] = num(first(r, ks))
            rows.append(row)
            added += 1
        rows.sort(key=lambda r: (r["expiry"], r["strike"]))
        print(f"{expiry} ({kind}): {added} strikes, spot {spot}, BSE time {t}")
        time.sleep(2)
    if not rows:
        print("no Sensex rows")
    with open(PENDING, "w") as f:
        json.dump({"date": f"{now:%Y-%m-%d}", "types": types, "rows": rows}, f)


def apply():
    """Append PENDING's rows to today's Sensex file, skipping any BSE time already saved."""
    import csv
    with open(PENDING) as f:
        p = json.load(f)
    path = os.path.join(OUT_DIR, f"{p['date']}.csv")
    os.makedirs(OUT_DIR, exist_ok=True)
    seen = {}
    if os.path.exists(path):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                seen.setdefault(row["expiry"], set()).add(row["nse_time"])
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
    arg = sys.argv[1:]
    if arg == ["--apply"]:
        apply()
    elif arg == ["--probe"]:
        probe()
    else:
        fetch()
