from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Allow frontend (Next.js) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to ["http://localhost:3000"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/categories")
def get_categories():
    conn = sqlite3.connect("db/quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category FROM questions")
    categories = [row[0] for row in cursor.fetchall()]
    conn.close()
    return {"categories": categories}

@app.get("/questions/{category}")
def get_questions(category: str):
    conn = sqlite3.connect("db/quiz.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT questionNumber, question, option1, option2, option3, option4, correct 
        FROM questions WHERE category = ?
    """, (category,))
    rows = cursor.fetchall()
    conn.close()
    questions = [
        {
            "questionNumber": r[0],
            "question": r[1],
            "options": [r[2], r[3], r[4], r[5]],
            "correct": r[6]
        }
        for r in rows
    ]
    return {"category": category, "questions": questions}
