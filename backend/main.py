# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os 
import logging

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "quiz.db")

logging.basicConfig(level=logging.INFO)
app.logger = logging.getLogger("uvicorn.error")
app.logger.info(f"Using DB at: {DB_PATH}")

def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)

@app.get("/categories")
def get_categories():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT category FROM questions")
    categories = [r[0] for r in cur.fetchall()]
    conn.close()
    return {"categories": categories}

@app.get("/questions/{category}")
def get_questions(category: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT questionNumber, question, option1, option2, option3, option4, correct
        FROM questions WHERE category = ?
    """, (category,))
    rows = cur.fetchall()
    conn.close()
    return {
        "category": category,
        "questions": [
            {"questionNumber": r[0], "question": r[1], "options": [r[2], r[3], r[4], r[5]], "correct": r[6]}
            for r in rows
        ]
    }

# GEÇİCİ: Debug endpoint (silmeyi unutma)
@app.get("/_debug")
def debug():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    total = 0
    by_cat = []
    if "questions" in tables:
        cur.execute("SELECT COUNT(*) FROM questions")
        total = cur.fetchone()[0]
        cur.execute("SELECT category, COUNT(*) FROM questions GROUP BY category")
        by_cat = cur.fetchall()
    conn.close()
    return {"db_path": DB_PATH, "tables": tables, "total_rows": total, "rows_by_category": by_cat}
