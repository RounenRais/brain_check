# init_db.py
import sqlite3
import os
import random
from config import DB_PATH

# 1) Klasörleri aç
os.makedirs(DB_PATH.parent, exist_ok=True)

# 2) Veritabanını aç
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 3) Tablonun taze kurulumu
cur.execute("DROP TABLE IF EXISTS questions")
cur.execute("""
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

# 4) VERİN (tamamını koy!)
db_quiz = {
  "Mathematics": [
    # === questionNumber 1: Algebra / linear equations ===
    {"questionNumber": 1, "question": "1. Solve for x: 3x - 7 = 11", "options": ["x = 6", "x = 18", "x = 3", "x = -6"], "correct": "x = 6"},
    {"questionNumber": 1, "question": "1. Solve for x: 5x + 2 = 2x + 14", "options": ["x = 4", "x = -4", "x = 6", "x = 2"], "correct": "x = 4"},
    {"questionNumber": 1, "question": "1. Solve for x: (x/4) + 3 = 7", "options": ["x = 8", "x = 12", "x = 14", "x = 16"], "correct": "x = 16"},
    {"questionNumber": 1, "question": "1. Solve for x: 2(2x - 5) = 3x + 1", "options": ["x = 11", "x =  -9", "x = 11", "x =  -?"], "correct": "x = 11"},
    {"questionNumber": 1, "question": "1. Solve for x: 7x - 4 = 2(3x + 1)", "options": ["x = 6", "x =  -6", "x = 2", "x = 1"], "correct": "x = 2"},
    {"questionNumber": 1, "question": "1. Solve for x: 0.5x + 1.5 = 2.5", "options": ["x = 1", "x = 2", "x = 3", "x = 0"], "correct": "x = 2"},
    {"questionNumber": 1, "question": "1. Solve for x: 4x/3 = 8", "options": ["x = 6", "x = 4", "x = 5", "x = 3"], "correct": "x = 6"},
    {"questionNumber": 1, "question": "1. Solve for x: x - 3 = 1/2", "options": ["x = 3.5", "x = 2.5", "x = 4", "x = 5"], "correct": "x = 3.5"},
    {"questionNumber": 1, "question": "1. Solve for x: 9x = 54", "options": ["x = 6", "x = 5", "x = 7", "x = 8"], "correct": "x = 6"},
    {"questionNumber": 1, "question": "1. Solve for x: 6 - x = 2", "options": ["x = 4", "x = -4", "x = 8", "x = 2"], "correct": "x = 4"},

    # === questionNumber 2: Quadratic equations / factoring ===
    {"questionNumber": 2, "question": "2. Solve: x^2 - 5x + 6 = 0", "options": ["x = 2 or 3", "x = -2 or -3", "x = 1 or 6", "x = -1 or -6"], "correct": "x = 2 or 3"},
    {"questionNumber": 2, "question": "2. Solve: x^2 + 4x + 4 = 0", "options": ["x = -2 (double)", "x = 2 or -2", "x = 4 or -1", "x = 0"], "correct": "x = -2 (double)"},
    {"questionNumber": 2, "question": "2. Solve: x^2 - 9 = 0", "options": ["x = 3 or -3", "x = 9 or -9", "x = 0 or 9", "x = 1 or -1"], "correct": "x = 3 or -3"},
    {"questionNumber": 2, "question": "2. Solve: x^2 - 4x = 0", "options": ["x = 0 or 4", "x = 2 or -2", "x = 4 only", "x = -4 only"], "correct": "x = 0 or 4"},
    {"questionNumber": 2, "question": "2. Find roots: x^2 - x - 6 = 0", "options": ["x = 3 or -2", "x = 2 or -3", "x = -3 or 2", "x = 1 or -6"], "correct": "x = 3 or -2"},
    {"questionNumber": 2, "question": "2. Solve: 2x^2 - 8x = 0", "options": ["x = 0 or 4", "x = 2 or -2", "x = 4 only", "x = -4 only"], "correct": "x = 0 or 4"},
    {"questionNumber": 2, "question": "2. Solve: x^2 + x - 12 = 0", "options": ["x = 3 or -4", "x = -3 or 4", "x = 4 or -3", "x = -4 or 3"], "correct": "x = 3 or -4"},
    {"questionNumber": 2, "question": "2. If x^2 = 16, x = ?", "options": ["±4", "4 only", "-4 only", "0"], "correct": "±4"},
    {"questionNumber": 2, "question": "2. Solve: x^2 - 2x - 3 = 0", "options": ["x = 3 or -1", "x = -3 or 1", "x = 1 or -3", "x = -1 or 3"], "correct": "x = 3 or -1"},
    {"questionNumber": 2, "question": "2. Solve: 3x^2 - 12 = 0", "options": ["x = ±2", "x = 2 only", "x = -2 only", "x = ±4"], "correct": "x = ±2"},

    # === questionNumber 3: Systems / simultaneous equations ===
    {"questionNumber": 3, "question": "3. Solve: { x + y = 7; x - y = 1 }", "options": ["x=4, y=3", "x=3, y=4", "x=5, y=2", "x=2, y=5"], "correct": "x=4, y=3"},
    {"questionNumber": 3, "question": "3. Solve: {2x + y = 8; x - y = 1}", "options": ["x=3, y=2", "x=2, y=4", "x=4, y=0", "x=5, y=-2"], "correct": "x=3, y=2"},
    {"questionNumber": 3, "question": "3. Solve: {3x + 2y = 12; x + y = 4}", "options": ["x=2, y=2", "x=3, y=1", "x=4, y=0", "x=1, y=3"], "correct": "x=2, y=2"},
    {"questionNumber": 3, "question": "3. Solve: {x + 2y = 5; 2x + 4y = 10}", "options": ["Infinitely many (dependent)", "No solution", "x=1, y=2", "x=2, y=1"], "correct": "Infinitely many (dependent)"},
    {"questionNumber": 3, "question": "3. Solve: {x + y = 0; x - y = 6}", "options": ["x=3, y=-3", "x=3, y=3", "x=-3, y=3", "x=6, y=-6"], "correct": "x=3, y=-3"},
    {"questionNumber": 3, "question": "3. Solve: {4x - y = 7; 2x + y = 5}", "options": ["x=2, y=1", "x=1, y=3", "x=3, y=-1", "x=0, y=5"], "correct": "x=2, y=1"},
    {"questionNumber": 3, "question": "3. Solve: {x + y = 10; x = 3y}", "options": ["x=7.5, y=2.5", "x=6, y=4", "x=5, y=5", "x=3, y=7"], "correct": "x=7.5, y=2.5"},
    {"questionNumber": 3, "question": "3. Solve: {5x + y = 11; x - 2y = 1}", "options": ["x=3, y=-4", "x=2, y=1", "x=1, y=6", "x=2, y=0.5"], "correct": "x=2, y=1"},
    {"questionNumber": 3, "question": "3. Solve: {x - y = 4; 3x + y = 14}", "options": ["x=4, y=0", "x=3, y=-1", "x=5, y=1", "x=2, y=-2"], "correct": "x=5, y=1"},
    {"questionNumber": 3, "question": "3. Solve: {2x + 3y = 16; 4x - 3y = 8}", "options": ["x=4, y=2", "x=2, y=4", "x=3, y=2", "x=1, y=5"], "correct": "x=4, y=2"},

    # === questionNumber 4: Functions / logs / exponents ===
    {"questionNumber": 4, "question": "4. Simplify: log_2(8)", "options": ["3", "2", "4", "1"], "correct": "3"},
    {"questionNumber": 4, "question": "4. Solve for x: 2^x = 32", "options": ["x = 5", "x = 6", "x = 4", "x = 3"], "correct": "x = 5"},
    {"questionNumber": 4, "question": "4. Simplify: log_10(1000)", "options": ["2", "3", "1", "4"], "correct": "3"},
    {"questionNumber": 4, "question": "4. Solve: e^{2x} = e^4", "options": ["x = 2", "x = 4", "x = 1", "x = 0"], "correct": "x = 2"},
    {"questionNumber": 4, "question": "4. Simplify: ln(e^5)", "options": ["5", "e^5", "ln 5", "1"], "correct": "5"},
    {"questionNumber": 4, "question": "4. Solve: 10^{x} = 0.01", "options": ["x = -2", "x = 2", "x = -1", "x = 1"], "correct": "x = -2"},
    {"questionNumber": 4, "question": "4. If f(x)=x^2, what is f(−3)?", "options": ["9", "-9", "6", "0"], "correct": "9"},
    {"questionNumber": 4, "question": "4. Simplify: log_3(1)", "options": ["0", "1", "3", "Undefined"], "correct": "0"},
    {"questionNumber": 4, "question": "4. Solve: 4^{x-1} = 16", "options": ["x = 3", "x = 2", "x = 4", "x = 5"], "correct": "x = 3"},
    {"questionNumber": 4, "question": "4. If g(x)=2^x, g(0) = ?", "options": ["1", "0", "2", "-1"], "correct": "1"},

    # === questionNumber 5: Trigonometry basics ===
    {"questionNumber": 5, "question": "5. What is sin(π/6)?", "options": ["1/2", "√2/2", "√3/2", "0"], "correct": "1/2"},
    {"questionNumber": 5, "question": "5. What is cos(π/3)?", "options": ["1/2", "1", "0", "√3/2"], "correct": "1/2"},
    {"questionNumber": 5, "question": "5. What is tan(π/4)?", "options": ["1", "0", "-1", "√3"], "correct": "1"},
    {"questionNumber": 5, "question": "5. Convert: sin 30° = ?", "options": ["1/2", "1/√2", "√3/2", "√2"], "correct": "1/2"},
    {"questionNumber": 5, "question": "5. What is cos 0°?", "options": ["1", "0", "-1", "1/2"], "correct": "1"},
    {"questionNumber": 5, "question": "5. If sin θ = 0, θ could be:", "options": ["0 or π", "π/2", "π/4", "π/3"], "correct": "0 or π"},
    {"questionNumber": 5, "question": "5. What is sin(π/2)?", "options": ["1", "0", "-1", "1/2"], "correct": "1"},
    {"questionNumber": 5, "question": "5. What is cos(π)?", "options": ["-1", "1", "0", "1/2"], "correct": "-1"},
    {"questionNumber": 5, "question": "5. Which identity is true?", "options": ["sin^2 x + cos^2 x = 1", "sin x + cos x = 1", "tan x = sin x + cos x", "cos 2x = cos^2 x + sin x"], "correct": "sin^2 x + cos^2 x = 1"},
    {"questionNumber": 5, "question": "5. What is tan 0°?", "options": ["0", "1", "Undefined", "∞"], "correct": "0"},

    # === questionNumber 6: Calculus — derivatives (basic) ===
    {"questionNumber": 6, "question": "6. Find d/dx (x^3)", "options": ["3x^2", "x^2", "x^3", "3x"], "correct": "3x^2"},
    {"questionNumber": 6, "question": "6. Find d/dx (sin x)", "options": ["cos x", "sin x", "-sin x", "-cos x"], "correct": "cos x"},
    {"questionNumber": 6, "question": "6. Find d/dx (e^x)", "options": ["e^x", "x e^{x-1}", "1", "ln e"], "correct": "e^x"},
    {"questionNumber": 6, "question": "6. If f(x)=x^2, f'(2) = ?", "options": ["4", "2", "8", "1"], "correct": "4"},
    {"questionNumber": 6, "question": "6. d/dx (ln x) = ?", "options": ["1/x", "ln x", "x", "e^x"], "correct": "1/x"},
    {"questionNumber": 6, "question": "6. d/dx (3x^2 + 2x) = ?", "options": ["6x + 2", "3x + 2", "6x^2 + 2", "3x^2 + 2x"], "correct": "6x + 2"},
    {"questionNumber": 6, "question": "6. d/dx (cos x) = ?", "options": ["-sin x", "sin x", "cos x", "-cos x"], "correct": "-sin x"},
    {"questionNumber": 6, "question": "6. If y = 5x, dy/dx = ?", "options": ["5", "x", "0", "1/5"], "correct": "5"},
    {"questionNumber": 6, "question": "6. d/dx (x^5) = ?", "options": ["5x^4", "x^4", "x^6", "5x^5"], "correct": "5x^4"},
    {"questionNumber": 6, "question": "6. If f(x)=3x^3, f'(1) = ?", "options": ["9", "3", "1", "27"], "correct": "9"},

    # === questionNumber 7: Calculus — integrals (basic) ===
    {"questionNumber": 7, "question": "7. ∫ x dx = ?", "options": ["x^2/2 + C", "x + C", "ln x + C", "1/x + C"], "correct": "x^2/2 + C"},
    {"questionNumber": 7, "question": "7. ∫ 3x^2 dx = ?", "options": ["x^3 + C", "x^3/3 + C", "3x + C", "x^4/4 + C"], "correct": "x^3 + C"},
    {"questionNumber": 7, "question": "7. ∫ cos x dx = ?", "options": ["sin x + C", "cos x + C", "-sin x + C", "-cos x + C"], "correct": "sin x + C"},
    {"questionNumber": 7, "question": "7. ∫ 1/x dx = ?", "options": ["ln|x| + C", "1/x + C", "x + C", "e^x + C"], "correct": "ln|x| + C"},
    {"questionNumber": 7, "question": "7. ∫ 0 dx = ?", "options": ["C", "0", "x + C", "1"], "correct": "C"},
    {"questionNumber": 7, "question": "7. ∫ 2 dx = ?", "options": ["2x + C", "x^2 + C", "ln 2 + C", "x + C"], "correct": "2x + C"},
    {"questionNumber": 7, "question": "7. ∫ x^2 dx = ?", "options": ["x^3/3 + C", "x^2/2 + C", "2x + C", "x + C"], "correct": "x^3/3 + C"},
    {"questionNumber": 7, "question": "7. ∫ sin x dx = ?", "options": ["-cos x + C", "sin x + C", "cos x + C", "-sin x + C"], "correct": "-cos x + C"},
    {"questionNumber": 7, "question": "7. ∫ (3) x^0 dx = ?", "options": ["3x + C", "x + C", "3 + C", "0"], "correct": "3x + C"},
    {"questionNumber": 7, "question": "7. ∫ (2x + 1) dx = ?", "options": ["x^2 + x + C", "x^2/2 + x + C", "2x^2 + x + C", "x^2 + C"], "correct": "x^2 + x + C"},

    # === questionNumber 8: Probability & combinatorics ===
    {"questionNumber": 8, "question": "8. Toss one fair coin. P(heads) = ?", "options": ["1/2", "1/4", "1", "0"], "correct": "1/2"},
    {"questionNumber": 8, "question": "8. Roll one fair six-sided die. P(rolling a 4) = ?", "options": ["1/6", "1/3", "1/2", "1/4"], "correct": "1/6"},
    {"questionNumber": 8, "question": "8. From {A,B,C} number of permutations = ?", "options": ["6", "3", "9", "1"], "correct": "6"},
    {"questionNumber": 8, "question": "8. Number of combinations C(5,2) = ?", "options": ["10", "5", "20", "15"], "correct": "10"},
    {"questionNumber": 8, "question": "8. If two independent events each have prob 1/3, P(both) = ?", "options": ["1/9", "2/3", "1/6", "1/3"], "correct": "1/9"},
    {"questionNumber": 8, "question": "8. P(at least one head in two coin tosses) = ?", "options": ["3/4", "1/4", "1/2", "1"], "correct": "3/4"},
    {"questionNumber": 8, "question": "8. In 3 coin tosses, P(exactly two heads) = ?", "options": ["3/8", "1/8", "1/2", "3/4"], "correct": "3/8"},
    {"questionNumber": 8, "question": "8. C(6,0) equals:", "options": ["1", "0", "6", "720"], "correct": "1"},
    {"questionNumber": 8, "question": "8. How many ways to arrange 'ABA' (distinct arrangements)?", "options": ["3", "6", "2", "1"], "correct": "3"},
    {"questionNumber": 8, "question": "8. Probability of drawing an ace from 52-card deck = ?", "options": ["4/52", "1/13", "1/52", "4/13"], "correct": "1/13"},

    # === questionNumber 9: Sequences / series / arithmetic-geometric ===
    {"questionNumber": 9, "question": "9. Sum of arithmetic series: a_1=3, d=2, n=5 → S_n = ?", "options": ["35", "25", "40", "30"], "correct": "35"},
    {"questionNumber": 9, "question": "9. nth term of arithmetic sequence a_n = 4 + (n-1)3. a_4 = ?", "options": ["13", "12", "10", "16"], "correct": "13"},
    {"questionNumber": 9, "question": "9. Sum of first 4 terms of geometric series 2, 6, 18,... = ?", "options": ["2 +6 +18 +54 = 80", "40", "26", "60"], "correct": "2 +6 +18 +54 = 80"},
    {"questionNumber": 9, "question": "9. For geometric with r=3, a=2, S_3 = ?", "options": ["26", "18", "20", "24"], "correct": "26"},
    {"questionNumber": 9, "question": "9. If a_n = 5n, a_3 = ?", "options": ["15", "10", "5", "20"], "correct": "15"},
    {"questionNumber": 9, "question": "9. Limit of 1/n as n→∞ = ?", "options": ["0", "1", "∞", "Undefined"], "correct": "0"},
    {"questionNumber": 9, "question": "9. Sum 1+2+3+...+10 = ?", "options": ["55", "45", "65", "50"], "correct": "55"},
    {"questionNumber": 9, "question": "9. If a_1=1 and r=2, a_5 = ?", "options": ["16", "8", "32", "10"], "correct": "16"},
    {"questionNumber": 9, "question": "9. For sequence 2,4,8,16..., a_6 = ?", "options": ["64", "32", "128", "256"], "correct": "64"},
    {"questionNumber": 9, "question": "9. Sum of first n of 1 (constant) = ?", "options": ["n", "1", "n^2", "0"], "correct": "n"},

    # === questionNumber 10: Matrices, determinants, basic linear algebra ===
    {"questionNumber": 10, "question": "10. For 2x2 matrix A = [[1,2],[3,4]], det(A) = ?", "options": ["(1)(4)-(2)(3)= -2", "10", "0", "1"], "correct": "(1)(4)-(2)(3)= -2"},
    {"questionNumber": 10, "question": "10. If A = [[2,0],[0,2]], det(A) = ?", "options": ["4", "2", "0", "1"], "correct": "4"},
    {"questionNumber": 10, "question": "10. Identity 2x2 matrix I has determinant:", "options": ["1", "2", "0", "-1"], "correct": "1"},
    {"questionNumber": 10, "question": "10. For matrix [[1,0],[0,1]] inverse = ?", "options": ["Same matrix", "Zero matrix", "Negative matrix", "No inverse"], "correct": "Same matrix"},
    {"questionNumber": 10, "question": "10. Multiply scalar 3 by matrix [[1,2],[3,4]] result element (1,2) = ?", "options": ["6", "2", "3", "9"], "correct": "6"},
    {"questionNumber": 10, "question": "10. If A is 2x2 and det(A)=0, A is:", "options": ["Singular", "Invertible", "Orthogonal", "Identity"], "correct": "Singular"},
    {"questionNumber": 10, "question": "10. Trace of [[1,2],[3,4]] = ?", "options": ["1+4 = 5", "2+3 = 5", "4", "10"], "correct": "1+4 = 5"},
    {"questionNumber": 10, "question": "10. Solve for x in matrix equation: [[1,0],[0,1]]x = [[2,3],[4,5]] → x = ?", "options": ["[[2,3],[4,5]]", "Zero", "No solution", "Identity"], "correct": "[[2,3],[4,5]]"},
    {"questionNumber": 10, "question": "10. Determinant property: det(kA) for 2x2 matrix = ?", "options": ["k^2 det(A)", "k det(A)", "det(A)/k", "det(A)"], "correct": "k^2 det(A)"},
    {"questionNumber": 10, "question": "10. If A = [[0,1],[-1,0]] (rotation by 90°), det(A) = ?", "options": ["1", "-1", "0", "2"], "correct": "1"}
  ],
"History": [
  # questionNumber 1
  {"questionNumber": 1, "question": "1. When did World War I begin?", "options": ["1912", "1914", "1916", "1918"], "correct": "1914"},
  {"questionNumber": 1, "question": "2. Which empire collapsed after World War I?", "options": ["Roman", "Ottoman", "Persian", "Mongol"], "correct": "Ottoman"},
  {"questionNumber": 1, "question": "3. Who was the founder of the Republic of Turkey?", "options": ["Ismet Inönü", "Mustafa Kemal Atatürk", "Celal Bayar", "Abdülhamid II"], "correct": "Mustafa Kemal Atatürk"},
  {"questionNumber": 1, "question": "4. In which year did Kazakhstan gain independence?", "options": ["1989", "1990", "1991", "1992"], "correct": "1991"},
  {"questionNumber": 1, "question": "5. What was the capital of the Ottoman Empire?", "options": ["Ankara", "Edirne", "Istanbul", "Bursa"], "correct": "Istanbul"},
  {"questionNumber": 1, "question": "6. Who was the first President of Kazakhstan?", "options": ["Nursultan Nazarbayev", "Kassym-Jomart Tokayev", "Dinmukhamed Kunayev", "Akhmet Baitursynov"], "correct": "Nursultan Nazarbayev"},
  {"questionNumber": 1, "question": "7. When did World War II begin?", "options": ["1937", "1938", "1939", "1940"], "correct": "1939"},
  {"questionNumber": 1, "question": "8. Which event ended World War II?", "options": ["Attack on Pearl Harbor", "Battle of Stalingrad", "Atomic bomb on Hiroshima", "Treaty of Versailles"], "correct": "Atomic bomb on Hiroshima"},
  {"questionNumber": 1, "question": "9. When was the United Nations founded?", "options": ["1919", "1939", "1945", "1950"], "correct": "1945"},
  {"questionNumber": 1, "question": "10. What was the Cold War mainly about?", "options": ["Territory", "Nuclear tension", "Religion", "Oil"], "correct": "Nuclear tension"},

  # questionNumber 2
  {"questionNumber": 2, "question": "1. When was the Republic of Turkey proclaimed?", "options": ["1920", "1921", "1923", "1924"], "correct": "1923"},
  {"questionNumber": 2, "question": "2. In which year did the Battle of Ankara occur between Timur and Bayezid I?", "options": ["1398", "1400", "1402", "1405"], "correct": "1402"},
  {"questionNumber": 2, "question": "3. What year did the Soviet Union dissolve?", "options": ["1989", "1990", "1991", "1992"], "correct": "1991"},
  {"questionNumber": 2, "question": "4. Which ancient civilization built the pyramids?", "options": ["Roman", "Greek", "Egyptian", "Sumerian"], "correct": "Egyptian"},
  {"questionNumber": 2, "question": "5. When did the Berlin Wall fall?", "options": ["1985", "1987", "1989", "1991"], "correct": "1989"},
  {"questionNumber": 2, "question": "6. What was the capital of the Byzantine Empire?", "options": ["Athens", "Constantinople", "Rome", "Alexandria"], "correct": "Constantinople"},
  {"questionNumber": 2, "question": "7. Which Kazakh khan united the Kazakh tribes in the 15th century?", "options": ["Abylai Khan", "Kerey Khan", "Tauke Khan", "Janibek Khan"], "correct": "Kerey Khan"},
  {"questionNumber": 2, "question": "8. Who discovered America in 1492?", "options": ["Ferdinand Magellan", "Christopher Columbus", "Marco Polo", "Vasco da Gama"], "correct": "Christopher Columbus"},
  {"questionNumber": 2, "question": "9. What empire was known as the ‘Empire on which the sun never sets’?", "options": ["Ottoman", "British", "Mongol", "French"], "correct": "British"},
  {"questionNumber": 2, "question": "10. Which war was fought between the North and South regions of the United States?", "options": ["Revolutionary War", "Civil War", "World War I", "Vietnam War"], "correct": "Civil War"},

  # questionNumber 3
  {"questionNumber": 3, "question": "1. When did the Renaissance begin approximately?", "options": ["11th century", "13th century", "14th century", "16th century"], "correct": "14th century"},
  {"questionNumber": 3, "question": "2. Who was a famous scientist during the Renaissance?", "options": ["Isaac Newton", "Leonardo da Vinci", "Galileo Galilei", "Albert Einstein"], "correct": "Leonardo da Vinci"},
  {"questionNumber": 3, "question": "3. When did the Ottoman Empire conquer Constantinople?", "options": ["1353", "1423", "1453", "1492"], "correct": "1453"},
  {"questionNumber": 3, "question": "4. Which empire was ruled by Genghis Khan?", "options": ["Roman", "Mongol", "Chinese", "Persian"], "correct": "Mongol"},
  {"questionNumber": 3, "question": "5. Who led the French Revolution?", "options": ["Robespierre", "Napoleon Bonaparte", "Louis XVI", "Voltaire"], "correct": "Robespierre"},
  {"questionNumber": 3, "question": "6. When did Napoleon Bonaparte become Emperor of France?", "options": ["1799", "1802", "1804", "1812"], "correct": "1804"},
  {"questionNumber": 3, "question": "7. Which treaty ended World War I?", "options": ["Treaty of Versailles", "Treaty of Sevres", "Treaty of Lausanne", "Treaty of Paris"], "correct": "Treaty of Versailles"},
  {"questionNumber": 3, "question": "8. Who was the first President of the United States?", "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"], "correct": "George Washington"},
  {"questionNumber": 3, "question": "9. Which Kazakh leader was known for his reforms in the 18th century?", "options": ["Abylai Khan", "Kenesary Kassymov", "Tauke Khan", "Kerey Khan"], "correct": "Tauke Khan"},
  {"questionNumber": 3, "question": "10. When was the first Constitution of Kazakhstan adopted?", "options": ["1991", "1993", "1995", "1998"], "correct": "1995"},

  # questionNumber 4
  {"questionNumber": 4, "question": "1. What was the capital of the Roman Empire?", "options": ["Athens", "Rome", "Carthage", "Byzantium"], "correct": "Rome"},
  {"questionNumber": 4, "question": "2. When did World War II end?", "options": ["1943", "1944", "1945", "1946"], "correct": "1945"},
  {"questionNumber": 4, "question": "3. Which Turkish leader introduced Latin alphabet reform?", "options": ["Atatürk", "İnönü", "Bayar", "Demirel"], "correct": "Atatürk"},
  {"questionNumber": 4, "question": "4. What was the ancient trade route connecting East and West?", "options": ["Amber Road", "Silk Road", "Spice Route", "Tea Route"], "correct": "Silk Road"},
  {"questionNumber": 4, "question": "5. Who was the first female Prime Minister of the UK?", "options": ["Elizabeth I", "Margaret Thatcher", "Theresa May", "Anne Boleyn"], "correct": "Margaret Thatcher"},
  {"questionNumber": 4, "question": "6. Which Kazakh city was once called Verny?", "options": ["Astana", "Semey", "Almaty", "Kyzylorda"], "correct": "Almaty"},
  {"questionNumber": 4, "question": "7. Who was the first man to step on the Moon?", "options": ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "Michael Collins"], "correct": "Neil Armstrong"},
  {"questionNumber": 4, "question": "8. When did the Ottoman Empire officially end?", "options": ["1918", "1920", "1922", "1923"], "correct": "1922"},
  {"questionNumber": 4, "question": "9. Who was known as the Iron Chancellor?", "options": ["Otto von Bismarck", "Napoleon III", "Winston Churchill", "Charles de Gaulle"], "correct": "Otto von Bismarck"},
  {"questionNumber": 4, "question": "10. When did the Cold War end?", "options": ["1985", "1989", "1990", "1991"], "correct": "1991"},

  # questionNumber 5
  {"questionNumber": 5, "question": "1. What was the name of the first human in space?", "options": ["Yuri Gagarin", "Neil Armstrong", "Alan Shepard", "John Glenn"], "correct": "Yuri Gagarin"},
  {"questionNumber": 5, "question": "2. Who was the famous Macedonian conqueror?", "options": ["Alexander the Great", "Caesar", "Cyrus the Great", "Darius"], "correct": "Alexander the Great"},
  {"questionNumber": 5, "question": "3. In which year did the Cuban Missile Crisis occur?", "options": ["1960", "1961", "1962", "1963"], "correct": "1962"},
  {"questionNumber": 5, "question": "4. What was the capital of the Ottoman Empire before Istanbul?", "options": ["Bursa", "Edirne", "Ankara", "Izmir"], "correct": "Bursa"},
  {"questionNumber": 5, "question": "5. When did the Kazakh Khanate form?", "options": ["1453", "1456", "1465", "1470"], "correct": "1465"},
  {"questionNumber": 5, "question": "6. Who invented the printing press?", "options": ["Galileo", "Johannes Gutenberg", "Isaac Newton", "Da Vinci"], "correct": "Johannes Gutenberg"},
  {"questionNumber": 5, "question": "7. Who was the U.S. president during the Civil War?", "options": ["George Washington", "Abraham Lincoln", "Andrew Johnson", "Theodore Roosevelt"], "correct": "Abraham Lincoln"},
  {"questionNumber": 5, "question": "8. When did Napoleon invade Russia?", "options": ["1805", "1810", "1812", "1815"], "correct": "1812"},
  {"questionNumber": 5, "question": "9. Which Kazakh poet wrote 'Kara Sozder'?", "options": ["Abai Kunanbayev", "Mukhtar Auezov", "Saken Seifullin", "Magzhan Zhumabayev"], "correct": "Abai Kunanbayev"},
  {"questionNumber": 5, "question": "10. Who founded the Mongol Empire?", "options": ["Kublai Khan", "Genghis Khan", "Tamerlane", "Batu Khan"], "correct": "Genghis Khan"},
 # questionNumber 6
  {"questionNumber": 6, "question": "1. When did the Industrial Revolution begin?", "options": ["16th century", "17th century", "18th century", "19th century"], "correct": "18th century"},
  {"questionNumber": 6, "question": "2. Who invented the telephone?", "options": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "James Watt"], "correct": "Alexander Graham Bell"},
  {"questionNumber": 6, "question": "3. Which Kazakh scientist developed important theories in chemistry?", "options": ["Kanysh Satpayev", "Abai Kunanbayev", "Al-Farabi", "Mukhtar Auezov"], "correct": "Kanysh Satpayev"},
  {"questionNumber": 6, "question": "4. When was the Declaration of Independence of the USA signed?", "options": ["1774", "1775", "1776", "1777"], "correct": "1776"},
  {"questionNumber": 6, "question": "5. Who was known as the ‘Father of the Turks’?", "options": ["Mustafa Kemal Atatürk", "Ismet Inönü", "Suleiman the Magnificent", "Celal Bayar"], "correct": "Mustafa Kemal Atatürk"},
  {"questionNumber": 6, "question": "6. When did Kazakhstan join the United Nations?", "options": ["1991", "1992", "1993", "1994"], "correct": "1992"},
  {"questionNumber": 6, "question": "7. What was the main cause of the American Civil War?", "options": ["Taxes", "Slavery", "Religion", "Trade"], "correct": "Slavery"},
  {"questionNumber": 6, "question": "8. Who painted the Mona Lisa?", "options": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Donatello"], "correct": "Leonardo da Vinci"},
  {"questionNumber": 6, "question": "9. When did the Soviet Union launch the first satellite, Sputnik 1?", "options": ["1955", "1957", "1959", "1961"], "correct": "1957"},
  {"questionNumber": 6, "question": "10. Who was the Kazakh leader during the transition from USSR to independence?", "options": ["Nursultan Nazarbayev", "Dinmukhamed Kunayev", "Kassym-Jomart Tokayev", "Bauyrzhan Momyshuly"], "correct": "Nursultan Nazarbayev"},

  # questionNumber 7
  {"questionNumber": 7, "question": "1. When did the French Revolution start?", "options": ["1787", "1788", "1789", "1790"], "correct": "1789"},
  {"questionNumber": 7, "question": "2. Who was the famous scientist who developed the theory of gravity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"], "correct": "Isaac Newton"},
  {"questionNumber": 7, "question": "3. When did the first man land on the Moon?", "options": ["1967", "1968", "1969", "1970"], "correct": "1969"},
  {"questionNumber": 7, "question": "4. Who was the Ottoman sultan during the conquest of Constantinople?", "options": ["Mehmed II", "Suleiman I", "Selim I", "Bayezid II"], "correct": "Mehmed II"},
  {"questionNumber": 7, "question": "5. When did Kazakhstan move its capital from Almaty to Astana?", "options": ["1995", "1997", "1998", "1999"], "correct": "1997"},
  {"questionNumber": 7, "question": "6. Who invented the light bulb?", "options": ["Alexander Graham Bell", "Thomas Edison", "James Watt", "Nikola Tesla"], "correct": "Thomas Edison"},
  {"questionNumber": 7, "question": "7. What year did the Titanic sink?", "options": ["1909", "1910", "1911", "1912"], "correct": "1912"},
  {"questionNumber": 7, "question": "8. Which Kazakh poet is known as the founder of modern Kazakh literature?", "options": ["Abai Kunanbayev", "Saken Seifullin", "Mukhtar Auezov", "Magzhan Zhumabayev"], "correct": "Abai Kunanbayev"},
  {"questionNumber": 7, "question": "9. Who was the British Prime Minister during World War II?", "options": ["Neville Chamberlain", "Winston Churchill", "Margaret Thatcher", "Tony Blair"], "correct": "Winston Churchill"},
  {"questionNumber": 7, "question": "10. When did the first World War end?", "options": ["1916", "1917", "1918", "1919"], "correct": "1918"},

  # questionNumber 8
  {"questionNumber": 8, "question": "1. When did Kazakhstan adopt the tenge as its national currency?", "options": ["1991", "1992", "1993", "1994"], "correct": "1993"},
  {"questionNumber": 8, "question": "2. Who was the famous Greek philosopher who taught Alexander the Great?", "options": ["Plato", "Socrates", "Aristotle", "Heraclitus"], "correct": "Aristotle"},
  {"questionNumber": 8, "question": "3. When did the Ottoman Empire reach its peak?", "options": ["15th century", "16th century", "17th century", "18th century"], "correct": "16th century"},
  {"questionNumber": 8, "question": "4. Who discovered penicillin?", "options": ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Joseph Lister"], "correct": "Alexander Fleming"},
  {"questionNumber": 8, "question": "5. When did the Berlin Wall get built?", "options": ["1958", "1960", "1961", "1963"], "correct": "1961"},
  {"questionNumber": 8, "question": "6. Which Kazakh writer wrote ‘The Path of Abai’?", "options": ["Mukhtar Auezov", "Abai Kunanbayev", "Sabit Mukanov", "Saken Seifullin"], "correct": "Mukhtar Auezov"},
  {"questionNumber": 8, "question": "7. When did World War II start for the Soviet Union?", "options": ["1939", "1940", "1941", "1942"], "correct": "1941"},
  {"questionNumber": 8, "question": "8. Who invented the airplane?", "options": ["Wright brothers", "Henry Ford", "Thomas Edison", "Nikola Tesla"], "correct": "Wright brothers"},
  {"questionNumber": 8, "question": "9. When was the European Union officially founded?", "options": ["1990", "1991", "1992", "1993"], "correct": "1993"},
  {"questionNumber": 8, "question": "10. Who was the Kazakh hero of the Great Patriotic War?", "options": ["Bauyrzhan Momyshuly", "Rakhymzhan Koshkarbaev", "Aliya Moldagulova", "All of them"], "correct": "All of them"},

  # questionNumber 9
  {"questionNumber": 9, "question": "1. When did the Renaissance end?", "options": ["15th century", "16th century", "17th century", "18th century"], "correct": "17th century"},
  {"questionNumber": 9, "question": "2. Who discovered America?", "options": ["Christopher Columbus", "Ferdinand Magellan", "Vasco da Gama", "James Cook"], "correct": "Christopher Columbus"},
  {"questionNumber": 9, "question": "3. When did the Soviet Union collapse?", "options": ["1989", "1990", "1991", "1992"], "correct": "1991"},
  {"questionNumber": 9, "question": "4. Who was the founder of the Mongol Empire?", "options": ["Batu Khan", "Kublai Khan", "Genghis Khan", "Tamerlane"], "correct": "Genghis Khan"},
  {"questionNumber": 9, "question": "5. When did the U.S. enter World War I?", "options": ["1915", "1916", "1917", "1918"], "correct": "1917"},
  {"questionNumber": 9, "question": "6. Who was the Kazakh educator and reformer executed in 1937?", "options": ["Ahmet Baitursynov", "Saken Seifullin", "Beimbet Maylin", "Magzhan Zhumabayev"], "correct": "Ahmet Baitursynov"},
  {"questionNumber": 9, "question": "7. When did the first Kazakh constitution come into force?", "options": ["1991", "1993", "1995", "1998"], "correct": "1995"},
  {"questionNumber": 9, "question": "8. Who was the leader of Nazi Germany?", "options": ["Hitler", "Mussolini", "Stalin", "Churchill"], "correct": "Hitler"},
  {"questionNumber": 9, "question": "9. When was NATO established?", "options": ["1947", "1948", "1949", "1950"], "correct": "1949"},
  {"questionNumber": 9, "question": "10. Who was the Kazakh composer of ‘Adai’ kuі?", "options": ["Kurmanğazy", "Dina Nurpeisova", "Abai", "Makhambet"], "correct": "Kurmanğazy"},

  # questionNumber 10
  {"questionNumber": 10, "question": "1. When did Kazakhstan host EXPO?", "options": ["2015", "2016", "2017", "2018"], "correct": "2017"},
  {"questionNumber": 10, "question": "2. Who was the founder of the Ottoman Empire?", "options": ["Osman I", "Orhan", "Suleiman", "Mehmed II"], "correct": "Osman I"},
  {"questionNumber": 10, "question": "3. When did the First Crusade begin?", "options": ["1095", "1100", "1110", "1120"], "correct": "1095"},
  {"questionNumber": 10, "question": "4. Who wrote the Declaration of Independence?", "options": ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"], "correct": "Thomas Jefferson"},
  {"questionNumber": 10, "question": "5. When did the Soviet Union send Yuri Gagarin to space?", "options": ["1959", "1960", "1961", "1962"], "correct": "1961"},
  {"questionNumber": 10, "question": "6. Which Kazakh city was renamed Astana in 1998?", "options": ["Akmola", "Kokshetau", "Karaganda", "Semey"], "correct": "Akmola"},
  {"questionNumber": 10, "question": "7. Who was the leader of the Russian Revolution of 1917?", "options": ["Lenin", "Stalin", "Trotsky", "Kerensky"], "correct": "Lenin"},
  {"questionNumber": 10, "question": "8. When was the Battle of Waterloo fought?", "options": ["1812", "1813", "1814", "1815"], "correct": "1815"},
  {"questionNumber": 10, "question": "9. Who was the first woman in space?", "options": ["Valentina Tereshkova", "Sally Ride", "Yuri Gagarin", "Laika"], "correct": "Valentina Tereshkova"},
  {"questionNumber": 10, "question": "10. When did Kazakhstan join the OSCE?", "options": ["1991", "1992", "1993", "1994"], "correct": "1992"}
],
"Science": [
  # questionNumber 1
  {"questionNumber": 1, "question": "1. What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "correct": "H2O"},
  {"questionNumber": 1, "question": "2. What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correct": "Mars"},
  {"questionNumber": 1, "question": "3. What gas do humans exhale?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "correct": "Carbon Dioxide"},
  {"questionNumber": 1, "question": "4. What is the center of an atom called?", "options": ["Electron", "Proton", "Nucleus", "Neutron"], "correct": "Nucleus"},
  {"questionNumber": 1, "question": "5. Which part of the plant makes food?", "options": ["Root", "Stem", "Leaf", "Flower"], "correct": "Leaf"},
  {"questionNumber": 1, "question": "6. What is the speed of light?", "options": ["3×10⁸ m/s", "3×10⁶ m/s", "1×10⁸ m/s", "5×10⁷ m/s"], "correct": "3×10⁸ m/s"},
  {"questionNumber": 1, "question": "7. What force keeps us on the ground?", "options": ["Friction", "Gravity", "Magnetism", "Inertia"], "correct": "Gravity"},
  {"questionNumber": 1, "question": "8. What is the boiling point of water?", "options": ["90°C", "95°C", "100°C", "110°C"], "correct": "100°C"},
  {"questionNumber": 1, "question": "9. What part of the human body pumps blood?", "options": ["Brain", "Lungs", "Heart", "Liver"], "correct": "Heart"},
  {"questionNumber": 1, "question": "10. What type of energy does a moving object have?", "options": ["Potential", "Thermal", "Kinetic", "Chemical"], "correct": "Kinetic"},

  # questionNumber 2
  {"questionNumber": 2, "question": "1. What gas do plants absorb during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Carbon Dioxide"},
  {"questionNumber": 2, "question": "2. Which planet is closest to the Sun?", "options": ["Venus", "Mercury", "Earth", "Mars"], "correct": "Mercury"},
  {"questionNumber": 2, "question": "3. What is the hardest natural substance on Earth?", "options": ["Iron", "Diamond", "Gold", "Quartz"], "correct": "Diamond"},
  {"questionNumber": 2, "question": "4. Which part of the cell controls its activities?", "options": ["Nucleus", "Cytoplasm", "Membrane", "Vacuole"], "correct": "Nucleus"},
  {"questionNumber": 2, "question": "5. What is measured in Newtons?", "options": ["Force", "Energy", "Speed", "Mass"], "correct": "Force"},
  {"questionNumber": 2, "question": "6. What is the main gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Nitrogen"},
  {"questionNumber": 2, "question": "7. What type of energy is stored in food?", "options": ["Thermal", "Kinetic", "Chemical", "Electrical"], "correct": "Chemical"},
  {"questionNumber": 2, "question": "8. What instrument measures temperature?", "options": ["Barometer", "Thermometer", "Hygrometer", "Anemometer"], "correct": "Thermometer"},
  {"questionNumber": 2, "question": "9. Which blood cells help fight infection?", "options": ["Red cells", "White cells", "Platelets", "Plasma"], "correct": "White cells"},
  {"questionNumber": 2, "question": "10. What is the main source of energy for Earth?", "options": ["Wind", "Sun", "Water", "Geothermal"], "correct": "Sun"},
  # questionNumber 3
  {"questionNumber": 3, "question": "1. What is the largest planet in our Solar System?", "options": ["Earth", "Saturn", "Jupiter", "Neptune"], "correct": "Jupiter"},
  {"questionNumber": 3, "question": "2. What part of the human body controls movement and balance?", "options": ["Cerebrum", "Cerebellum", "Brainstem", "Spinal cord"], "correct": "Cerebellum"},
  {"questionNumber": 3, "question": "3. What is the chemical symbol for gold?", "options": ["G", "Ag", "Au", "Go"], "correct": "Au"},
  {"questionNumber": 3, "question": "4. What phenomenon causes rainbows?", "options": ["Reflection", "Refraction", "Diffraction", "Dispersion"], "correct": "Dispersion"},
  {"questionNumber": 3, "question": "5. What is the process by which liquid water changes to vapor?", "options": ["Condensation", "Freezing", "Evaporation", "Melting"], "correct": "Evaporation"},
  {"questionNumber": 3, "question": "6. What gas do humans need to survive?", "options": ["Carbon Dioxide", "Nitrogen", "Oxygen", "Hydrogen"], "correct": "Oxygen"},
  {"questionNumber": 3, "question": "7. What is the unit of electrical current?", "options": ["Volt", "Ampere", "Ohm", "Watt"], "correct": "Ampere"},
  {"questionNumber": 3, "question": "8. What type of blood cells carry oxygen?", "options": ["Red cells", "White cells", "Platelets", "Plasma"], "correct": "Red cells"},
  {"questionNumber": 3, "question": "9. Which organ in the body filters blood?", "options": ["Heart", "Kidneys", "Lungs", "Liver"], "correct": "Kidneys"},
  {"questionNumber": 3, "question": "10. What is the main organ of the nervous system?", "options": ["Heart", "Brain", "Lungs", "Liver"], "correct": "Brain"},

  # questionNumber 4
  {"questionNumber": 4, "question": "1. What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"], "correct": "Mitochondria"},
  {"questionNumber": 4, "question": "2. What planet has the most moons?", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "correct": "Saturn"},
  {"questionNumber": 4, "question": "3. What is the process by which plants make their food?", "options": ["Respiration", "Photosynthesis", "Fermentation", "Transpiration"], "correct": "Photosynthesis"},
  {"questionNumber": 4, "question": "4. What is the study of living organisms called?", "options": ["Physics", "Chemistry", "Biology", "Astronomy"], "correct": "Biology"},
  {"questionNumber": 4, "question": "5. What part of the human eye controls the amount of light entering?", "options": ["Pupil", "Iris", "Lens", "Cornea"], "correct": "Iris"},
  {"questionNumber": 4, "question": "6. Which vitamin is produced by the skin in sunlight?", "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin E"], "correct": "Vitamin D"},
  {"questionNumber": 4, "question": "7. What is the smallest unit of matter?", "options": ["Molecule", "Atom", "Proton", "Cell"], "correct": "Atom"},
  {"questionNumber": 4, "question": "8. What part of the plant absorbs water?", "options": ["Stem", "Root", "Leaf", "Flower"], "correct": "Root"},
  {"questionNumber": 4, "question": "9. What is the process by which ice turns directly into vapor?", "options": ["Condensation", "Sublimation", "Evaporation", "Melting"], "correct": "Sublimation"},
  {"questionNumber": 4, "question": "10. What is the closest star to Earth?", "options": ["Sirius", "Alpha Centauri", "Sun", "Proxima Centauri"], "correct": "Sun"},

  # questionNumber 5
  {"questionNumber": 5, "question": "1. What is Newton’s third law of motion?", "options": ["F=ma", "For every action, there is an equal and opposite reaction", "Energy cannot be created or destroyed", "An object at rest stays at rest"], "correct": "For every action, there is an equal and opposite reaction"},
  {"questionNumber": 5, "question": "2. What type of blood does the universal donor have?", "options": ["A", "B", "AB", "O negative"], "correct": "O negative"},
  {"questionNumber": 5, "question": "3. What is the main function of red blood cells?", "options": ["Fight infection", "Carry oxygen", "Produce hormones", "Store nutrients"], "correct": "Carry oxygen"},
  {"questionNumber": 5, "question": "4. Which element is necessary for respiration?", "options": ["Hydrogen", "Oxygen", "Nitrogen", "Helium"], "correct": "Oxygen"},
  {"questionNumber": 5, "question": "5. What is the SI unit of power?", "options": ["Volt", "Newton", "Watt", "Joule"], "correct": "Watt"},
  {"questionNumber": 5, "question": "6. Which part of the brain controls breathing?", "options": ["Cerebrum", "Cerebellum", "Medulla Oblongata", "Hippocampus"], "correct": "Medulla Oblongata"},
  {"questionNumber": 5, "question": "7. What is the most abundant element in the universe?", "options": ["Oxygen", "Hydrogen", "Carbon", "Helium"], "correct": "Hydrogen"},
  {"questionNumber": 5, "question": "8. What process do living organisms use to release energy from food?", "options": ["Photosynthesis", "Respiration", "Fermentation", "Transpiration"], "correct": "Respiration"},
  {"questionNumber": 5, "question": "9. Which metal is liquid at room temperature?", "options": ["Mercury", "Iron", "Sodium", "Lead"], "correct": "Mercury"},
  {"questionNumber": 5, "question": "10. What is the main gas responsible for the greenhouse effect?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "correct": "Carbon Dioxide"},
  # questionNumber 6
  {"questionNumber": 6, "question": "1. What is the main function of red blood cells?", "options": ["Fight infection", "Carry oxygen", "Digest food", "Transport hormones"], "correct": "Carry oxygen"},
  {"questionNumber": 6, "question": "2. Which vitamin is produced when skin is exposed to sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "correct": "Vitamin D"},
  {"questionNumber": 6, "question": "3. What is the center of the Solar System?", "options": ["Earth", "Sun", "Moon", "Jupiter"], "correct": "Sun"},
  {"questionNumber": 6, "question": "4. What process converts sugar into energy in cells?", "options": ["Respiration", "Photosynthesis", "Fermentation", "Osmosis"], "correct": "Respiration"},
  {"questionNumber": 6, "question": "5. What type of energy is stored in food?", "options": ["Thermal", "Chemical", "Kinetic", "Potential"], "correct": "Chemical"},
  {"questionNumber": 6, "question": "6. What part of the cell contains genetic material?", "options": ["Cytoplasm", "Nucleus", "Cell wall", "Ribosome"], "correct": "Nucleus"},
  {"questionNumber": 6, "question": "7. What is the main gas responsible for global warming?", "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"], "correct": "Carbon Dioxide"},
  {"questionNumber": 6, "question": "8. What is H2SO4 commonly known as?", "options": ["Nitric acid", "Sulfuric acid", "Hydrochloric acid", "Acetic acid"], "correct": "Sulfuric acid"},
  {"questionNumber": 6, "question": "9. What is the most abundant element in the universe?", "options": ["Helium", "Oxygen", "Hydrogen", "Carbon"], "correct": "Hydrogen"},
  {"questionNumber": 6, "question": "10. What instrument measures atmospheric pressure?", "options": ["Thermometer", "Barometer", "Anemometer", "Hygrometer"], "correct": "Barometer"},

  # questionNumber 7
  {"questionNumber": 7, "question": "1. What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "1,000 km/s", "3,000 km/s"], "correct": "300,000 km/s"},
  {"questionNumber": 7, "question": "2. What organ filters blood in the human body?", "options": ["Liver", "Heart", "Kidneys", "Lungs"], "correct": "Kidneys"},
  {"questionNumber": 7, "question": "3. Which metal is liquid at room temperature?", "options": ["Mercury", "Iron", "Sodium", "Zinc"], "correct": "Mercury"},
  {"questionNumber": 7, "question": "4. Which planet is known for its Great Red Spot?", "options": ["Earth", "Saturn", "Jupiter", "Mars"], "correct": "Jupiter"},
  {"questionNumber": 7, "question": "5. What is the chemical symbol for gold?", "options": ["Ag", "Au", "Pb", "Fe"], "correct": "Au"},
  {"questionNumber": 7, "question": "6. What is the smallest unit of life?", "options": ["Atom", "Molecule", "Cell", "Organ"], "correct": "Cell"},
  {"questionNumber": 7, "question": "7. What is the process by which plants lose water through leaves?", "options": ["Photosynthesis", "Transpiration", "Condensation", "Evaporation"], "correct": "Transpiration"},
  {"questionNumber": 7, "question": "8. What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Chloroplast", "Ribosome"], "correct": "Mitochondria"},
  {"questionNumber": 7, "question": "9. What is the freezing point of water?", "options": ["-5°C", "0°C", "10°C", "32°C"], "correct": "0°C"},
  {"questionNumber": 7, "question": "10. What is Earth's primary source of energy?", "options": ["Coal", "Wind", "Sun", "Nuclear"], "correct": "Sun"},

  # questionNumber 8
  {"questionNumber": 8, "question": "1. Which blood type is known as the universal donor?", "options": ["A", "B", "O", "AB"], "correct": "O"},
  {"questionNumber": 8, "question": "2. What part of the plant absorbs water and minerals?", "options": ["Stem", "Root", "Leaf", "Flower"], "correct": "Root"},
  {"questionNumber": 8, "question": "3. What natural phenomenon is measured by the Richter scale?", "options": ["Hurricanes", "Earthquakes", "Floods", "Volcanoes"], "correct": "Earthquakes"},
  {"questionNumber": 8, "question": "4. What is the most common gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Nitrogen"},
  {"questionNumber": 8, "question": "5. What part of the human body produces insulin?", "options": ["Liver", "Pancreas", "Kidneys", "Heart"], "correct": "Pancreas"},
  {"questionNumber": 8, "question": "6. What is the main source of energy for photosynthesis?", "options": ["Soil", "Water", "Sunlight", "Oxygen"], "correct": "Sunlight"},
  {"questionNumber": 8, "question": "7. What is the study of living organisms called?", "options": ["Geology", "Biology", "Chemistry", "Physics"], "correct": "Biology"},
  {"questionNumber": 8, "question": "8. Which planet has the most moons?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "correct": "Saturn"},
  {"questionNumber": 8, "question": "9. What is the largest organ of the human body?", "options": ["Liver", "Brain", "Skin", "Heart"], "correct": "Skin"},
  {"questionNumber": 8, "question": "10. What scientist proposed the three laws of motion?", "options": ["Einstein", "Newton", "Galileo", "Kepler"], "correct": "Newton"},

  # questionNumber 9
  {"questionNumber": 9, "question": "1. What is the main component of the Sun?", "options": ["Oxygen", "Hydrogen", "Helium", "Carbon"], "correct": "Hydrogen"},
  {"questionNumber": 9, "question": "2. Which planet is called Earth’s twin?", "options": ["Mars", "Venus", "Mercury", "Jupiter"], "correct": "Venus"},
  {"questionNumber": 9, "question": "3. What part of the eye controls the amount of light entering?", "options": ["Retina", "Cornea", "Pupil", "Lens"], "correct": "Pupil"},
  {"questionNumber": 9, "question": "4. Which element has the symbol O?", "options": ["Osmium", "Oxygen", "Oganesson", "Oxide"], "correct": "Oxygen"},
  {"questionNumber": 9, "question": "5. What is measured in ohms?", "options": ["Current", "Voltage", "Resistance", "Power"], "correct": "Resistance"},
  {"questionNumber": 9, "question": "6. What type of energy is associated with moving objects?", "options": ["Potential", "Kinetic", "Chemical", "Thermal"], "correct": "Kinetic"},
  {"questionNumber": 9, "question": "7. What organ helps maintain body balance?", "options": ["Heart", "Lungs", "Inner ear", "Liver"], "correct": "Inner ear"},
  {"questionNumber": 9, "question": "8. What is the main function of chlorophyll?", "options": ["Absorb sunlight", "Store water", "Support plant", "Transport minerals"], "correct": "Absorb sunlight"},
  {"questionNumber": 9, "question": "9. What planet has the largest volcano?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "correct": "Mars"},
  {"questionNumber": 9, "question": "10. Which metal is used in batteries?", "options": ["Zinc", "Lead", "Lithium", "Copper"], "correct": "Lithium"},

  # questionNumber 10
  {"questionNumber": 10, "question": "1. What is the chemical symbol for sodium?", "options": ["S", "Na", "N", "Sn"], "correct": "Na"},
  {"questionNumber": 10, "question": "2. Which scientist discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Isaac Newton"], "correct": "Alexander Fleming"},
  {"questionNumber": 10, "question": "3. What is the main function of white blood cells?", "options": ["Clot blood", "Fight infection", "Carry oxygen", "Transport nutrients"], "correct": "Fight infection"},
  {"questionNumber": 10, "question": "4. What planet is farthest from the Sun?", "options": ["Neptune", "Uranus", "Saturn", "Pluto"], "correct": "Neptune"},
  {"questionNumber": 10, "question": "5. What is the most common element in the human body?", "options": ["Carbon", "Hydrogen", "Oxygen", "Nitrogen"], "correct": "Oxygen"},
  {"questionNumber": 10, "question": "6. What part of the brain controls breathing?", "options": ["Cerebrum", "Cerebellum", "Medulla Oblongata", "Hypothalamus"], "correct": "Medulla Oblongata"},
  {"questionNumber": 10, "question": "7. What is the SI unit of force?", "options": ["Watt", "Newton", "Pascal", "Joule"], "correct": "Newton"},
  {"questionNumber": 10, "question": "8. What is the process by which liquids change to gas?", "options": ["Condensation", "Evaporation", "Freezing", "Melting"], "correct": "Evaporation"},
  {"questionNumber": 10, "question": "9. What part of an atom has a positive charge?", "options": ["Electron", "Neutron", "Proton", "Nucleus"], "correct": "Proton"},
  {"questionNumber": 10, "question": "10. What is the main gas used in balloons?", "options": ["Oxygen", "Helium", "Hydrogen", "Nitrogen"], "correct": "Helium"},
],
"Geography": [
  # questionNumber 1
  {"questionNumber": 1, "question": "1. What is the largest continent on Earth?", "options": ["Africa", "Asia", "Europe", "North America"], "correct": "Asia"},
  {"questionNumber": 1, "question": "2. Which ocean is the deepest?", "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "correct": "Pacific Ocean"},
  {"questionNumber": 1, "question": "3. What is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct": "Nile"},
  {"questionNumber": 1, "question": "4. Which country has the largest population?", "options": ["India", "China", "USA", "Indonesia"], "correct": "China"},
  {"questionNumber": 1, "question": "5. What is the capital city of Kazakhstan?", "options": ["Almaty", "Astana", "Shymkent", "Atyrau"], "correct": "Astana"},
  {"questionNumber": 1, "question": "6. Which desert is the largest in the world?", "options": ["Gobi", "Sahara", "Arabian", "Kalahari"], "correct": "Sahara"},
  {"questionNumber": 1, "question": "7. What mountain range separates Europe and Asia?", "options": ["Himalayas", "Alps", "Ural Mountains", "Andes"], "correct": "Ural Mountains"},
  {"questionNumber": 1, "question": "8. What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"], "correct": "Vatican City"},
  {"questionNumber": 1, "question": "9. What ocean surrounds Japan?", "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "correct": "Pacific Ocean"},
  {"questionNumber": 1, "question": "10. Which country is known as the ‘Land of a Thousand Lakes’?", "options": ["Norway", "Finland", "Canada", "Sweden"], "correct": "Finland"},

  # questionNumber 2
  {"questionNumber": 2, "question": "1. What is the longest mountain range in the world?", "options": ["Rockies", "Andes", "Himalayas", "Alps"], "correct": "Andes"},
  {"questionNumber": 2, "question": "2. Which continent has the most countries?", "options": ["Europe", "Asia", "Africa", "South America"], "correct": "Africa"},
  {"questionNumber": 2, "question": "3. What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"], "correct": "Ottawa"},
  {"questionNumber": 2, "question": "4. Which river flows through Paris?", "options": ["Thames", "Danube", "Seine", "Rhine"], "correct": "Seine"},
  {"questionNumber": 2, "question": "5. What is the largest island in the world?", "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"], "correct": "Greenland"},
  {"questionNumber": 2, "question": "6. What is the highest mountain in the world?", "options": ["K2", "Everest", "Kangchenjunga", "Lhotse"], "correct": "Everest"},
  {"questionNumber": 2, "question": "7. Which sea is the saltiest?", "options": ["Dead Sea", "Caspian Sea", "Black Sea", "Red Sea"], "correct": "Dead Sea"},
  {"questionNumber": 2, "question": "8. What is the capital of Japan?", "options": ["Osaka", "Tokyo", "Kyoto", "Nagoya"], "correct": "Tokyo"},
  {"questionNumber": 2, "question": "9. Which country has the longest coastline?", "options": ["Australia", "Canada", "Russia", "Indonesia"], "correct": "Canada"},
  {"questionNumber": 2, "question": "10. What river runs through Egypt?", "options": ["Amazon", "Nile", "Tigris", "Euphrates"], "correct": "Nile"},

  # questionNumber 3
  {"questionNumber": 3, "question": "1. What is the largest lake in the world by area?", "options": ["Caspian Sea", "Lake Superior", "Lake Victoria", "Lake Baikal"], "correct": "Caspian Sea"},
  {"questionNumber": 3, "question": "2. Which desert covers most of northern Africa?", "options": ["Sahara", "Gobi", "Kalahari", "Namib"], "correct": "Sahara"},
  {"questionNumber": 3, "question": "3. What is the capital of France?", "options": ["Berlin", "Rome", "Madrid", "Paris"], "correct": "Paris"},
  {"questionNumber": 3, "question": "4. Which continent is known as the ‘Dark Continent’?", "options": ["Asia", "Africa", "South America", "Europe"], "correct": "Africa"},
  {"questionNumber": 3, "question": "5. What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "correct": "Canberra"},
  {"questionNumber": 3, "question": "6. Which country is home to the Amazon rainforest?", "options": ["Peru", "Brazil", "Colombia", "Venezuela"], "correct": "Brazil"},
  {"questionNumber": 3, "question": "7. What is the capital of Russia?", "options": ["St. Petersburg", "Moscow", "Kazan", "Novosibirsk"], "correct": "Moscow"},
  {"questionNumber": 3, "question": "8. Which continent is completely in the Southern Hemisphere?", "options": ["Australia", "Africa", "South America", "Antarctica"], "correct": "Antarctica"},
  {"questionNumber": 3, "question": "9. What river flows through London?", "options": ["Thames", "Seine", "Danube", "Elbe"], "correct": "Thames"},
  {"questionNumber": 3, "question": "10. What is the capital city of Turkey?", "options": ["Istanbul", "Ankara", "Izmir", "Bursa"], "correct": "Ankara"},
  # questionNumber 4
  {"questionNumber": 4, "question": "1. What is the largest country in the world by area?", "options": ["USA", "China", "Russia", "Canada"], "correct": "Russia"},
  {"questionNumber": 4, "question": "2. Which sea borders Kazakhstan to the west?", "options": ["Caspian Sea", "Black Sea", "Aral Sea", "Baltic Sea"], "correct": "Caspian Sea"},
  {"questionNumber": 4, "question": "3. Which continent has the highest population density?", "options": ["Europe", "Asia", "Africa", "South America"], "correct": "Asia"},
  {"questionNumber": 4, "question": "4. Which volcano erupted in 1883 causing one of the largest recorded explosions?", "options": ["Krakatoa", "Vesuvius", "Etna", "Mount Fuji"], "correct": "Krakatoa"},
  {"questionNumber": 4, "question": "5. What is the capital of Kazakhstan?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Astana"},
  {"questionNumber": 4, "question": "6. Which river is the longest in Kazakhstan?", "options": ["Ili", "Irtysh", "Ural", "Syr Darya"], "correct": "Irtysh"},
  {"questionNumber": 4, "question": "7. Which desert is located in southern Kazakhstan?", "options": ["Kyzylkum", "Gobi", "Karakum", "Sahara"], "correct": "Kyzylkum"},
  {"questionNumber": 4, "question": "8. Which mountain range is in eastern Kazakhstan?", "options": ["Altai", "Tian Shan", "Himalayas", "Ural"], "correct": "Altai"},
  {"questionNumber": 4, "question": "9. Which body of water is shrinking due to irrigation and climate change?", "options": ["Caspian Sea", "Aral Sea", "Black Sea", "Dead Sea"], "correct": "Aral Sea"},
  {"questionNumber": 4, "question": "10. What is the largest city in Kazakhstan by population?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Almaty"},

  # questionNumber 5
  {"questionNumber": 5, "question": "1. Which country has the most natural lakes?", "options": ["Canada", "Finland", "Russia", "USA"], "correct": "Canada"},
  {"questionNumber": 5, "question": "2. Which river forms part of the border between Kazakhstan and Russia?", "options": ["Ural", "Ili", "Irtysh", "Syr Darya"], "correct": "Ural"},
  {"questionNumber": 5, "question": "3. What is the name of the peninsula that separates the Black Sea from the Sea of Azov?", "options": ["Crimea", "Balkan", "Scandinavia", "Iberian"], "correct": "Crimea"},
  {"questionNumber": 5, "question": "4. Which plateau covers much of central Kazakhstan?", "options": ["Kazakh Uplands", "Deccan Plateau", "Colorado Plateau", "Tibetan Plateau"], "correct": "Kazakh Uplands"},
  {"questionNumber": 5, "question": "5. Which strait connects the Black Sea and the Sea of Marmara?", "options": ["Bosphorus", "Dardanelles", "Malacca", "Magellan"], "correct": "Bosphorus"},
  {"questionNumber": 5, "question": "6. Which country contains the most volcanoes?", "options": ["Japan", "Indonesia", "USA", "Russia"], "correct": "Indonesia"},
  {"questionNumber": 5, "question": "7. What is the northernmost capital city in the world?", "options": ["Reykjavik", "Oslo", "Helsinki", "Stockholm"], "correct": "Reykjavik"},
  {"questionNumber": 5, "question": "8. Which river flows through Almaty?", "options": ["Ili", "Syr Darya", "Irtysh", "Ural"], "correct": "Ili"},
  {"questionNumber": 5, "question": "9. What is the largest desert in Kazakhstan?", "options": ["Kyzylkum", "Betpak-Dala", "Karakum", "Sahara"], "correct": "Betpak-Dala"},
  {"questionNumber": 5, "question": "10. Which mountain is the highest in Kazakhstan?", "options": ["Khan Tengri", "Belukha", "Mount Elbrus", "Mount Ararat"], "correct": "Khan Tengri"},
# questionNumber 6
{"questionNumber": 6, "question": "1. Which river is considered the longest in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct": "Nile"},
{"questionNumber": 6, "question": "2. Which Kazakh city is famous for its Charyn Canyon?", "options": ["Almaty", "Astana", "Shymkent", "Aktau"], "correct": "Almaty"},
{"questionNumber": 6, "question": "3. Which ocean is the largest?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "correct": "Pacific"},
{"questionNumber": 6, "question": "4. What is the southernmost country in Africa?", "options": ["South Africa", "Namibia", "Botswana", "Zimbabwe"], "correct": "South Africa"},
{"questionNumber": 6, "question": "5. Which lake is the largest in Kazakhstan?", "options": ["Lake Balkhash", "Caspian Sea", "Aral Sea", "Lake Zaysan"], "correct": "Lake Balkhash"},
{"questionNumber": 6, "question": "6. What is the deepest ocean trench?", "options": ["Mariana Trench", "Tonga Trench", "Java Trench", "Kuril Trench"], "correct": "Mariana Trench"},
{"questionNumber": 6, "question": "7. Which desert is located in western Kazakhstan?", "options": ["Karakum", "Betpak-Dala", "Kyzylkum", "Sahara"], "correct": "Karakum"},
{"questionNumber": 6, "question": "8. What is the highest peak in Central Asia?", "options": ["Pik Pobeda", "Khan Tengri", "Belukha", "Peak Lenin"], "correct": "Pik Pobeda"},
{"questionNumber": 6, "question": "9. Which river flows into the Aral Sea?", "options": ["Amu Darya", "Syr Darya", "Ural", "Ili"], "correct": "Syr Darya"},
{"questionNumber": 6, "question": "10. Which strait connects the Pacific and Arctic Oceans?", "options": ["Bering Strait", "Malacca Strait", "Bosporus", "Magellan"], "correct": "Bering Strait"},

# questionNumber 7
{"questionNumber": 7, "question": "1. What is the largest island in the world?", "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"], "correct": "Greenland"},
{"questionNumber": 7, "question": "2. Which Kazakh mountain range is part of the Tian Shan?", "options": ["Altai", "Dzungarian Alatau", "Zailiysky Alatau", "Karkaraly"], "correct": "Zailiysky Alatau"},
{"questionNumber": 7, "question": "3. Which country has the most time zones?", "options": ["Russia", "USA", "China", "Canada"], "correct": "Russia"},
{"questionNumber": 7, "question": "4. Which desert lies on the border of Kazakhstan and Uzbekistan?", "options": ["Kyzylkum", "Gobi", "Karakum", "Betpak-Dala"], "correct": "Kyzylkum"},
{"questionNumber": 7, "question": "5. Which Kazakh river flows into Lake Balkhash?", "options": ["Ili", "Syr Darya", "Ural", "Emba"], "correct": "Ili"},
{"questionNumber": 7, "question": "6. Which plateau is in western Kazakhstan?", "options": ["Ustyurt Plateau", "Kazakh Uplands", "Tian Shan", "Altai"], "correct": "Ustyurt Plateau"},
{"questionNumber": 7, "question": "7. What is the longest mountain range in the world?", "options": ["Andes", "Himalayas", "Rockies", "Alps"], "correct": "Andes"},
{"questionNumber": 7, "question": "8. Which Kazakh city is closest to the Aral Sea?", "options": ["Aktobe", "Kyzylorda", "Shymkent", "Oral"], "correct": "Kyzylorda"},
{"questionNumber": 7, "question": "9. Which river forms part of the border between Kazakhstan and China?", "options": ["Ili", "Irtysh", "Ural", "Syr Darya"], "correct": "Ili"},
{"questionNumber": 7, "question": "10. Which sea is almost entirely enclosed by land?", "options": ["Caspian Sea", "Black Sea", "Aral Sea", "Baltic Sea"], "correct": "Caspian Sea"},

# questionNumber 8
{"questionNumber": 8, "question": "1. Which country has the largest number of islands?", "options": ["Indonesia", "Canada", "Philippines", "Japan"], "correct": "Sweden"},
{"questionNumber": 8, "question": "2. Which river passes through Astana?", "options": ["Ishim", "Ili", "Irtysh", "Syr Darya"], "correct": "Ishim"},
{"questionNumber": 8, "question": "3. Which is the smallest continent by area?", "options": ["Europe", "Australia", "Antarctica", "South America"], "correct": "Australia"},
{"questionNumber": 8, "question": "4. What is the climate of southern Kazakhstan?", "options": ["Tropical", "Continental", "Mediterranean", "Arctic"], "correct": "Continental"},
{"questionNumber": 8, "question": "5. Which Kazakh city is a major oil center?", "options": ["Atyrau", "Almaty", "Astana", "Karaganda"], "correct": "Atyrau"},
{"questionNumber": 8, "question": "6. What is the highest waterfall in the world?", "options": ["Niagara Falls", "Angel Falls", "Victoria Falls", "Iguazu Falls"], "correct": "Angel Falls"},
{"questionNumber": 8, "question": "7. Which ocean touches the eastern coast of Africa?", "options": ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"], "correct": "Indian Ocean"},
{"questionNumber": 8, "question": "8. Which Kazakh city is located near the Altai Mountains?", "options": ["Ust-Kamenogorsk", "Almaty", "Astana", "Aktobe"], "correct": "Ust-Kamenogorsk"},
{"questionNumber": 8, "question": "9. What is the longest river in Russia?", "options": ["Volga", "Ob", "Lena", "Yenisei"], "correct": "Lena"},
{"questionNumber": 8, "question": "10. Which peninsula is in the north of Kazakhstan?", "options": ["Mangyshlak", "Emba", "Ustyurt", "Saryarka"], "correct": "Mangyshlak"},

# questionNumber 9
{"questionNumber": 9, "question": "1. Which Kazakh lake has both freshwater and saltwater parts?", "options": ["Lake Balkhash", "Lake Zaysan", "Caspian Sea", "Aral Sea"], "correct": "Lake Balkhash"},
{"questionNumber": 9, "question": "2. Which desert in Kazakhstan is considered semi-arid?", "options": ["Betpak-Dala", "Kyzylkum", "Karakum", "Gobi"], "correct": "Betpak-Dala"},
{"questionNumber": 9, "question": "3. Which mountain range is on the border of Kazakhstan and China?", "options": ["Tien Shan", "Altai", "Ural", "Himalayas"], "correct": "Tien Shan"},
{"questionNumber": 9, "question": "4. Which Kazakh river flows into the Caspian Sea?", "options": ["Ural", "Ili", "Syr Darya", "Irtysh"], "correct": "Ural"},
{"questionNumber": 9, "question": "5. Which city is the southernmost in Kazakhstan?", "options": ["Shymkent", "Taraz", "Almaty", "Aktau"], "correct": "Shymkent"},
{"questionNumber": 9, "question": "6. What is the largest island in Kazakhstan?", "options": ["Barsa-Kelmes", "Kokaral", "Komsomol", "Vladimir"], "correct": "Barsa-Kelmes"},
{"questionNumber": 9, "question": "7. Which Kazakh mountain peak exceeds 7000 meters?", "options": ["Khan Tengri", "Belukha", "Pik Pobeda", "Peak Lenin"], "correct": "Khan Tengri"},
{"questionNumber": 9, "question": "8. Which is the coldest inhabited city in Kazakhstan?", "options": ["Petropavl", "Astana", "Karaganda", "Oskemen"], "correct": "Oskemen"},
{"questionNumber": 9, "question": "9. Which desert stretches into Uzbekistan from Kazakhstan?", "options": ["Kyzylkum", "Betpak-Dala", "Karakum", "Gobi"], "correct": "Kyzylkum"},
{"questionNumber": 9, "question": "10. Which Kazakh city lies on the Irtysh River?", "options": ["Pavlodar", "Semey", "Ust-Kamenogorsk", "Aktobe"], "correct": "Pavlodar"},

# questionNumber 10
{"questionNumber": 10, "question": "1. What is the largest steppe in Kazakhstan?", "options": ["Kazakh Steppe", "Ili Steppe", "Ustyurt Steppe", "Betpak-Dala"], "correct": "Kazakh Steppe"},
{"questionNumber": 10, "question": "2. Which river is important for irrigation in southern Kazakhstan?", "options": ["Syr Darya", "Ili", "Ural", "Irtysh"], "correct": "Syr Darya"},
{"questionNumber": 10, "question": "3. Which Kazakh lake is rapidly shrinking due to water diversion?", "options": ["Aral Sea", "Balkhash", "Zaysan", "Alakol"], "correct": "Aral Sea"},
{"questionNumber": 10, "question": "4. Which mountain range separates Kazakhstan from Kyrgyzstan?", "options": ["Tien Shan", "Altai", "Zailiysky Alatau", "Ural"], "correct": "Tien Shan"},
{"questionNumber": 10, "question": "5. Which sea is west of Kazakhstan?", "options": ["Caspian Sea", "Aral Sea", "Black Sea", "Baltic Sea"], "correct": "Caspian Sea"},
{"questionNumber": 10, "question": "6. What is the largest plateau in Kazakhstan?", "options": ["Ustyurt Plateau", "Kazakh Uplands", "Altai Plateau", "Betpak-Dala Plateau"], "correct": "Kazakh Uplands"},
{"questionNumber": 10, "question": "7. Which city in Kazakhstan is a former capital of the Kazakh SSR?", "options": ["Almaty", "Astana", "Semey", "Karaganda"], "correct": "Almaty"},
{"questionNumber": 10, "question": "8. Which Kazakh river forms part of the border with China?", "options": ["Ili", "Irtysh", "Syr Darya", "Ural"], "correct": "Ili"},
{"questionNumber": 10, "question": "9. Which mountain is considered sacred in Kazakhstan?", "options": ["Kok-Tobe", "Khan Tengri", "Mount Aral", "Belukha"], "correct": "Khan Tengri"},
{"questionNumber": 9, "question": "9. Which desert stretches into Uzbekistan from Kazakhstan?", "options": ["Kyzylkum", "Betpak-Dala", "Karakum", "Gobi"], "correct": "Kyzylkum"},
],
"Technology": [

  # questionNumber 1
  {"questionNumber": 1, "question": "1. Who is known as the father of computers?", "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"], "correct": "Charles Babbage"},
  {"questionNumber": 1, "question": "2. What does CPU stand for?", "options": ["Central Processing Unit", "Computer Primary Unit", "Control Processing Unit", "Central Peripheral Unit"], "correct": "Central Processing Unit"},
  {"questionNumber": 1, "question": "3. Which company created the first smartphone?", "options": ["Apple", "IBM", "Samsung", "Nokia"], "correct": "IBM"},
  {"questionNumber": 1, "question": "4. What year was the Internet made publicly available?", "options": ["1985", "1989", "1991", "1995"], "correct": "1991"},
  {"questionNumber": 1, "question": "5. Who founded Microsoft?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"], "correct": "Bill Gates"},
  {"questionNumber": 1, "question": "6. What is the first Kazakh IT company?", "options": ["Kcell", "KazTech Innovations", "Beeline", "Astana IT"], "correct": "KazTech Innovations"},
  {"questionNumber": 1, "question": "7. Which programming language is used for AI the most?", "options": ["Python", "C++", "Java", "PHP"], "correct": "Python"},
  {"questionNumber": 1, "question": "8. What does RAM stand for?", "options": ["Random Access Memory", "Read Access Memory", "Rapid Access Memory", "Run All Memory"], "correct": "Random Access Memory"},
  {"questionNumber": 1, "question": "9. What is considered the first computer virus?", "options": ["Creeper", "ILOVEYOU", "Melissa", "Code Red"], "correct": "Creeper"},
  {"questionNumber": 1, "question": "10. Which Kazakh city has the largest tech park?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},

  # questionNumber 2
  {"questionNumber": 2, "question": "1. What is the main function of an operating system?", "options": ["Manage software", "Run applications", "Manage hardware and software", "Store files"], "correct": "Manage hardware and software"},
  {"questionNumber": 2, "question": "2. Who invented the World Wide Web?", "options": ["Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Mark Zuckerberg"], "correct": "Tim Berners-Lee"},
  {"questionNumber": 2, "question": "3. What year was Google founded?", "options": ["1996", "1998", "2000", "2002"], "correct": "1998"},
  {"questionNumber": 2, "question": "4. Which Kazakh university specializes in IT and robotics?", "options": ["Kazakh-British Technical University", "Nazarbayev University", "Al-Farabi KazNU", "KBTU"], "correct": "KBTU"},
  {"questionNumber": 2, "question": "5. What is open-source software?", "options": ["Free software with accessible code", "Paid software", "Software for students only", "Proprietary software"], "correct": "Free software with accessible code"},
  {"questionNumber": 2, "question": "6. Which company owns the Android operating system?", "options": ["Apple", "Google", "Microsoft", "Samsung"], "correct": "Google"},
  {"questionNumber": 2, "question": "7. What does GPU stand for?", "options": ["Graphics Processing Unit", "General Processing Unit", "Graphical Power Unit", "General Purpose Unit"], "correct": "Graphics Processing Unit"},
  {"questionNumber": 2, "question": "8. Which Kazakh city hosted the first tech startup festival?", "options": ["Almaty", "Astana", "Karaganda", "Shymkent"], "correct": "Almaty"},
  {"questionNumber": 2, "question": "9. What year was Facebook launched?", "options": ["2002", "2003", "2004", "2005"], "correct": "2004"},
  {"questionNumber": 2, "question": "10. What is blockchain technology mainly used for?", "options": ["Cryptocurrency", "AI", "Cloud storage", "Robotics"], "correct": "Cryptocurrency"},

  # questionNumber 3
  {"questionNumber": 3, "question": "1. Which programming language was created by James Gosling?", "options": ["C++", "Python", "Java", "Ruby"], "correct": "Java"},
  {"questionNumber": 3, "question": "2. What does IoT stand for?", "options": ["Internet of Things", "Input of Technology", "Intelligent of Things", "Interface of Tech"], "correct": "Internet of Things"},
  {"questionNumber": 3, "question": "3. Which Kazakh IT company focuses on fintech solutions?", "options": ["Kcell", "Finstar Kazakhstan", "KazTech Innovations", "Beeline"], "correct": "Finstar Kazakhstan"},
  {"questionNumber": 3, "question": "4. Which device is used to connect to a network wirelessly?", "options": ["Router", "Modem", "Switch", "Access Point"], "correct": "Access Point"},
  {"questionNumber": 3, "question": "5. What is the primary function of a compiler?", "options": ["Convert code into machine language", "Run applications", "Manage memory", "Store files"], "correct": "Convert code into machine language"},
  {"questionNumber": 3, "question": "6. Which Kazakh city has a growing AI development hub?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
  {"questionNumber": 3, "question": "7. What is cloud computing?", "options": ["Storing data on remote servers", "Computing on local PC", "Building a home server", "Downloading games"], "correct": "Storing data on remote servers"},
  {"questionNumber": 3, "question": "8. Who created Linux?", "options": ["Linus Torvalds", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"], "correct": "Linus Torvalds"},
  {"questionNumber": 3, "question": "9. Which Kazakh city has the largest number of IT startups?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
  {"questionNumber": 3, "question": "10. What is 5G technology mainly used for?", "options": ["Faster mobile networks", "Artificial intelligence", "Quantum computing", "Virtual reality"], "correct": "Faster mobile networks"},

  # questionNumber 4
  {"questionNumber": 4, "question": "1. What is a database?", "options": ["Collection of organized data", "Software application", "Programming language", "Network device"], "correct": "Collection of organized data"},
  {"questionNumber": 4, "question": "2. Which Kazakh university offers courses in cybersecurity?", "options": ["KBTU", "KazNU", "Nazarbayev University", "Al-Farabi KazNU"], "correct": "Nazarbayev University"},
  {"questionNumber": 4, "question": "3. Who is the co-founder of Apple?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"], "correct": "Steve Jobs"},
  {"questionNumber": 4, "question": "4. What is the main purpose of HTML?", "options": ["Create web pages", "Program apps", "Manage databases", "Encrypt data"], "correct": "Create web pages"},
  {"questionNumber": 4, "question": "5. Which Kazakh city hosts the annual tech expo 'Astana Hub'?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
  {"questionNumber": 4, "question": "6. What is VR technology used for?", "options": ["Virtual reality experiences", "Video recording", "Voice recognition", "Data storage"], "correct": "Virtual reality experiences"},
  {"questionNumber": 4, "question": "7. Which programming language is used to develop iOS apps?", "options": ["Swift", "Python", "Java", "C#"], "correct": "Swift"},
  {"questionNumber": 4, "question": "8. What does SEO stand for?", "options": ["Search Engine Optimization", "Software Engineering Output", "System Execution Order", "Search Entity Output"], "correct": "Search Engine Optimization"},
  {"questionNumber": 4, "question": "9. What is 3D printing?", "options": ["Creating objects layer by layer", "Digital animation", "Laser cutting", "Robotic assembly"], "correct": "Creating objects layer by layer"},
  {"questionNumber": 4, "question": "10. Which Kazakh city launched a blockchain-based city project?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

  # questionNumber 5
  {"questionNumber": 5, "question": "1. What is AI?", "options": ["Artificial Intelligence", "Automated Input", "Advanced Internet", "Algorithm Interface"], "correct": "Artificial Intelligence"},
  {"questionNumber": 5, "question": "2. Which Kazakh IT company develops e-government solutions?", "options": ["Beeline", "Astana IT", "Zerde", "Kcell"], "correct": "Zerde"},
  {"questionNumber": 5, "question": "3. Which technology is used for online payments?", "options": ["Fintech", "Blockchain", "VPN", "Cloud Computing"], "correct": "Fintech"},
  {"questionNumber": 5, "question": "4. What is the main function of a firewall?", "options": ["Protect network from attacks", "Store files", "Encrypt emails", "Connect devices"], "correct": "Protect network from attacks"},
  {"questionNumber": 5, "question": "5. Which Kazakh city has a tech incubator for startups?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
  {"questionNumber": 5, "question": "6. Which programming language is used for web backend?", "options": ["PHP", "Python", "JavaScript", "All of the above"], "correct": "All of the above"},
  {"questionNumber": 5, "question": "7. What is cloud storage?", "options": ["Online data storage", "Local hard drive storage", "Flash drive storage", "External HDD storage"], "correct": "Online data storage"},
  {"questionNumber": 5, "question": "8. What year was the first computer created?", "options": ["1830", "1843", "1936", "1943"], "correct": "Charles Babbage 1836"},
  {"questionNumber": 5, "question": "9. Which Kazakh city has an AI lab at Nazarbayev University?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
  {"questionNumber": 5, "question": "10. What is cybersecurity mainly concerned with?", "options": ["Protecting computers and networks", "Developing apps", "Artificial intelligence", "Designing websites"], "correct": "Protecting computers and networks"},

# questionNumber 6
{"questionNumber": 6, "question": "1. What is the main purpose of an algorithm?", "options": ["Solve problems", "Store data", "Run programs", "Connect networks"], "correct": "Solve problems"},
{"questionNumber": 6, "question": "2. Which Kazakh city has a coding school for children?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Almaty"},
{"questionNumber": 6, "question": "3. What is machine learning?", "options": ["AI technique to learn from data", "Programming language", "Cloud service", "Database type"], "correct": "AI technique to learn from data"},
{"questionNumber": 6, "question": "4. Who developed the first electronic computer?", "options": ["Charles Babbage", "Alan Turing", "John von Neumann", "Steve Jobs"], "correct": "John von Neumann"},
{"questionNumber": 6, "question": "5. Which Kazakh company develops AI solutions for healthcare?", "options": ["Astana IT", "KazTech Innovations", "Finstar Kazakhstan", "Beeline"], "correct": "KazTech Innovations"},
{"questionNumber": 6, "question": "6. What does VPN stand for?", "options": ["Virtual Private Network", "Visual Private Network", "Virtual Public Network", "Verified Private Network"], "correct": "Virtual Private Network"},
{"questionNumber": 6, "question": "7. Which technology is used for digital currency?", "options": ["Blockchain", "Cloud computing", "IoT", "VR"], "correct": "Blockchain"},
{"questionNumber": 6, "question": "8. Which programming language is known for data analysis?", "options": ["Python", "C#", "Swift", "HTML"], "correct": "Python"},
{"questionNumber": 6, "question": "9. What is augmented reality (AR)?", "options": ["Overlaying digital info on real world", "Virtual gaming", "3D printing", "Cloud computing"], "correct": "Overlaying digital info on real world"},
{"questionNumber": 6, "question": "10. Which Kazakh city hosts international IT conferences?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

# questionNumber 7
{"questionNumber": 7, "question": "1. What is the main use of a microprocessor?", "options": ["Process data in a computer", "Store files", "Display graphics", "Connect networks"], "correct": "Process data in a computer"},
{"questionNumber": 7, "question": "2. Who is the founder of Tesla and SpaceX?", "options": ["Elon Musk", "Jeff Bezos", "Steve Jobs", "Mark Zuckerberg"], "correct": "Elon Musk"},
{"questionNumber": 7, "question": "3. Which Kazakh city launched a robotics center for students?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
{"questionNumber": 7, "question": "4. What does HTML stand for?", "options": ["HyperText Markup Language", "HighText Markup Language", "Hyper Tool Markup Language", "HyperText Machine Language"], "correct": "HyperText Markup Language"},
{"questionNumber": 7, "question": "5. What is a server?", "options": ["Computer providing services over network", "Programming tool", "Mobile app", "Database"], "correct": "Computer providing services over network"},
{"questionNumber": 7, "question": "6. What is SaaS?", "options": ["Software as a Service", "System as a Server", "Security as a Service", "Storage as a Service"], "correct": "Software as a Service"},
{"questionNumber": 7, "question": "7. Which Kazakh university offers robotics courses?", "options": ["KBTU", "KazNU", "Nazarbayev University", "Al-Farabi KazNU"], "correct": "KBTU"},
{"questionNumber": 7, "question": "8. What is Python mainly used for?", "options": ["Web development, AI, data science", "Gaming only", "Networking only", "Databases only"], "correct": "Web development, AI, data science"},
{"questionNumber": 7, "question": "9. Which technology powers virtual assistants like Siri?", "options": ["AI and Natural Language Processing", "Blockchain", "Cloud storage", "IoT"], "correct": "AI and Natural Language Processing"},
{"questionNumber": 7, "question": "10. Which Kazakh city has an AI accelerator program?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

# questionNumber 8
{"questionNumber": 8, "question": "1. What is a cloud service provider?", "options": ["Company offering cloud computing", "Software developer", "Hardware manufacturer", "AI startup"], "correct": "Company offering cloud computing"},
{"questionNumber": 8, "question": "2. Who created the programming language C?", "options": ["Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"], "correct": "Dennis Ritchie"},
{"questionNumber": 8, "question": "3. What does API stand for?", "options": ["Application Programming Interface", "Automated Programming Instruction", "Advanced Program Integration", "Application Process Info"], "correct": "Application Programming Interface"},
{"questionNumber": 8, "question": "4. Which Kazakh city opened a cybersecurity training center?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Astana"},
{"questionNumber": 8, "question": "5. What is the main feature of IoT?", "options": ["Connect devices via Internet", "Store files locally", "Process offline", "Encrypt emails"], "correct": "Connect devices via Internet"},
{"questionNumber": 8, "question": "6. What is edge computing?", "options": ["Data processing near data source", "Cloud computing", "Mobile computing", "Desktop computing"], "correct": "Data processing near data source"},
{"questionNumber": 8, "question": "7. Which Kazakh city has an innovation hub for IoT projects?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
{"questionNumber": 8, "question": "8. What is cryptocurrency?", "options": ["Digital currency using blockchain", "Physical currency", "Online banking", "Credit card payment"], "correct": "Digital currency using blockchain"},
{"questionNumber": 8, "question": "9. Which programming language is used for Android development?", "options": ["Java", "Python", "C#", "Swift"], "correct": "Java"},
{"questionNumber": 8, "question": "10. Which Kazakh city promotes smart city projects?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

# questionNumber 9
{"questionNumber": 9, "question": "1. What is quantum computing?", "options": ["Next-gen computing using qubits", "Classical computing", "Mobile computing", "Cloud computing"], "correct": "Next-gen computing using qubits"},
{"questionNumber": 9, "question": "2. Who invented the first hard disk drive?", "options": ["IBM", "Seagate", "Western Digital", "Apple"], "correct": "IBM"},
{"questionNumber": 9, "question": "3. What does SSL stand for?", "options": ["Secure Sockets Layer", "System Security Level", "Secure Software Link", "Server Socket Layer"], "correct": "Secure Sockets Layer"},
{"questionNumber": 9, "question": "4. Which Kazakh city hosts the biggest hackathon?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
{"questionNumber": 9, "question": "5. What is a chatbot?", "options": ["AI program simulating conversation", "Database system", "Cloud service", "Mobile app"], "correct": "AI program simulating conversation"},
{"questionNumber": 9, "question": "6. Which technology enables self-driving cars?", "options": ["AI and sensors", "Blockchain", "Cloud storage", "IoT"], "correct": "AI and sensors"},
{"questionNumber": 9, "question": "7. Which Kazakh city has a drone development lab?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
{"questionNumber": 9, "question": "8. What is DevOps?", "options": ["Software development + IT operations", "AI programming", "Networking protocol", "Database management"], "correct": "Software development + IT operations"},
{"questionNumber": 9, "question": "9. What is the primary use of a firewall?", "options": ["Protect network from attacks", "Store data", "Encrypt files", "Run applications"], "correct": "Protect network from attacks"},
{"questionNumber": 9, "question": "10. Which Kazakh city has a blockchain education program?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

# questionNumber 10
{"questionNumber": 10, "question": "1. What is a supercomputer?", "options": ["High-performance computing system", "Personal computer", "Laptop", "Smartphone"], "correct": "High-performance computing system"},
{"questionNumber": 10, "question": "2. Who invented the first microprocessor?", "options": ["Intel", "IBM", "AMD", "Apple"], "correct": "Intel"},
{"questionNumber": 10, "question": "3. Which Kazakh city has a technology park for AI startups?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
{"questionNumber": 10, "question": "4. What is an IDE in programming?", "options": ["Integrated Development Environment", "Intelligent Data Engine", "Internet Development Extension", "Input Device Emulator"], "correct": "Integrated Development Environment"},
{"questionNumber": 10, "question": "5. What is a neural network?", "options": ["AI model inspired by the brain", "Networking system", "Cloud storage", "Mobile network"], "correct": "AI model inspired by the brain"},
{"questionNumber": 10, "question": "6. Which Kazakh city hosts AI and robotics competitions?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Astana"},
{"questionNumber": 10, "question": "7. What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "High Transfer Text Protocol", "Hyper Tool Transfer Protocol", "HyperText Translation Protocol"], "correct": "HyperText Transfer Protocol"},
{"questionNumber": 10, "question": "8. What is edge AI?", "options": ["AI processing on local devices", "AI in the cloud", "AI for gaming", "AI in robotics"], "correct": "AI processing on local devices"},
{"questionNumber": 10, "question": "9. Which programming language is used in web frontend?", "options": ["JavaScript", "Python", "C#", "Java"], "correct": "JavaScript"},
{"questionNumber": 10, "question": "10. Which Kazakh city promotes digital transformation projects?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
]
}


# 5) Güvenlik: verinin boş olmadığını doğrula
total_expected = sum(len(v) for v in db_quiz.values())
assert total_expected > 0, "db_quiz boş! Lütfen verileri ekleyin."

# 6) Insert
for category, questions in db_quiz.items():
    for i, q in enumerate(questions):
        cur.execute("""
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

# for i in range(1, 11):
#     item = random.choice(db["Science"][i]["questionNumber"]) 
#     cur.execute("SELECT * FROM item")

# 7) Doğrulama logları
cur.execute("SELECT COUNT(*) FROM questions")
count = cur.fetchone()[0]
cur.execute("SELECT category, COUNT(*) FROM questions GROUP BY category")
by_cat = cur.fetchall()

conn.close()
print(f"✔ DB path: {DB_PATH}")
print(f"✔ Toplam satır: {count}")
print(f"✔ Kategori bazında: {by_cat}")