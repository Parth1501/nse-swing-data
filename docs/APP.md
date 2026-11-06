# Swing Desk: the phone app

An installable web app (PWA) for Android and iPhone that shows the option chain, swing ideas,
open trades and every analysis, and sends a push notification when something new lands.
No Play Store or App Store, no Firebase.

```
Claude routines ──► data/feed/<date>/<id>.json ──► GitHub (this repo)
GitHub Actions  ──► data/*.csv, option_chain, oc_learning ─┘        │ git pull every 60 s
OCI cron (5 min) ──► POST /api/admin/items ─────────────────┐       ▼
                                                            └─► Swing Desk service (OCI, 127.0.0.1:8765)
                                                                  │ SQLite: users, devices, feed
                                                                  │ Web Push (VAPID) ──► phones
                                                         nginx + Let's Encrypt (stock.unisolution.co.in)
```

## What is where

| Path | What |
|---|---|
| `app/backend/main.py` | FastAPI app: login, data API, push, background repo sync |
| `app/backend/repo.py` | Reads the repo files (latest.csv, picks_log.csv, option_chain, oc_learning, value) |
| `app/backend/webpush.py` | Web Push encryption + VAPID, on `cryptography` only |
| `app/backend/store.py` | SQLite tables |
| `app/web/` | The app itself: plain HTML/CSS/JS, service worker, icons. No build step |
| `app/deploy/install.sh` | One-command install/update on the server (no Docker) |
| `feed.py` | How routines and cron jobs publish an analysis to the app |

## Screens

- **Home**: Nifty spot and trends, PCR, walls, max pain, implied range, track record, global markets, latest posts.
- **Options**: weekly/monthly switch, today's spot path, pattern read and writer verdicts, OI ladder ±10 strikes with walls marked.
- **Ideas**: today's list and the top-ranked watch list with buy zone, T1/T2, why, and the chart; value shortlist.
- **Trades**: track record, open trades with current %, recently closed.
- **Feed**: every morning list, review, value pick, option chain read, trade update and alert. Tap for the full text.
- **Settings**: notifications on/off per device and per kind, test notification, install steps.

Notifications go out for every new feed item, and automatically when `picks_log.csv` shows a pick
being listed, bought, hitting T1/T2, failing or closing (one grouped "trade updates" message per sync).

## Server install (OCI, 1 GB is enough, no Docker)

Uses about 60 MB of RAM. Listens only on `127.0.0.1:8765` (set `SWINGDESK_PORT` to change it);
nginx forwards the domain to it and certbot adds the certificate. Your other nginx sites are not touched.

1. DNS: an A record for `stock.unisolution.co.in` pointing to the server's public IP.
2. On the server:
   ```bash
   git clone https://github.com/Parth1501/nse-swing-data.git ~/nse-swing-data
   cd ~/nse-swing-data
   ./app/deploy/install.sh stock.unisolution.co.in you@email.com
   ```
   It prints the **invite code** (give it to people you want in) and the **admin token** (keep it private).
   Settings and keys live in `/etc/swingdesk.env`; data in `/var/lib/swingdesk/`.
3. Open `https://stock.unisolution.co.in` on the phone, sign in with your name + invite code,
   install it (Android: Chrome menu → Install app; iPhone: Safari → Share → Add to Home Screen),
   then Settings → Turn on notifications → Send me a test notification.

Update later: `cd ~/nse-swing-data && git pull && ./app/deploy/install.sh`. Every step checks first and skips what is already done (packages, Python, settings, unchanged service, nginx site, certificate), so re-running is quick. `FORCE=1` redoes everything except the nginx site and certificate.
Logs: `journalctl -u swingdesk -f`.

Keep `/etc/swingdesk.env` safe: if the VAPID keys change, every phone has to turn notifications on again.

## Publishing an analysis

From a routine (inside its repo checkout), after the email is written:

