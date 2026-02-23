import sqlite3
import os
from .config import DB_PATH


os.makedirs(DB_PATH.parent, exist_ok=True)

with sqlite3.connect(DB_PATH) as con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            mail TEXT UNIQUE,
            username TEXT UNIQUE,
            password TEXT,
            score INT DEFAULT 0,
            geography INT DEFAULT 0,
            history INT DEFAULT 0,
            math INT DEFAULT 0,
            science INT DEFAULT 0,
            technology INT DEFAULT 0
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            category TEXT NOT NULL,
            score INT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)
    con.commit()


def sign_up(mail, username, password):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        try:
            cur.execute(
                "INSERT INTO users (mail, username, password) "
                "VALUES (?, ?, ?)",
                (mail, username, password),
            )
            con.commit()
            return True
        except sqlite3.IntegrityError:
            return False


def login(username, password):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(
            "SELECT 1 FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        return cur.fetchone() is not None


def addscore(username, new_score, category=None):
    category_key = (category or "").strip().lower()
    allowed = {"geography", "history", "math", "science", "technology"}

    if category_key not in allowed:
        return False

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        cur.execute(
            f"SELECT {category_key} FROM users WHERE username = ?",
            (username,)
        )
        row = cur.fetchone()

        if row is None:
            return False

        current_record = row[0] or 0

        cur.execute(
            "INSERT INTO scores (username, category, score) VALUES (?, ?, ?)",
            (username, category_key, new_score)
        )
        cur.execute(
            "UPDATE users SET score = COALESCE(score, 0) + ? WHERE username = ?",
            (new_score, username)
        )

        if new_score > current_record:
            cur.execute(
                f"UPDATE users SET {category_key} = ? WHERE username = ?",
                (new_score, username)
            )

        con.commit()
        return True


def get_leaderboard(category, limit=10):
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(
            """
            SELECT
                username,
                MAX(score) AS best_score,
                COUNT(*) AS attempts,
                MAX(created_at) AS last_played
            FROM scores
            WHERE LOWER(category) = LOWER(?)
            GROUP BY username
            ORDER BY best_score DESC, attempts DESC, username ASC
            LIMIT ?
            """,
            (category, max(1, int(limit))),
        )
        return [dict(row) for row in cur.fetchall()]
