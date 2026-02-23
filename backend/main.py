from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from db.auth import sign_up, login, addscore, get_leaderboard
from pydantic import BaseModel
import sqlite3
import os
import json
import random


class RegUsers(BaseModel):
    mail: str
    username: str
    password: str


class LoginUsers(BaseModel):
    username: str
    password: str


class UserScore(BaseModel):
    username: str
    score: int
    category: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "Questions")
DB_PATH = os.path.join(BASE_DIR, "brain_check.db")


def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def load_all_questions():
    files = [
        "geographyQuestion.json",
        "historyQuestion.json",
        "mathQuestion.json",
        "scienceQuestion.json",
        "technologyQuestion.json"
    ]

    all_questions = []
    for f_name in files:
        path = os.path.join(DB_DIR, f_name)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            all_questions += data
    return all_questions


ALL_QUESTIONS = load_all_questions()


@app.get("/categories")
def get_categories():
    categories = sorted({q["category"] for q in ALL_QUESTIONS})
    return {"categories": categories}


@app.get("/questions/{category}")
def get_questions(category: str):
    filtered = [
        q
        for q in ALL_QUESTIONS
        if q["category"].lower() == category.lower()
    ]

    result = []

    for i in range(1, 11):
        same_number = [q for q in filtered if q["question_number"] == i]

        if same_number:
            q = random.choice(same_number)
            random.shuffle(q["options"])

            result.append({
                "question_number": q["question_number"],
                "question": q["question"],
                "options": q["options"],
                "correct": q["correct"]
            })

    return {"category": category, "questions": result}


@app.get("/leaderboard/{category}")
def leaderboard(category: str, limit: int = 10):
    return {
        "category": category,
        "leaderboard": get_leaderboard(category, limit)
    }


@app.post("/sign_up")
async def add_user(user: RegUsers):
    reg = sign_up(user.mail, user.username, user.password)

    if reg:
        return {
            "mail": user.mail,
            "username": user.username,
            "score": 0
        }

    return {"error": "User already exists"}


@app.post("/login")
async def verify_login(user: LoginUsers):
    if login(user.username, user.password):
        return {"message": f"Welcome, {user.username}"}
    return {"error": "Wrong username or password"}


@app.post("/add_score")
async def add_db(user: UserScore):
    res = addscore(user.username, user.score, user.category)

    if res:
        return {
            "username": user.username,
            "score": user.score,
            "category": user.category
        }
    return {"error": "Failed to add score"}
