from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import os
import json
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "Questions")


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
    filtered = [q for q in ALL_QUESTIONS if q["category"].lower() == category.lower()]

    result = []

    for i in range(1, 11):
        same_number = [q for q in filtered if q["question_number"] == i]

        if same_number:
            q = random.choice(same_number)

            result.append({
                "question_number": q["question_number"],
                "question": q["question"],
                "options": q["options"],
                "correct": q["correct"]
            })

    return {"category": category, "questions": result}
