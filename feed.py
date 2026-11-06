"""Publishes one analysis to the phone app's feed.

Writes data/feed/<date>/<id>.json. Commit and push it, and the app server picks it up within a
minute and sends a notification to every installed phone.

    python feed.py add --kind morning_list --title "Morning list 6 Nov" \
        --summary "2 picks: TATAINVEST, NMDC. Global mildly positive." --body-file /tmp/morning.md

Kinds: morning_list, trade_review, value_pick, oc_read, alert, note.
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
IST = timezone(timedelta(hours=5, minutes=30))
ROOT = os.path.dirname(os.path.abspath(__file__))


def build(args) -> dict:
    now = datetime.now(IST)
    body = args.body or ""
    if args.body_file:
        with open(args.body_file, encoding="utf-8") as f:
            body = f.read()
    item_id = args.id or f"{now:%Y-%m-%d-%H%M}-{args.kind}"
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
    args = p.parse_args()

    item = build(args)
    if not args.no_file:
        folder = os.path.join(ROOT, "data", "feed", item["created_at"][:10])
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{item['id']}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=1)
        print(os.path.relpath(path, ROOT))
    if args.post:
        post(item)


if __name__ == "__main__":
    main()
