#!/usr/bin/env bash
# Installs or updates Swing Desk on the server, without Docker.
#
#   First time:  ./app/deploy/install.sh stock.unisolution.co.in you@email.com
#   Update:      git pull && ./app/deploy/install.sh
#   Redo all:    FORCE=1 ./app/deploy/install.sh
#
# Every step checks first and is skipped when it is already done, so re-running is quick and safe.
#
# What it does: Python 3.12 venv in ~/.swingdesk-venv (via uv), settings in /etc/swingdesk.env (keys made once),
# a systemd service on 127.0.0.1:$PORT (default 8765, never 8080), an nginx site for the domain,
# and a Let's Encrypt certificate for it through certbot. Other nginx sites are not touched.
set -euo pipefail

DOMAIN="${1:-}"
EMAIL="${2:-}"
PORT="${SWINGDESK_PORT:-8765}"
APP="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$HOME/.swingdesk-venv"
DATA_DIR="/var/lib/swingdesk"
ENV_FILE="/etc/swingdesk.env"
ME="$(id -un)"

FORCE="${FORCE:-0}"
STATE_DIR="$HOME/.swingdesk-install"
mkdir -p "$STATE_DIR"

say()  { printf '\n\033[1m%s\033[0m\n' "$*"; }
skip() { printf '   already done, skipping: %s\n' "$*"; }
# done_before <name> <fingerprint>: true when the step last finished with the same fingerprint
done_before() { [ "$FORCE" != 1 ] && [ -f "$STATE_DIR/$1" ] && [ "$(cat "$STATE_DIR/$1")" = "$2" ]; }
mark_done()   { printf '%s' "$2" > "$STATE_DIR/$1"; }
fingerprint() { cat "$@" 2>/dev/null | sha256sum | cut -c1-16; }

if ss -ltn 2>/dev/null | awk '{print $4}' | grep -qE "[:.]$PORT\$" && ! systemctl is-active --quiet swingdesk; then
  echo "Port $PORT is already used by something else. Run again with SWINGDESK_PORT=8766 (or another free port)." >&2
  exit 1
fi

say "1/5 Packages (git, curl, nginx, certbot)"
have_pkgs() {
  command -v git >/dev/null && command -v curl >/dev/null && command -v nginx >/dev/null \
    && command -v certbot >/dev/null \
    && { dpkg -s python3-certbot-nginx || rpm -q python3-certbot-nginx || sudo -n certbot plugins | grep -q nginx; } >/dev/null 2>&1
}
if [ "$FORCE" != 1 ] && have_pkgs; then
  skip "git, curl, nginx, certbot and its nginx plugin are installed"
elif command -v apt-get >/dev/null; then
  sudo apt-get update -qq
  sudo apt-get install -y -qq git curl nginx certbot python3-certbot-nginx >/dev/null
elif command -v dnf >/dev/null; then
  sudo dnf install -y -q git curl nginx certbot python3-certbot-nginx
else
  echo "Unknown Linux; install git, curl, nginx and certbot by hand, then re-run." >&2
fi

say "2/5 Python environment"
# The app needs Python 3.10+. uv downloads its own Python 3.12 into ~/.local/share/uv,
# so the system Python (3.8 on Ubuntu 20.04) and other apps are left as they are.
export PATH="$HOME/.local/bin:$PATH"
if command -v uv >/dev/null; then skip "uv"; else curl -LsSf https://astral.sh/uv/install.sh | sh; fi
if [ -x "$VENV/bin/python" ] && ! "$VENV/bin/python" -c 'import sys; sys.exit(sys.version_info < (3, 10))'; then
  rm -rf "$VENV"   # left over from an older run with the system Python
  rm -f "$STATE_DIR/requirements"
fi
if [ -x "$VENV/bin/python" ]; then skip "Python $("$VENV/bin/python" -V | cut -d' ' -f2) venv"; else uv venv -q --python 3.12 "$VENV"; fi
REQ_FP="$(fingerprint "$APP/backend/requirements.txt")"
if done_before requirements "$REQ_FP"; then
  skip "Python packages (requirements.txt unchanged)"
else
  uv pip install -q --python "$VENV/bin/python" -r "$APP/backend/requirements.txt"
  mark_done requirements "$REQ_FP"
fi

say "3/5 Settings"
sudo mkdir -p "$DATA_DIR" && sudo chown "$ME" "$DATA_DIR"
if [ -f "$ENV_FILE" ]; then skip "$ENV_FILE exists (keys and invite code kept)"; fi
if [ ! -f "$ENV_FILE" ]; then
  if [ -z "$DOMAIN" ] || [ -z "$EMAIL" ]; then
    echo "First run needs the domain and your email: ./app/deploy/install.sh stock.unisolution.co.in you@email.com" >&2
    exit 1
  fi
  KEYS="$(cd "$APP/backend" && "$VENV/bin/python" gen_keys.py)"
  sudo tee "$ENV_FILE" >/dev/null <<ENV
