"""NSE Swing app backend: serves the web app, the repo's data and Web Push."""
import html
import hmac
import logging
import os
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

import httpx
import markdown
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

import repo
import store
import webpush

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("app")

IST = timezone(timedelta(hours=5, minutes=30))
INVITE_CODE = os.environ.get("INVITE_CODE", "")
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")
VAPID_PRIVATE = os.environ.get("VAPID_PRIVATE_KEY", "")
VAPID_PUBLIC = os.environ.get("VAPID_PUBLIC_KEY", "")
VAPID_SUBJECT = os.environ.get("VAPID_SUBJECT", "mailto:admin@example.com")
SYNC_SECONDS = int(os.environ.get("REPO_SYNC_SECONDS", "60"))
REPO_SYNC = os.environ.get("REPO_SYNC", "1") != "0"
WEB_DIR = os.environ.get("WEB_DIR", os.path.join(os.path.dirname(__file__), "..", "web"))
COOKIE = "nse_session"
COOKIE_SECURE = os.environ.get("COOKIE_SECURE", "1") != "0"

app = FastAPI(title="NSE Swing", docs_url=None, redoc_url=None)
pool = ThreadPoolExecutor(max_workers=8)


# ---------- auth ----------
def _token(request: Request) -> str:
    auth = request.headers.get("authorization", "")
    if auth.lower().startswith("bearer "):
        return auth[7:].strip()
    return request.cookies.get(COOKIE, "")


def user(request: Request) -> dict:
    u = store.user_for(_token(request)) if _token(request) else None
    if not u:
        raise HTTPException(401, "Sign in first")
    return u


def admin(request: Request) -> None:
    tok = _token(request)
    if not ADMIN_TOKEN or not hmac.compare_digest(tok, ADMIN_TOKEN):
        raise HTTPException(401, "Admin token required")