```bash
python feed.py add --kind morning_list --title "Morning list · 6 Nov" \
  --summary "1 pick: TATAINVEST (buy 541–557). Global mildly positive." \
  --body-file /tmp/morning.md --symbols TATAINVEST
git add data/feed && git commit -m "Feed: morning list 6 Nov" && git push
```

Kinds: `morning_list`, `trade_review`, `value_pick`, `oc_read`, `alert`, `note`.
`--summary` is the notification text (keep it to one or two lines); `--body-file` is the full
Markdown shown in the app. The server picks it up within a minute.

From a cron job on the server (no git push needed, arrives instantly):

```bash
APP_URL=https://stock.unisolution.co.in APP_ADMIN_TOKEN=... \
  python feed.py add --kind alert --title "Nifty at call wall 25000" --summary "..." --post --no-file
```

or plain curl: `POST /api/admin/items` with `Authorization: Bearer <admin token>` and JSON
`{"kind","title","summary","body_md","symbols","notify"}`.

### From a Claude routine or thread (no git push there)

Build the item as JSON, base64 it, and start the **App feed** workflow; it writes the file with
`feed.py import` and pushes. The server shows it within about two minutes.

```bash
ITEM=$(python3 -c 'import base64,json,sys; print(base64.b64encode(json.dumps(json.load(sys.stdin)).encode()).decode())' < /tmp/item.json)
curl -sS -X POST -H "Accept: application/vnd.github+json" -H "Content-Type: application/json" \
  https://api.github.com/repos/Parth1501/nse-swing-data/actions/workflows/app_feed.yml/dispatches \
  -d "{\"ref\":\"main\",\"inputs\":{\"item\":\"$ITEM\"}}" -w 'HTTP %{http_code}'   # expect 204
```

`/tmp/item.json` is one item (or a list):
`{"kind":"morning_list","title":"…","summary":"one or two lines (the notification)","body_md":"full Markdown","symbols":["…"]}`.

### Option trades (F&O trades tab)

Every emailed Nifty option trade is posted as `kind: "option_trade"` with a `trade` object. Use the
same `trade_id` for the entry, its updates and the exit; the app folds them into one card with
levels, live P&L per lot (65) and a timeline.

```json
{"kind":"option_trade","title":"Nifty 8/10: bull call spread 24700/24850 (9 Nov)",
 "summary":"Buy 24700 CE (~146), sell 24850 CE (~85) for ~61. Target 95-100, stop 40 or close < 24600.",
 "body_md":"<the email text>",
 "trade":{"trade_id":"2026-11-06-bcs-24700-24850","event":"open","strategy":"Bull call spread",
          "expiry":"2026-11-09","legs":["BUY 24700 CE @ 146","SELL 24850 CE @ 85"],"entry":61,
          "target":"95-100","stop":"40 or close < 24600","conviction":8,"spot":24684,"now":61}}
```

Update: `"trade":{"trade_id":"…","event":"update","now":68,"spot":24728}` (no notification unless `"notify":true`).
Exit: `"trade":{"trade_id":"…","event":"exit","exit":96,"result":"Target hit","spot":24805}`.
Credit trades (iron condor, short strangle) add `"side":"credit"` so P&L is entry minus current.


## Working on it from VS Code

Clone the repo, open the folder, and install the **Claude Code** extension (or run `claude` in
the terminal). Everything is in this repo, so changes made there and changes pushed from the
project threads meet on GitHub.

Run it on your laptop against your local checkout:

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r app/backend/requirements.txt
cd app/backend
eval "$(python gen_keys.py | sed 's/^/export /')"
REPO_DIR=../.. REPO_SYNC=0 COOKIE_SECURE=0 DB_PATH=/tmp/swingdesk.db uvicorn main:app --reload --port 8765
```

Open http://localhost:8765 and sign in with the printed `INVITE_CODE`. Push works on localhost in Chrome too.

## Access and compliance

The app is invite-only on purpose: anyone without the invite code sees only the sign-in screen.
Sending buy/sell ideas to the general public can count as research advice under SEBI rules, so
keep it to people you know. Every screen says "Analysis only, not investment advice".
