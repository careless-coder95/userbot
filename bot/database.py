import sqlite3
import os

DB_PATH = "bot/stark.db"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Database initialize
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id     INTEGER PRIMARY KEY,
            username    TEXT,
            approved    INTEGER DEFAULT 0,
            banned      INTEGER DEFAULT 0,
            session     TEXT DEFAULT NULL,
            joined_at   TEXT DEFAULT (datetime('now')),
            approved_at TEXT DEFAULT NULL
        )
    """)
    conn.commit()
    conn.close()


def get_conn():
    return sqlite3.connect(DB_PATH)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   User helpers
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def add_user(user_id: int, username: str = None):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO users (user_id, username)
        VALUES (?, ?)
    """, (user_id, username or ""))
    conn.commit()
    conn.close()


def get_user(user_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row


def is_approved(user_id: int) -> bool:
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT approved FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    return bool(row and row[0] == 1)


def is_banned(user_id: int) -> bool:
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT banned FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    return bool(row and row[0] == 1)


def approve_user(user_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE users SET approved = 1, approved_at = datetime('now')
        WHERE user_id = ?
    """, (user_id,))
    conn.commit()
    conn.close()


def unapprove_user(user_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE users SET approved = 0 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


def ban_user(user_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE users SET banned = 1, approved = 0 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


def unban_user(user_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE users SET banned = 0 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


def save_session(user_id: int, session: str):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE users SET session = ? WHERE user_id = ?", (session, user_id))
    conn.commit()
    conn.close()


def get_session(user_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT session FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None


def get_all_users():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT user_id, username, approved, banned, session, joined_at FROM users")
    rows = c.fetchall()
    conn.close()
    return rows


def get_stats():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    total = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE approved = 1")
    approved = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE banned = 1")
    banned = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE session IS NOT NULL")
    active = c.fetchone()[0]
    conn.close()
    return total, approved, banned, active
