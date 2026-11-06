"""SQLite storage: users, push subscriptions, feed items, pick states."""
import json
import os
import secrets
import sqlite3
import threading
from datetime import datetime, timezone

DB_PATH = os.environ.get("DB_PATH", "/data/app.db")
_lock = threading.Lock()

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    token TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL,
    last_seen TEXT
);
CREATE TABLE IF NOT EXISTS subscriptions (
    endpoint TEXT PRIMARY KEY,
    token TEXT NOT NULL,
    p256dh TEXT NOT NULL,
    auth TEXT NOT NULL,
    kinds TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS items (
    id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    title TEXT NOT NULL,
    summary TEXT NOT NULL DEFAULT '',
    body_md TEXT NOT NULL DEFAULT '',
    symbols TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'repo',
    notified INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS items_created ON items(created_at DESC);
CREATE TABLE IF NOT EXISTS pick_states (
    key TEXT PRIMARY KEY,
    last_event TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS kv (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect() -> sqlite3.Connection:
    os.makedirs(os.path.dirname(DB_PATH) or ".", exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


_conn: sqlite3.Connection | None = None


def db() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = connect()
        _conn.executescript(SCHEMA)
    return _conn


def execute(sql: str, args=()):
    with _lock:
        cur = db().execute(sql, args)
        db().commit()
        return cur


def query(sql: str, args=()) -> list[dict]:
    with _lock:
        return [dict(r) for r in db().execute(sql, args).fetchall()]


# --- kv ---
def kv_get(key: str, default=None):
    rows = query("SELECT value FROM kv WHERE key=?", (key,))
    return json.loads(rows[0]["value"]) if rows else default


def kv_set(key: str, value) -> None:
    execute("INSERT INTO kv(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (key, json.dumps(value)))


# --- users ---
def create_user(name: str) -> str:
    token = secrets.token_urlsafe(32)
    execute("INSERT INTO users(token,name,created_at) VALUES(?,?,?)", (token, name[:60], now_iso()))
    return token


def user_for(token: str) -> dict | None:
    rows = query("SELECT * FROM users WHERE token=?", (token,))
    if rows:
        execute("UPDATE users SET last_seen=? WHERE token=?", (now_iso(), token))
        return rows[0]
    return None


def list_users() -> list[dict]:
    return query("SELECT u.name, u.created_at, u.last_seen, "
                 "(SELECT COUNT(*) FROM subscriptions s WHERE s.token=u.token) AS devices "
                 "FROM users u ORDER BY u.created_at")


# --- subscriptions ---
def save_subscription(token: str, endpoint: str, p256dh: str, auth: str, kinds: list[str]) -> None:
    execute("INSERT INTO subscriptions(endpoint,token,p256dh,auth,kinds,created_at) VALUES(?,?,?,?,?,?) "
            "ON CONFLICT(endpoint) DO UPDATE SET token=excluded.token, p256dh=excluded.p256dh, "
            "auth=excluded.auth, kinds=excluded.kinds",
            (endpoint, token, p256dh, auth, json.dumps(kinds), now_iso()))


def delete_subscription(endpoint: str) -> None:
    execute("DELETE FROM subscriptions WHERE endpoint=?", (endpoint,))


def get_subscription(endpoint: str) -> dict | None:
    rows = query("SELECT * FROM subscriptions WHERE endpoint=?", (endpoint,))
    return rows[0] if rows else None


def subscriptions_for_kind(kind: str) -> list[dict]:
    out = []
    for s in query("SELECT * FROM subscriptions"):
        kinds = json.loads(s["kinds"] or "[]")
        if not kinds or kind in kinds:
            out.append(s)
    return out


# --- items ---
def item_exists(item_id: str) -> bool:
    return bool(query("SELECT 1 FROM items WHERE id=?", (item_id,)))


def insert_item(item: dict, source: str, notified: bool) -> None:
    execute("INSERT OR IGNORE INTO items(id,kind,title,summary,body_md,symbols,created_at,source,notified) "
            "VALUES(?,?,?,?,?,?,?,?,?)",
            (item["id"], item["kind"], item["title"], item.get("summary", ""), item.get("body_md", ""),
             json.dumps(item.get("symbols", [])), item["created_at"], source, int(notified)))


def mark_notified(item_id: str) -> None:
    execute("UPDATE items SET notified=1 WHERE id=?", (item_id,))


def list_items(kind: str | None = None, limit: int = 50, before: str | None = None) -> list[dict]:
    sql = "SELECT id,kind,title,summary,symbols,created_at FROM items"
    where, args = [], []
    if kind:
        where.append("kind=?"); args.append(kind)
    if before:
        where.append("created_at<?"); args.append(before)
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY created_at DESC LIMIT ?"
    args.append(limit)
    rows = query(sql, args)
    for r in rows:
        r["symbols"] = json.loads(r["symbols"])
    return rows


def get_item(item_id: str) -> dict | None:
    rows = query("SELECT * FROM items WHERE id=?", (item_id,))
    if not rows:
        return None
    r = rows[0]
    r["symbols"] = json.loads(r["symbols"])
    return r


# --- picks ---
def pick_states() -> dict[str, str]:
    return {r["key"]: r["last_event"] for r in query("SELECT * FROM pick_states")}


def set_pick_state(key: str, event: str) -> None:
    execute("INSERT INTO pick_states(key,last_event) VALUES(?,?) "
            "ON CONFLICT(key) DO UPDATE SET last_event=excluded.last_event", (key, event))
