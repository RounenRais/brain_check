import sqlite3

db_quiz = {
    # your full db_quiz data here
}

conn = sqlite3.connect("db/quiz.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    questionNumber INTEGER,
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,
    correct TEXT
)
""")

for category, questions in db_quiz.items():
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (category, questionNumber, question, option1, option2, option3, option4, correct)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            category,
            q["questionNumber"],
            q["question"],
            q["options"][0],
            q["options"][1],
            q["options"][2],
            q["options"][3],
            q["correct"]
        ))

conn.commit()
conn.close()

print("✅ Database created and questions inserted successfully.")