DOMAIN=$DOMAIN
VAPID_SUBJECT=mailto:$EMAIL
$KEYS
REPO_URL=https://github.com/Parth1501/nse-swing-data.git
REPO_BRANCH=main
REPO_DIR=$DATA_DIR/repo
DB_PATH=$DATA_DIR/app.db
WEB_DIR=$APP/web
REPO_SYNC_SECONDS=60
ENV
  sudo chown root:"$(id -gn)" "$ENV_FILE" && sudo chmod 640 "$ENV_FILE"
else
  sudo sed -i "s|^WEB_DIR=.*|WEB_DIR=$APP/web|" "$ENV_FILE"
fi
DOMAIN="$(sudo grep '^DOMAIN=' "$ENV_FILE" | cut -d= -f2)"

say "4/5 Service on 127.0.0.1:$PORT"
UNIT_NEW="$(sed -e "s|__USER__|$ME|" -e "s|__APP__|$APP|" -e "s|__VENV__|$VENV|" -e "s|__PORT__|$PORT|" \
  "$APP/deploy/swingdesk.service")"
UNIT_FILE=/etc/systemd/system/swingdesk.service
if [ "$FORCE" != 1 ] && [ -f "$UNIT_FILE" ] && [ "$(cat "$UNIT_FILE")" = "$UNIT_NEW" ]; then
  skip "systemd unit unchanged"
else
  printf '%s\n' "$UNIT_NEW" | sudo tee "$UNIT_FILE" >/dev/null
  sudo systemctl daemon-reload
  rm -f "$STATE_DIR/code"
fi
systemctl is-enabled --quiet swingdesk 2>/dev/null || sudo systemctl enable --quiet swingdesk
# restart only when the app code, packages or settings changed, or it is not running
CODE_FP="$(cd "$APP" && find backend web -type f ! -path '*__pycache__*' -print0 | sort -z | xargs -0 cat | sha256sum | cut -c1-16)-$REQ_FP-$(sudo cat "$ENV_FILE" | sha256sum | cut -c1-16)"
if systemctl is-active --quiet swingdesk && done_before code "$CODE_FP"; then
  skip "service running with the current code"
else
  sudo systemctl restart swingdesk
fi
for i in $(seq 1 20); do
  curl -fsS "http://127.0.0.1:$PORT/healthz" >/dev/null 2>&1 && break
  sleep 1
done
curl -fsS "http://127.0.0.1:$PORT/healthz" >/dev/null || { echo "Service did not start; see: journalctl -u swingdesk -n 50" >&2; exit 1; }
mark_done code "$CODE_FP"
echo "   service healthy on 127.0.0.1:$PORT"

say "5/5 nginx + Let's Encrypt for $DOMAIN"
SITE=/etc/nginx/conf.d/swingdesk.conf
[ -d /etc/nginx/sites-available ] && SITE=/etc/nginx/sites-available/swingdesk
# nginx: written once; after that certbot owns the file (it adds the 443 part), so it is never overwritten,
# not even with FORCE=1. Delete it by hand to have it written again.
if [ -f "$SITE" ]; then
  skip "nginx site $SITE exists"
else
  sed -e "s|__DOMAIN__|$DOMAIN|g" -e "s|__PORT__|$PORT|g" "$APP/deploy/nginx.conf" | sudo tee "$SITE" >/dev/null
  [ -d /etc/nginx/sites-enabled ] && sudo ln -sf "$SITE" /etc/nginx/sites-enabled/swingdesk
  sudo nginx -t
  sudo systemctl reload nginx
fi
if sudo test -d "/etc/letsencrypt/live/$DOMAIN"; then
  skip "Let's Encrypt certificate for $DOMAIN exists (certbot renews it automatically)"
else
  EMAIL_ARG=(--register-unsafely-without-email)
  [ -n "$EMAIL" ] && EMAIL_ARG=(-m "$EMAIL")
  sudo certbot --nginx -d "$DOMAIN" --non-interactive --agree-tos --redirect "${EMAIL_ARG[@]}"
fi

set -a; . <(sudo cat "$ENV_FILE"); set +a
say "Done: https://$DOMAIN"
echo "Invite code for people you want to add: $INVITE_CODE"
echo "Admin token (private, for cron jobs):     $ADMIN_TOKEN"
echo "Logs: journalctl -u swingdesk -f    Memory: systemctl status swingdesk"
