"""Publishes one analysis to the phone app's feed.

Writes data/feed/<date>/<id>.json. Commit and push it, and the app server picks it up within a
minute and sends a notification to every installed phone.

    python feed.py add --kind morning_list --title "Morning list 6 Nov" \
        --summary "2 picks: TATAINVEST, NMDC. Global mildly positive." --body-file /tmp/morning.md

Kinds: morning_list, trade_review, value_pick, oc_read, alert, note.

Option trades get their own section in the app. Post the entry, any updates and the exit with the
same --trade-id, and the app shows one card per trade with its levels, live P&L and history:

    python feed.py trade --trade-id 2026-11-06-bcs-24700-24850 --event open \
        --title "Nifty 8/10: bull call spread 24700/24850 (9 Nov)" \
        --summary "Buy 24700 CE, sell 24850 CE for ~61. Target 95-100, stop 40 or close < 24600." \
        --strategy "Bull call spread" --expiry 2026-11-09 --conviction 8 \
        --legs "BUY 24700 CE @ 146" "SELL 24850 CE @ 85" --entry 61 --target "95-100" \
        --stop "40, or a 30-min close below 24600" --spot 24684 --body-file /tmp/trade.md
    python feed.py trade --trade-id 2026-11-06-bcs-24700-24850 --event update --now 68 --spot 24728 \
        --title "Spread 68, holding" --summary "Up ~7 pts. Hold for 95-100." --no-notify
    python feed.py trade --trade-id 2026-11-06-bcs-24700-24850 --event exit --exit 96 \
        --result "Target hit" --title "Exit: target hit at 96" --summary "Booked +35 pts (Rs 2,275/lot)."

Entry and exit notify by default; updates notify only with --notify.

From a Claude routine (no git push there): build the same JSON and start the "App feed" workflow,
which runs `python feed.py import --b64 <base64 of the JSON item or list of items>` and commits.
See docs/APP.md for the exact curl.
Add --post to also send it straight to the server (needs APP_URL and APP_ADMIN_TOKEN), which
is what the OCI option chain cron uses so alerts arrive without waiting for a git push.
"""
import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

KINDS = ["morning_list", "trade_review", "value_pick", "oc_read", "alert", "note"]
TRADE_EVENTS = ["open", "update", "exit"]
IST = timezone(timedelta(hours=5, minutes=30))
ROOT = os.path.dirname(os.path.abspath(__file__))


def build(args) -> dict:
    now = datetime.now(IST)
    body = args.body or ""
    if args.body_file:
        with open(args.body_file, encoding="utf-8") as f:
            body = f.read()
    item_id = args.id or f"{now:%Y-%m-%d-%H%M%S}-{args.kind}"
    if not re.fullmatch(r"[A-Za-z0-9_.-]{3,80}", item_id):
        sys.exit("id may only use letters, digits, '-', '_' and '.'")
    return {
        "id": item_id,
        "kind": args.kind,
        "title": args.title,
        "summary": args.summary or "",
        "body_md": body,
        "symbols": [s.strip().upper() for s in (args.symbols or "").split(",") if s.strip()],
        "created_at": now.isoformat(timespec="seconds"),
        "notify": not args.no_notify,
    }


def build_trade(args) -> dict:
    args.kind = "option_trade"
    if args.event == "update":
        args.no_notify = not args.notify
    item = build(args)
    trade = {
        "trade_id": args.trade_id,
        "event": args.event,
        "underlying": args.underlying,
        "strategy": args.strategy,
        "expiry": args.expiry,
        "legs": args.legs or [],
        "side": args.side,
        "entry": args.entry,
        "target": args.target,
        "stop": args.stop,
        "conviction": args.conviction,
        "lot_size": args.lot_size,
        "now": args.now,
        "spot": args.spot,
        "exit": args.exit,
        "result": args.result,
    }
    item["trade"] = {k: v for k, v in trade.items() if v not in (None, "", [])}
    item["symbols"] = item["symbols"] or [args.underlying]
    return item


def write_item(item: dict) -> str:
    folder = os.path.join(ROOT, "data", "feed", item["created_at"][:10])
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{item['id']}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(item, f, ensure_ascii=False, indent=1)
    return os.path.relpath(path, ROOT)


