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
            score INT DEFAULT 0
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