class Login(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    code: str


@app.post("/api/login")
def login(body: Login, response: Response):
    if not INVITE_CODE or not hmac.compare_digest(body.code.strip(), INVITE_CODE):
        raise HTTPException(403, "Wrong invite code")
    token = store.create_user(body.name.strip())
    response.set_cookie(COOKIE, token, max_age=3 * 365 * 86400, httponly=True, secure=COOKIE_SECURE,
                        samesite="lax")
    return {"ok": True, "name": body.name.strip()}


@app.post("/api/logout")
def logout(response: Response):
    response.delete_cookie(COOKIE)
    return {"ok": True}


@app.get("/api/me")
def me(u: dict = Depends(user)):
    return {"name": u["name"]}


@app.get("/api/config")
def config():
    return {"vapid_public_key": VAPID_PUBLIC, "kinds": repo.FEED_KINDS}


# ---------- data ----------
@app.get("/api/overview")
def overview(u: dict = Depends(user)):
    data = repo.overview()
    data["latest"] = store.list_items(limit=8)
    return data


@app.get("/api/option-chain")
def option_chain(u: dict = Depends(user)):
    return repo.option_chain()


@app.get("/api/ideas")
def ideas(u: dict = Depends(user)):
    return repo.ideas()


@app.get("/api/trades")
def trades(u: dict = Depends(user)):
    return repo.trades()


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def build_option_trades() -> list[dict]:
    """Folds every option_trade feed item into one record per trade_id."""
    trades: dict[str, dict] = {}
    for it in store.option_trade_items():
        t = it.get("trade") or {}
        tid = t.get("trade_id") or it["id"]
        rec = trades.setdefault(tid, {"trade_id": tid, "events": [], "opened_at": it["created_at"]})
        for k, v in t.items():
            if v not in (None, "", []):
                rec[k] = v
        rec["events"].append({"id": it["id"], "at": it["created_at"], "event": t.get("event", "update"),
                              "title": it["title"], "summary": it["summary"], "now": t.get("now"),
                              "spot": t.get("spot"), "exit": t.get("exit"), "result": t.get("result")})
        rec["updated_at"] = it["created_at"]
    out = []
    for rec in trades.values():
        last = rec["events"][-1]["event"]
        rec["status"] = "closed" if last in ("exit", "closed", "cancel") else "open"
        entry, mark = _num(rec.get("entry")), _num(rec.get("exit") if rec["status"] == "closed" else rec.get("now"))
        if entry is not None and mark is not None:
            sign = -1 if str(rec.get("side", "debit")).lower() == "credit" else 1
            pts = round((mark - entry) * sign, 2)
            lot = _num(rec.get("lot_size")) or 65
            rec["pnl_pts"], rec["pnl_rs"] = pts, round(pts * lot)
        rec.pop("event", None)
        rec.pop("now" if rec["status"] == "closed" else "exit", None)
        rec["events"].reverse()
        out.append(rec)
    out.sort(key=lambda r: (r["status"] != "open", r["updated_at"]), reverse=False)
    open_ = sorted([r for r in out if r["status"] == "open"], key=lambda r: r["updated_at"], reverse=True)
    closed = sorted([r for r in out if r["status"] != "open"], key=lambda r: r["updated_at"], reverse=True)
    return open_ + closed


@app.get("/api/option-trades")
def option_trades(u: dict = Depends(user)):
    return {"trades": build_option_trades()}


@app.get("/api/feed")
def feed(kind: str | None = None, before: str | None = None, limit: int = 30, u: dict = Depends(user)):
    return {"items": store.list_items(kind=kind, before=before, limit=min(limit, 100))}


def render_md(text: str) -> str:
    # Our own routines write the markdown; still escape raw HTML so nothing can inject script.
    return markdown.markdown(html.escape(text, quote=False), extensions=["tables", "sane_lists", "nl2br"])


@app.get("/api/feed/{item_id}")
def feed_item(item_id: str, u: dict = Depends(user)):
    item = store.get_item(item_id)
    if not item:
        raise HTTPException(404, "Not found")
    item["body_html"] = render_md(item.pop("body_md") or item["summary"])
    return item


_SAFE_FILE = re.compile(r"^charts/\d{4}-\d{2}-\d{2}/[A-Za-z0-9&_.-]+\.png$")


@app.get("/files/{path:path}")
def files(path: str, u: dict = Depends(user)):
    if not _SAFE_FILE.match(path):
        raise HTTPException(404)
    full = repo.DATA(path)
    if not os.path.isfile(full):
        raise HTTPException(404)
    return FileResponse(full, headers={"Cache-Control": "private, max-age=86400"})


# ---------- push ----------
class Subscription(BaseModel):
    endpoint: str
    keys: dict[str, str]


class Subscribe(BaseModel):
    subscription: Subscription
    kinds: list[str] = []


@app.post("/api/push/subscribe")
def subscribe(body: Subscribe, request: Request, u: dict = Depends(user)):
    s = body.subscription
    if not s.endpoint.startswith("https://") or "p256dh" not in s.keys or "auth" not in s.keys:
        raise HTTPException(400, "Bad subscription")
    kinds = [k for k in body.kinds if k in repo.FEED_KINDS]
    store.save_subscription(_token(request), s.endpoint, s.keys["p256dh"], s.keys["auth"], kinds)
    return {"ok": True, "kinds": kinds}


class Endpoint(BaseModel):
    endpoint: str


@app.post("/api/push/unsubscribe")
def unsubscribe(body: Endpoint, u: dict = Depends(user)):
    store.delete_subscription(body.endpoint)
    return {"ok": True}


@app.post("/api/push/status")
def push_status(body: Endpoint, u: dict = Depends(user)):
    s = store.get_subscription(body.endpoint)
    import json as _j
    return {"subscribed": bool(s), "kinds": _j.loads(s["kinds"]) if s else []}


@app.post("/api/push/test")
def push_test(body: Endpoint, u: dict = Depends(user)):
    s = store.get_subscription(body.endpoint)
    if not s:
        raise HTTPException(404, "This device is not subscribed")
    status = _send_one(s, {"title": "NSE Swing", "body": f"Test notification for {u['name']} works.",
                           "url": "/", "tag": "test"})
    return {"status": status}


def _send_one(sub: dict, payload: dict) -> int:
    if not VAPID_PRIVATE:
        log.warning("VAPID keys missing; push skipped")
        return 0
    try:
        status = webpush.send(sub, payload, VAPID_PRIVATE, VAPID_PUBLIC, VAPID_SUBJECT)
    except httpx.HTTPError as e:
        log.warning("push failed: %s", e)
        return 0
    if status in (404, 410):
        store.delete_subscription(sub["endpoint"])
    elif status >= 400:
        log.warning("push %s -> %s", sub["endpoint"][:60], status)
    return status


def notify(item: dict) -> None:
    payload = {"title": item["title"], "body": item.get("summary") or "", "url": f"/#/item/{item['id']}",
               "tag": item["kind"], "kind": item["kind"]}
    subs = store.subscriptions_for_kind(item["kind"])
    list(pool.map(lambda s: _send_one(s, payload), subs))
    store.mark_notified(item["id"])
    log.info("notified %d devices: %s", len(subs), item["title"])


# ---------- admin: post an item straight from a cron job ----------
class NewItem(BaseModel):
    id: str | None = None
    kind: str = "alert"
    title: str = Field(min_length=1, max_length=200)
    summary: str = ""
    body_md: str = ""
    symbols: list[str] = []
    notify: bool = True
    trade: dict | None = None


@app.post("/api/admin/items")
def admin_item(body: NewItem, _: None = Depends(admin)):
    if body.kind not in repo.FEED_KINDS:
        raise HTTPException(400, f"kind must be one of {list(repo.FEED_KINDS)}")
    now = datetime.now(IST)
    item = body.model_dump()
    item["id"] = body.id or f"{now:%Y-%m-%d-%H%M%S}-{body.kind}"
    item["created_at"] = now.isoformat(timespec="seconds")
    if store.item_exists(item["id"]):
        return {"ok": True, "id": item["id"], "duplicate": True}
    store.insert_item(item, source="api", notified=False)
    if body.notify:
        pool.submit(notify, item)
    return {"ok": True, "id": item["id"]}


@app.get("/api/admin/users")
def admin_users(_: None = Depends(admin)):
    return {"users": store.list_users()}


@app.post("/api/admin/sync")
def admin_sync(_: None = Depends(admin)):
    return {"new_items": sync_once()}


# ---------- background sync ----------
PICK_EVENT_WORDS = {
    "Listed": "new pick",
    "Bought": "bought (entry filled)",
    "T1 hit (+3%)": "T1 hit (+3%)",
    "T2 hit (+6%)": "T2 hit (+6%), full win",
    "Failed (30 days, no target)": "failed, 30 days without a target",
    "Not bought (entry never reached)": "not bought, entry never reached",
    "Closed: partial win (30 days, T1 only)": "closed, partial win (T1 only)",
}


def _pick_events(silent: bool) -> list[dict]:
    states = store.pick_states()
    changes = []
    for p in repo.picks():
        key, ev = repo.pick_key(p), p.get("last_event", "")
        if not ev or states.get(key) == ev:
            continue
        store.set_pick_state(key, ev)
        if not silent:
            changes.append(p)
    if not changes:
        return []
    lines = []
    for p in changes:
        word = PICK_EVENT_WORDS.get(p["last_event"], p["last_event"])
        extra = ""
        if p["last_event"] == "Listed":
            extra = f" · buy zone ₹{p['entry_low']}–{p['entry_high']}, T1 ₹{p['t1']}, T2 ₹{p['t2']}"
        elif p.get("return_pct"):
            extra = f" · return {p['return_pct']}%"
        elif p.get("fill_price"):
            extra = f" · filled ₹{p['fill_price']}"
        lines.append(f"- **{p['symbol']}** (listed {p['list_date']}): {word}{extra}")
    now = datetime.now(IST)
    syms = [p["symbol"] for p in changes]
    short = ", ".join(f"{p['symbol']} {PICK_EVENT_WORDS.get(p['last_event'], p['last_event']).split(',')[0]}"
                      for p in changes[:4])
    item = {
        "id": f"{now:%Y-%m-%d-%H%M%S}-trade-events",
        "kind": "trade_event",
        "title": f"{len(changes)} trade update{'s' if len(changes) > 1 else ''}",
        "summary": short + ("…" if len(changes) > 4 else ""),
        "body_md": "\n".join(lines),
        "symbols": syms,
        "created_at": now.isoformat(timespec="seconds"),
    }
    store.insert_item(item, source="picks", notified=False)
    return [item]


def sync_once() -> int:
    first_run = not store.kv_get("initialized", False)
    if REPO_SYNC:
        try:
            repo.sync()
        except Exception as e:
            log.warning("repo sync failed: %s", e)
    new = []
    for item in repo.feed_files():
        if store.item_exists(item["id"]):
            # keep the stored copy in step with the file (e.g. trade details saved by older code)
            store.refresh_item(item)
            continue
        store.insert_item(item, source="repo", notified=first_run)
        if not first_run and item.get("notify", True):
            new.append(item)
    new += _pick_events(silent=first_run)
    if first_run:
        store.kv_set("initialized", True)
    for item in new:
        notify(item)
    return len(new)


def _loop():
    while True:
        try:
            sync_once()
        except Exception:
            log.exception("sync failed")
        time.sleep(SYNC_SECONDS)


@app.on_event("startup")
def _start():
    store.db()
    threading.Thread(target=_loop, daemon=True, name="sync").start()


@app.get("/healthz")
def healthz():
    return {"ok": True, "repo": repo.head()}


# ---------- web app ----------
@app.get("/sw.js")
def sw():
    return FileResponse(os.path.join(WEB_DIR, "sw.js"), media_type="text/javascript",
                        headers={"Cache-Control": "no-cache", "Service-Worker-Allowed": "/"})


@app.exception_handler(HTTPException)
def http_err(request: Request, exc: HTTPException):
    return JSONResponse({"error": exc.detail}, status_code=exc.status_code)


app.mount("/", StaticFiles(directory=WEB_DIR, html=True), name="web")