def import_items(raw: str) -> None:
    """Validates items sent by a routine (JSON object or list) and writes them."""
    import base64
    data = json.loads(base64.b64decode(raw).decode("utf-8"))
    items = data if isinstance(data, list) else [data]
    now = datetime.now(IST)
    for n, item in enumerate(items):
        kind = item.get("kind", "note")
        if kind not in KINDS + ["option_trade"]:
            sys.exit(f"unknown kind {kind!r}")
        if not str(item.get("title", "")).strip():
            sys.exit("every item needs a title")
        if kind == "option_trade":
            t = item.get("trade") or {}
            if not t.get("trade_id") or t.get("event") not in TRADE_EVENTS:
                sys.exit("option_trade needs trade.trade_id and trade.event (open/update/exit)")
        item["kind"] = kind
        item.setdefault("created_at", now.isoformat(timespec="seconds"))
        item.setdefault("id", f"{now:%Y-%m-%d-%H%M%S}-{kind}" + (f"-{n}" if len(items) > 1 else ""))
        if not re.fullmatch(r"[A-Za-z0-9_.-]{3,80}", item["id"]):
            sys.exit(f"bad id {item['id']!r}")
        item.setdefault("summary", "")
        item.setdefault("body_md", "")
        item.setdefault("symbols", [])
        item.setdefault("notify", not (kind == "option_trade" and item.get("trade", {}).get("event") == "update"))
        print(write_item(item))


def post(item: dict) -> None:
    url = os.environ["APP_URL"].rstrip("/") + "/api/admin/items"
    req = urllib.request.Request(url, data=json.dumps(item).encode(), method="POST", headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {os.environ['APP_ADMIN_TOKEN']}"})
    with urllib.request.urlopen(req, timeout=20) as r:
        print(r.read().decode())


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("--kind", required=True, choices=KINDS)
    a.add_argument("--title", required=True)
    a.add_argument("--summary", help="one or two lines; this is the notification text")
    a.add_argument("--body", help="full text in Markdown")
    a.add_argument("--body-file", help="read the Markdown body from this file")
    a.add_argument("--symbols", help="comma separated NSE symbols mentioned")
    a.add_argument("--id", help="unique id (default: <date>-<HHMM>-<kind>)")
    a.add_argument("--no-notify", action="store_true", help="add to the feed without a notification")
    a.add_argument("--post", action="store_true", help="also POST to APP_URL now")
    a.add_argument("--no-file", action="store_true", help="with --post: do not write the repo file")
    t = sub.add_parser("trade", help="an option trade entry, update or exit")
    t.add_argument("--trade-id", required=True, help="same id for the entry, its updates and the exit")
    t.add_argument("--event", required=True, choices=TRADE_EVENTS)
    t.add_argument("--title", required=True)
    t.add_argument("--summary", help="notification text")
    t.add_argument("--body")
    t.add_argument("--body-file")
    t.add_argument("--underlying", default="NIFTY")
    t.add_argument("--strategy", help="e.g. Bull call spread, Iron condor, Long CE")
    t.add_argument("--expiry", help="YYYY-MM-DD")
    t.add_argument("--legs", nargs="*", help='e.g. "BUY 24700 CE @ 146" "SELL 24850 CE @ 85"')
    t.add_argument("--side", choices=["debit", "credit"], default=None, help="debit (default) or credit trade")
    t.add_argument("--entry", type=float, help="net entry price in points")
    t.add_argument("--target")
    t.add_argument("--stop")
    t.add_argument("--conviction", type=int, help="score out of 10")
    t.add_argument("--lot-size", type=int, default=None, help="default 65 for Nifty")
    t.add_argument("--now", type=float, help="current value of the position in points")
    t.add_argument("--spot", type=float, help="Nifty spot at this moment")
    t.add_argument("--exit", type=float, help="exit price in points (with --event exit)")
    t.add_argument("--result", help='e.g. "Target hit", "Stopped out", "Time exit"')
    t.add_argument("--symbols")
    t.add_argument("--id")
    t.add_argument("--notify", action="store_true", help="notify for an update too")
    t.add_argument("--no-notify", action="store_true")
    t.add_argument("--post", action="store_true")
    t.add_argument("--no-file", action="store_true")
    im = sub.add_parser("import", help="write items sent by a routine through the App feed workflow")
    im.add_argument("--b64", required=True, help="base64 of a JSON item or a JSON list of items")
    args = p.parse_args()
    if args.cmd == "import":
        import_items(args.b64)
        return

    item = build_trade(args) if args.cmd == "trade" else build(args)
    if not args.no_file:
        print(write_item(item))
    if args.post:
        post(item)


if __name__ == "__main__":
    main()
