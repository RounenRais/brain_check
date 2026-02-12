# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import json


app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("geographyQuestion.json", "r", encoding="utf-8") as f:
    q1 = json.load(f)

with open("historyQuestion.json", "r", encoding="utf-8") as f:
    q2 = json.load(f)

with open("mathQuestion.json", "r", encoding="utf-8") as f:
    q3 = json.load(f)

with open("scienceQuestion.json", "r", encoding="utf-8") as f:
    q4 = json.load(f)

with open("technology.json", "r", encoding="utf-8") as f:
    q5 = json.load(f)

all_questions = q1 + q2 + q3 + q4 + q5


@app.get("/categories")
def get_categories():
    categories = {q["category"] for q in all_questions}
    return {"categories": list(categories)}


@app.get("/questions/{category}")
def get_questions(category: str):
    filtered = [q for q in all_questions if q["category"] == category.lower()]

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
