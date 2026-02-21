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


def addscore(username, new_score, category):
    allowed = ["geography", "history", "math", "scienca", "tecnology"]

    if category not in allowed:
        return False

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        cur.execute(
            f"SELECT {category} FROM users WHERE username = ?",
            (username,)
        )
        row = cur.fetchone()

        if row is None:
            return False

        current_record = row[0]

        if new_score > current_record:
            cur.execute(
                f"UPDATE users SET {category} = ? WHERE username = ?",
                (new_score, username)
            )
            con.commit()
            return True

        return False
