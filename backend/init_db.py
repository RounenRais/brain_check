# init_db.py
import sqlite3
import os
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
    {
        "question_number": 1,
        "question": "Solve for x: 3x - 7 = 11",
        "options": [
            "x = 6",
            "x = 18",
            "x = 3",
            "x = -6",
        ],
        "correct": "x = 6",
    },
    {
        "question_number": 1,
        "question": "Solve for x: 5x + 2 = 2x + 14",
        "options": [
            "x = 4",
            "x = -4",
            "x = 6",
            "x = 2",
        ],
        "correct": "x = 4",
    },
    {
        "question_number": 1,
        "question": "Solve for x: (x / 4) + 3 = 7",
        "options": [
            "x = 8",
            "x = 12",
            "x = 14",
            "x = 16",
        ],
        "correct": "x = 16",
    },
    {
        "question_number": 1,
        "question": "Solve for x: 2(2x - 5) = 3x + 1",
        "options": [
            "x = 11",
            "x = -9",
            "x = 11",
            "x = -?",
        ],
        "correct": "x = 11",
    },
    {
        "question_number": 1,
        "question": "Solve for x: 7x - 4 = 2(3x + 1)",
        "options": [
            "x = 6",
            "x = -6",
            "x = 2",
            "x = 1",
        ],
        "correct": "x = 2",
    },
    {
        "question_number": 1,
        "question": "Solve for x: 0.5x + 1.5 = 2.5",
        "options": [
            "x = 1",
            "x = 2",
            "x = 3",
            "x = 0",
        ],
        "correct": "x = 2",
    },
    {
        "question_number": 1,
        "question": "Solve for x: 4x / 3 = 8",
        "options": [
            "x = 6",
            "x = 4",
            "x = 5",
            "x = 3",
        ],
        "correct": "x = 6",
    },
    {
        "question_number": 1,
        "question": "Solve for x: x - 3 = 1/2",
        "options": [
            "x = 3.5",
            "x = 2.5",
            "x = 4",
            "x = 5",
        ],
        "correct": "x = 3.5",
    },
    {
        "question_number": 1,
        "question": "Solve for x: 9x = 54",
        "options": [
            "x = 6",
            "x = 5",
            "x = 7",
            "x = 8",
        ],
        "correct": "x = 6",
    },
    {
        "question_number": 1,
        "question": "Solve for x: 6 - x = 2",
        "options": [
            "x = 4",
            "x = -4",
            "x = 8",
            "x = 2",
        ],
        "correct": "x = 4",
    },


    {
      "questionNumber": 2,
      "question": "Solve: x^2 + 6x + 5 = 0",
      "options": ["x = -1 or -5", "x = 1 or 5", "x = -6 or -1", "x = -5 only"],
      "correct": "x = -1 or -5"
    },
    {
      "questionNumber": 2,
      "question": "Solve: 2x^2 - 5x - 3 = 0",
      "options": ["x = 3 or -0.5", "x = -3 or 0.5", "x = 1 or -3", "x = -1 or 3"],
      "correct": "x = 3 or -0.5"
    },
    {
      "questionNumber": 2,
      "question": "If x^2 - 4x + k = 0 has one solution, find k",
      "options": ["k = 4", "k = -4", "k = 0", "k = 8"],
      "correct": "k = 4"
    },
    {
      "questionNumber": 2,
      "question": "Solve: (x - 2)(x + 3) = 5",
      "options": ["x = 3 or -4", "x = 4 or -3", "x = 5 or -1", "x = 1 or -5"],
      "correct": "x = 3 or -4"
    },
    {
      "questionNumber": 2,
      "question": "Solve: x^2 = 5x",
      "options": ["x = 0 or 5", "x = 1 or 5", "x = -5 or 0", "x = 5 only"],
      "correct": "x = 0 or 5"
    },
    {
      "questionNumber": 2,
      "question": "Solve: x(x - 7) + 10 = 0",
      "options": ["x = 5 or 2", "x = -5 or 2", "x = 7 or -10", "x = 0 or 7"],
      "correct": "x = 5 or 2"
    },
    {
      "questionNumber": 2,
      "question": "Solve: (x + 1)^2 = 9",
      "options": ["x = 2 or -4", "x = 3 or -3", "x = -2 or 4", "x = 1 or -3"],
      "correct": "x = 2 or -4"
    },
    {
      "questionNumber": 2,
      "question": "Solve system: { x^2 + y = 10; y = x }",
      "options": ["x = 2, y = 2", "x = -2, y = -2", "x = 3, y = 3", "x = 1, y = 1"],
      "correct": "x = 2, y = 2"
    },
    {
      "questionNumber": 2,
      "question": "For which x is x^2 - 2x - 8 > 0?",
      "options": ["x < -2 or x > 4", "-2 < x < 4", "x > -2", "x < 4"],
      "correct": "x < -2 or x > 4"
    },
    {
      "questionNumber": 2,
      "question": "Solve: |x - 3| = 5",
      "options": ["x = 8 or -2", "x = 5 or 1", "x = -8 or 2", "x = 3 only"],
      "correct": "x = 8 or -2"
    },


    {
        "question_number": 3,
        "question": (
            "Solve the system: "
            "{ x + y = 5; x^2 + y^2 = 13 }"
        ),
        "options": [
            "x = 2, y = 3",
            "x = 3, y = 2",
            "x = -2, y = -3",
            "x = 3, y = -2",
        ],
        "correct": "x = 2, y = 3",
    },
    {
        "question_number": 3,
        "question": (
            "Solve the system: "
            "{ 1/x + 1/y = 1/2; x - y = 2 }"
        ),
        "options": [
            "x = 4, y = 2",
            "x = 3, y = 1",
            "x = 6, y = 4",
            "x = 2, y = 0",
        ],
        "correct": "x = 4, y = 2",
    },
    {
        "question_number": 3,
        "question": (
            "For which value of k does the system have infinitely many solutions? "
            "{ 2x + 4y = 6; kx + 2ky = 3k }"
        ),
        "options": [
            "k = 1",
            "k = 2",
            "k = 3",
            "k ≠ 0",
        ],
        "correct": "k = 1",
    },
    {
        "question_number": 3,
        "question": (
            "Solve the system: "
            "{ |x - y| = 2; x + y = 6 }"
        ),
        "options": [
            "x = 4, y = 2",
            "x = 2, y = 4",
            "x = 5, y = 1",
            "x = 1, y = 5",
        ],
        "correct": "x = 4, y = 2",
    },
    {
        "question_number": 3,
        "question": (
            "Solve the system: "
            "{ x^2 - y = 7; x + y = 5 }"
        ),
        "options": [
            "x = 3, y = 2",
            "x = -2, y = 7",
            "x = 2, y = 3",
            "x = -3, y = 8",
        ],
        "correct": "x = 3, y = 2",
    },
    {
        "question_number": 3,
        "question": (
            "Determine the number of solutions: "
            "{ 3x + 2y = 6; 6x + 4y = 15 }"
        ),
        "options": [
            "No solution",
            "One solution",
            "Infinitely many solutions",
            "Two solutions",
        ],
        "correct": "No solution",
    },
    {
        "question_number": 3,
        "question": (
            "Solve the system: "
            "{ x/y = 2; x + y = 9 }"
        ),
        "options": [
            "x = 6, y = 3",
            "x = 3, y = 6",
            "x = 4.5, y = 4.5",
            "x = 2, y = 7",
        ],
        "correct": "x = 6, y = 3",
    },
    {
        "question_number": 3,
        "question": (
            "Solve the system: "
            "{ x + y = 4; (x - y)^2 = 4 }"
        ),
        "options": [
            "x = 3, y = 1",
            "x = 1, y = 3",
            "x = 2, y = 2",
            "x = 4, y = 0",
        ],
        "correct": "x = 3, y = 1",
    },
    {
        "question_number": 3,
        "question": (
            "Solve the system: "
            "{ 2x + y = 5; x^2 = y + 1 }"
        ),
        "options": [
            "x = 2, y = 1",
            "x = -1, y = 7",
            "x = 1, y = 3",
            "x = 3, y = -1",
        ],
        "correct": "x = 2, y = 1",
    },
    {
        "question_number": 3,
        "question": (
            "Find all solutions: "
            "{ x + y = 1; xy = -6 }"
        ),
        "options": [
            "x = 3, y = -2",
            "x = -3, y = 2",
            "x = 2, y = -3",
            "x = 1, y = 0",
        ],
        "correct": "x = 3, y = -2",
    },

    {
        "question_number": 4,
        "question": (
            "Simplify the expression: "
            "log_2(8x) - log_2(x), where x > 0"
        ),
        "options": [
            "3",
            "x",
            "log_2(8)",
            "3x",
        ],
        "correct": "3",
    },
    {
        "question_number": 4,
        "question": (
            "Solve for x: "
            "2^(x + 1) = 4^(x - 2)"
        ),
        "options": [
            "x = 5",
            "x = 3",
            "x = 1",
            "x = -1",
        ],
        "correct": "x = 5",
    },
    {
        "question_number": 4,
        "question": (
            "Solve: "
            "log_3(x - 1) + log_3(x - 3) = 2"
        ),
        "options": [
            "x = 4",
            "x = 5",
            "x = 6",
            "No solution",
        ],
        "correct": "x = 5",
    },
    {
        "question_number": 4,
        "question": (
            "Solve for x: "
            "e^(2x) - 5e^x + 6 = 0"
        ),
        "options": [
            "x = ln 2 or ln 3",
            "x = 2 or 3",
            "x = ln 5 or ln 6",
            "x = 1 or 2",
        ],
        "correct": "x = ln 2 or ln 3",
    },
    {
        "question_number": 4,
        "question": (
            "Simplify: "
            "ln(e^(x + 1)) - ln(e)"
        ),
        "options": [
            "x",
            "x + 1",
            "x - 1",
            "1",
        ],
        "correct": "x",
    },
    {
        "question_number": 4,
        "question": (
            "Solve: "
            "10^(2x) = 0.001"
        ),
        "options": [
            "x = -3/2",
            "x = -3",
            "x = 3/2",
            "x = -1",
        ],
        "correct": "x = -3/2",
    },
    {
        "question_number": 4,
        "question": (
            "If f(x) = 2^(x - 1), find f(3)"
        ),
        "options": [
            "4",
            "8",
            "2",
            "16",
        ],
        "correct": "4",
    },
    {
        "question_number": 4,
        "question": (
            "Find the domain of: "
            "log_5(x - 4)"
        ),
        "options": [
            "x > 4",
            "x ≥ 4",
            "x ≠ 4",
            "All real numbers",
        ],
        "correct": "x > 4",
    },
    {
        "question_number": 4,
        "question": (
            "Solve: "
            "4^(x) = 2^(2x + 2)"
        ),
        "options": [
            "x = -1",
            "x = 1",
            "x = 2",
            "x = 0",
        ],
        "correct": "x = -1",
    },
    {
        "question_number": 4,
        "question": (
            "Solve: "
            "ln(x) = 1 - ln(x)"
        ),
        "options": [
            "x = e^(1/2)",
            "x = e",
            "x = 1",
            "No solution",
        ],
        "correct": "x = e^(1/2)",
    },

    {
        "question_number": 5,
        "question": (
            "Find the value of: "
            "sin(π/3) · cos(π/6)"
        ),
        "options": [
            "3/4",
            "√3/4",
            "1/2",
            "√3/2",
        ],
        "correct": "3/4",
    },
    {
        "question_number": 5,
        "question": (
            "Simplify: "
            "sin(x) / cos(x)"
        ),
        "options": [
            "tan(x)",
            "cot(x)",
            "sin^2(x)",
            "1 / tan(x)",
        ],
        "correct": "tan(x)",
    },
    {
        "question_number": 5,
        "question": (
            "Solve for x in [0, 2π): "
            "sin(x) = 1/2"
        ),
        "options": [
            "x = π/6 or 5π/6",
            "x = π/3 or 2π/3",
            "x = π/6 only",
            "x = 5π/6 only",
        ],
        "correct": "x = π/6 or 5π/6",
    },
    {
        "question_number": 5,
        "question": (
            "Simplify using identities: "
            "1 - cos^2(x)"
        ),
        "options": [
            "sin^2(x)",
            "cos(x)",
            "1",
            "tan^2(x)",
        ],
        "correct": "sin^2(x)",
    },
    {
        "question_number": 5,
        "question": (
            "Solve for x in [0, 2π): "
            "cos(x) = -1/2"
        ),
        "options": [
            "x = 2π/3 or 4π/3",
            "x = π/3 or 5π/3",
            "x = π only",
            "x = 3π/2",
        ],
        "correct": "x = 2π/3 or 4π/3",
    },
    {
        "question_number": 5,
        "question": (
            "Evaluate: "
            "tan(π/3) · sin(π/6)"
        ),
        "options": [
            "√3/2",
            "1/2",
            "√3",
            "1",
        ],
        "correct": "√3/2",
    },
    {
        "question_number": 5,
        "question": (
            "Which identity is always true?"
        ),
        "options": [
            "1 + tan^2(x) = sec^2(x)",
            "tan(x) = sin^2(x) + cos^2(x)",
            "sin(x) = cos(x)",
            "cos(x) = 1 - sin(x)",
        ],
        "correct": "1 + tan^2(x) = sec^2(x)",
    },
    {
        "question_number": 5,
        "question": (
            "Simplify: "
            "sin(2x) / (2 sin(x))"
        ),
        "options": [
            "cos(x)",
            "sin(x)",
            "tan(x)",
            "1",
        ],
        "correct": "cos(x)",
    },
    {
        "question_number": 5,
        "question": (
            "Find all x in [0, 2π): "
            "tan(x) = 1"
        ),
        "options": [
            "x = π/4 or 5π/4",
            "x = π/6 or 7π/6",
            "x = π/3 or 4π/3",
            "x = π/2 or 3π/2",
        ],
        "correct": "x = π/4 or 5π/4",
    },
    {
        "question_number": 5,
        "question": (
            "Evaluate: "
            "cos(π) + sin(π/2)"
        ),
        "options": [
            "0",
            "1",
            "-1",
            "2",
        ],
        "correct": "0",
    },

    {
        "question_number": 6,
        "question": (
            "Compute the limit: "
            "lim_{x→0} (1 - cos(x)) / x**2"
        ),
        "options": [
            "1/2",
            "1",
            "0",
            "2",
        ],
        "correct": "1/2",
    },
    {
        "question_number": 6,
        "question": "Find f'(2) for f(x) = x**3 - 3*x**2.",
        "options": [
            "0",
            "1",
            "6",
            "-3",
        ],
        "correct": "0",
    },
    {
        "question_number": 6,
        "question": (
            "Equation of the tangent line to y = x**2 at x = 1."
        ),
        "options": [
            "y = 2*x - 1",
            "y = x - 1",
            "y = 2*x + 1",
            "y = x + 1",
        ],
        "correct": "y = 2*x - 1",
    },
    {
        "question_number": 6,
        "question": "Compute derivative: d/dx [ln(x**2)].",
        "options": [
            "2 / x",
            "ln(2x)",
            "1 / x**2",
            "2 * ln(x)",
        ],
        "correct": "2 / x",
    },
    {
        "question_number": 6,
        "question": "Evaluate the definite integral: ∫_0^1 x dx.",
        "options": [
            "1/2",
            "1",
            "1/3",
            "2",
        ],
        "correct": "1/2",
    },
    {
        "question_number": 6,
        "question": "Find critical points of f(x) = x**3 - 3*x.",
        "options": [
            "x = -1 and x = 1",
            "x = 0 only",
            "x = -3 and x = 3",
            "No critical points",
        ],
        "correct": "x = -1 and x = 1",
    },
    {
        "question_number": 6,
        "question": "Compute limit: lim_{n→∞} (1 + 1/n)**n.",
        "options": [
            "e",
            "1",
            "∞",
            "0",
        ],
        "correct": "e",
    },
    {
        "question_number": 6,
        "question": "d/dx [sin(2*x)] equals:",
        "options": [
            "2*cos(2*x)",
            "cos(2*x)",
            "2*sin(2*x)",
            "cos(x)",
        ],
        "correct": "2*cos(2*x)",
    },
    {
        "question_number": 6,
        "question": "Area under y = 1 from x = 0 to x = 3 is:",
        "options": [
            "3",
            "1",
            "0",
            "6",
        ],
        "correct": "3",
    },
    {
        "question_number": 6,
        "question": "Find derivative at x = 1 of x**x.",
        "options": [
            "1",
            "0",
            "e",
            "2",
        ],
        "correct": "1",
    },

    # ===== question_number = 7 (Advanced calculus & series) =====
    {
        "question_number": 7,
        "question": (
            "Evaluate the definite integral: "
            "∫_0^{ln 2} e^{2*x} dx"
        ),
        "options": [
            "3/2",
            "1/2",
            "2",
            "ln 2",
        ],
        "correct": "3/2",
    },
    {
        "question_number": 7,
        "question": "Does the series ∑_{n=1}^∞ 1/n**2 converge?",
        "options": [
            "Yes, converges",
            "No, diverges",
            "Converges only conditionally",
            "Depends on n",
        ],
        "correct": "Yes, converges",
    },
    {
        "question_number": 7,
        "question": "Solve the ODE: dy/dx = 3*y, with y(0)=2.",
        "options": [
            "y = 2*e^{3*x}",
            "y = 3*e^{2*x}",
            "y = 2 + 3*x",
            "y = e^{3*x}",
        ],
        "correct": "y = 2*e^{3*x}",
    },
    {
        "question_number": 7,
        "question": (
            "Evaluate the improper integral: "
            "∫_1^{∞} 1/x**2 dx"
        ),
        "options": [
            "1",
            "∞",
            "0",
            "1/2",
        ],
        "correct": "1",
    },
    {
        "question_number": 7,
        "question": "Second-degree Taylor polynomial of e^x at 0:",
        "options": [
            "1 + x + x**2 / 2",
            "1 + x",
            "e^x",
            "1 + x + x**3 / 6",
        ],
        "correct": "1 + x + x**2 / 2",
    },
    {
        "question_number": 7,
        "question": "Compute ∫_0^{π} sin(x) dx.",
        "options": [
            "2",
            "0",
            "1",
            "π",
        ],
        "correct": "2",
    },
    {
        "question_number": 7,
        "question": "Sum of infinite geometric series with a = 3, r = 1/4:",
        "options": [
            "4",
            "3/4",
            "1",
            "12",
        ],
        "correct": "4",
    },
    {
        "question_number": 7,
        "question": "Solve separable DE: dy/dx = x, y(0)=1.",
        "options": [
            "y = x**2 / 2 + 1",
            "y = x + 1",
            "y = x**2 + 1",
            "y = 1",
        ],
        "correct": "y = x**2 / 2 + 1",
    },
    {
        "question_number": 7,
        "question": "Value of d/dx [x**x] at x = 1:",
        "options": [
            "1",
            "0",
            "e",
            "2",
        ],
        "correct": "1",
    },
    {
        "question_number": 7,
        "question": "Compute ∫_0^1 1 / (1 + x**2) dx.",
        "options": [
            "π / 4",
            "1",
            "ln 2",
            "1/2",
        ],
        "correct": "π / 4",
    },

    # ===== question_number = 8 (Linear algebra — advanced) =====
    {
        "question_number": 8,
        "question": "determinant of matrix [[2, 1], [1, 2]] is:",
        "options": [
            "3",
            "1",
            "4",
            "0",
        ],
        "correct": "3",
    },
    {
        "question_number": 8,
        "question": "Eigenvalues of diag(2, 3) are:",
        "options": [
            "2 and 3",
            "1 and 5",
            "0 and 5",
            "2 and -3",
        ],
        "correct": "2 and 3",
    },
    {
        "question_number": 8,
        "question": (
            "Matrix A = [[1, 2], [2, 4]] has rank:"
        ),
        "options": [
            "1",
            "2",
            "0",
            "3",
        ],
        "correct": "1",
    },
    {
        "question_number": 8,
        "question": (
            "Inverse of [[1, 2], [3, 4]] equals:"
        ),
        "options": [
            "[[-2, 1], [1.5, -0.5]]",
            "[[2, -1], [-1.5, 0.5]]",
            "[[4, -2], [-3, 1]]",
            "Matrix is not invertible",
        ],
        "correct": "[[-2, 1], [1.5, -0.5]]",
    },
    {
        "question_number": 8,
        "question": "Trace of a matrix equals:",
        "options": [
            "Sum of eigenvalues (counted with multiplicity)",
            "Determinant",
            "Number of nonzero rows",
            "Rank squared",
        ],
        "correct": "Sum of eigenvalues (counted with multiplicity)",
    },
    {
        "question_number": 8,
        "question": "An orthogonal matrix Q satisfies:",
        "options": [
            "Q^{-1} = Q^{T}",
            "Q = Q^{2}",
            "det(Q) = 0",
            "Q is diagonal",
        ],
        "correct": "Q^{-1} = Q^{T}",
    },
    {
        "question_number": 8,
        "question": (
            "Eigenvector of [[2, 1], [1, 2]] corresponding "
            "to eigenvalue 3 is proportional to:"
        ),
        "options": [
            "[1, 1]",
            "[1, -1]",
            "[2, -1]",
            "[0, 1]",
        ],
        "correct": "[1, 1]",
    },
    {
        "question_number": 8,
        "question": "Projection of (2, 1) onto (1, 0) is:",
        "options": [
            "(2, 0)",
            "(1, 0)",
            "(2, 1)",
            "(0, 1)",
        ],
        "correct": "(2, 0)",
    },
    {
        "question_number": 8,
        "question": (
            "Solve linear system: "
            "A x = b with A = [[1, 0, 0], [0, 2, 0], [0, 0, 3]] "
            "and b = [1, 2, 3]. x = ?"
        ),
        "options": [
            "[1, 1, 1]",
            "[1, 1, 1/3]",
            "[1, 1, 0]",
            "[1, 1, 3]",
        ],
        "correct": "[1, 1, 1]",
    },
    {
        "question_number": 8,
        "question": "If A is 2x2 with det(A) = 5, det(2*A) equals:",
        "options": [
            "20",
            "10",
            "5",
            "2",
        ],
        "correct": "20",
    },

    # ===== question_number = 9 (Probability & Statistics — advanced) =====
    {
        "question_number": 9,
        "question": "Probability of at least one head in 3 fair coin flips:",
        "options": [
            "7/8",
            "3/8",
            "1/8",
            "1",
        ],
        "correct": "7/8",
    },
    {
        "question_number": 9,
        "question": "Expected value of a fair six-sided die:",
        "options": [
            "3.5",
            "3",
            "4",
            "21",
        ],
        "correct": "3.5",
    },
    {
        "question_number": 9,
        "question": "Variance of fair six-sided die (1..6):",
        "options": [
            "35 / 12",
            "2",
            "3.5",
            "6",
        ],
        "correct": "35 / 12",
    },
    {
        "question_number": 9,
        "question": "P(X = 2) for Binomial(n=3, p=1/2):",
        "options": [
            "3/8",
            "1/8",
            "1/2",
            "3/4",
        ],
        "correct": "3/8",
    },
    {
        "question_number": 9,
        "question": (
            "Two balls drawn without replacement from 2 red, 3 blue. "
            "P(both red)?"
        ),
        "options": [
            "1 / 10",
            "2 / 5",
            "1 / 5",
            "3 / 10",
        ],
        "correct": "1 / 10",
    },
    {
        "question_number": 9,
        "question": (
            "Which statement describes the Central Limit Theorem?"
        ),
        "options": [
            "Sample mean approximates normal for large n",
            "Sample mean equals population mean for any n",
            "Distribution becomes uniform for large n",
            "Variance goes to zero for large n",
        ],
        "correct": "Sample mean approximates normal for large n",
    },
    {
        "question_number": 9,
        "question": "For Poisson(λ), mean equals:",
        "options": [
            "λ",
            "√λ",
            "λ^2",
            "1/λ",
        ],
        "correct": "λ",
    },
    {
        "question_number": 9,
        "question": "Approximately what percentage lies within 1σ of mean in normal dist.?",
        "options": [
            "About 68%",
            "About 95%",
            "About 50%",
            "About 99.7%",
        ],
        "correct": "About 68%",
    },
    {
        "question_number": 9,
        "question": "If A and B independent, P(A ∩ B) equals:",
        "options": [
            "P(A) * P(B)",
            "P(A) + P(B)",
            "P(A) - P(B)",
            "0",
        ],
        "correct": "P(A) * P(B)",
    },
    {
        "question_number": 9,
        "question": "Sample space of one fair coin toss is:",
        "options": [
            "{H, T}",
            "{0, 1, 2}",
            "R",
            "Empty set",
        ],
        "correct": "{H, T}",
    },

    # ===== question_number = 10 (Olympiad / Very advanced) =====
    {
        "question_number": 10,
        "question": "Solve for real x: x**4 - 5*x**2 + 4 = 0.",
        "options": [
            "x = ±1, ±2",
            "x = ±1 only",
            "x = ±2 only",
            "No real roots",
        ],
        "correct": "x = ±1, ±2",
    },
    {
        "question_number": 10,
        "question": (
            "How many integer pairs (x, y) satisfy x**2 + y**2 = 25?"
        ),
        "options": [
            "12",
            "8",
            "4",
            "16",
        ],
        "correct": "12",
    },
    {
        "question_number": 10,
        "question": "Compute the telescoping sum: ∑_{n=1}^N 1/(n(n+1)).",
        "options": [
            "1 - 1/(N + 1)",
            "1/(N + 1)",
            "N/(N + 1)",
            "1",
        ],
        "correct": "1 - 1/(N + 1)",
    },
    {
        "question_number": 10,
        "question": "Minimum of x + 1/x for x > 0 is:",
        "options": [
            "2",
            "1",
            "0",
            "No minimum",
        ],
        "correct": "2",
    },
    {
        "question_number": 10,
        "question": "Solve congruence 3*x ≡ 1 (mod 7).",
        "options": [
            "x ≡ 5 (mod 7)",
            "x ≡ 3 (mod 7)",
            "x ≡ 1 (mod 7)",
            "No solution",
        ],
        "correct": "x ≡ 5 (mod 7)",
    },
    {
        "question_number": 10,
        "question": (
            "Number of onto functions from a 3-element set to a 2-element set:"
        ),
        "options": [
            "6",
            "8",
            "4",
            "2",
        ],
        "correct": "6",
    },
    {
        "question_number": 10,
        "question": "Number of distinct strings from 3 R's and 2 B's:",
        "options": [
            "10",
            "5",
            "15",
            "20",
        ],
        "correct": "10",
    },
    {
        "question_number": 10,
        "question": "Area of right triangle with legs 3 and 4 is:",
        "options": [
            "6",
            "12",
            "7",
            "24",
        ],
        "correct": "6",
    },
    {
        "question_number": 10,
        "question": "Evaluate ∫_0^{π/2} sin**2(x) dx.",
        "options": [
            "π / 4",
            "π / 2",
            "1",
            "0",
        ],
        "correct": "π / 4",
    },
    {
        "question_number": 10,
        "question": "gcd(2**100 - 1, 2**50 - 1) equals:",
        "options": [
            "2**50 - 1",
            "1",
            "2**100 - 1",
            "2**25 - 1",
        ],
        "correct": "2**50 - 1",
    },
    ],

  "History": [
    # ====================== question_number = 1 (basic facts) ======================
    {
        "question_number": 1,
        "question": "Who was the first President of the United States?",
        "options": [
            "George Washington",
            "John Adams",
            "Thomas Jefferson",
            "James Madison",
        ],
        "correct": "George Washington",
    },
    {
        "question_number": 1,
        "question": "In which year did the United States declare independence?",
        "options": [
            "1776",
            "1783",
            "1812",
            "1607",
        ],
        "correct": "1776",
    },
    {
        "question_number": 1,
        "question": "Which ancient civilization built the pyramids of Giza?",
        "options": [
            "Ancient Egyptians",
            "Mesopotamians",
            "Romans",
            "Phoenicians",
        ],
        "correct": "Ancient Egyptians",
    },
    {
        "question_number": 1,
        "question": "Which river was central to ancient Egyptian civilization?",
        "options": [
            "Nile",
            "Tigris",
            "Euphrates",
            "Amazon",
        ],
        "correct": "Nile",
    },
    {
        "question_number": 1,
        "question": "Who was the first emperor of unified China?",
        "options": [
            "Qin Shi Huang",
            "Liu Bang",
            "Kublai Khan",
            "Emperor Wu",
        ],
        "correct": "Qin Shi Huang",
    },
    {
        "question_number": 1,
        "question": "Which civilization built Machu Picchu?",
        "options": [
            "Inca",
            "Maya",
            "Aztec",
            "Olmec",
        ],
        "correct": "Inca",
    },
    {
        "question_number": 1,
        "question": "What city was the capital of the Byzantine Empire?",
        "options": [
            "Constantinople",
            "Rome",
            "Alexandria",
            "Athens",
        ],
        "correct": "Constantinople",
    },
    {
        "question_number": 1,
        "question": "Which people developed cuneiform writing?",
        "options": [
            "Sumerians",
            "Egyptians",
            "Phoenicians",
            "Hittites",
        ],
        "correct": "Sumerians",
    },
    {
        "question_number": 1,
        "question": "On which island was Napoleon Bonaparte finally exiled?",
        "options": [
            "Saint Helena",
            "Elba",
            "Corsica",
            "Sicily",
        ],
        "correct": "Saint Helena",
    },
    {
        "question_number": 1,
        "question": "What language was the primary official language of the Roman Empire?",
        "options": [
            "Latin",
            "Greek",
            "Aramaic",
            "Egyptian",
        ],
        "correct": "Latin",
    },

    # ====================== question_number = 2 (dates & periods) ======================
    {
        "question_number": 2,
        "question": "In which year did World War I begin?",
        "options": [
            "1914",
            "1918",
            "1939",
            "1905",
        ],
        "correct": "1914",
    },
    {
        "question_number": 2,
        "question": "In which year did World War II begin?",
        "options": [
            "1939",
            "1914",
            "1945",
            "1929",
        ],
        "correct": "1939",
    },
    {
        "question_number": 2,
        "question": "Which year marks the fall of the Western Roman Empire?",
        "options": [
            "476",
            "410",
            "1453",
            "330",
        ],
        "correct": "476",
    },
    {
        "question_number": 2,
        "question": "In which year did Columbus first reach the Americas?",
        "options": [
            "1492",
            "1502",
            "1485",
            "1519",
        ],
        "correct": "1492",
    },
    {
        "question_number": 2,
        "question": "When was the Magna Carta sealed?",
        "options": [
            "1215",
            "1066",
            "1415",
            "1314",
        ],
        "correct": "1215",
    },
    {
        "question_number": 2,
        "question": "What year is commonly given for the start of the French Revolution?",
        "options": [
            "1789",
            "1776",
            "1804",
            "1799",
        ],
        "correct": "1789",
    },
    {
        "question_number": 2,
        "question": "When did the Berlin Wall fall?",
        "options": [
            "1989",
            "1991",
            "1979",
            "2001",
        ],
        "correct": "1989",
    },
    {
        "question_number": 2,
        "question": "When was the Peace of Westphalia signed (ending Thirty Years' War)?",
        "options": [
            "1648",
            "1517",
            "1815",
            "1701",
        ],
        "correct": "1648",
    },
    {
        "question_number": 2,
        "question": "In which year did the Ottoman Empire officially end (abolition of the sultanate)?",
        "options": [
            "1922",
            "1918",
            "1939",
            "1908",
        ],
        "correct": "1922",
    },
    {
        "question_number": 2,
        "question": "In what year did the American Civil War begin?",
        "options": [
            "1861",
            "1850",
            "1870",
            "1848",
        ],
        "correct": "1861",
    },

    # ====================== question_number = 3 (revolutions & leaders) ======================
    {
        "question_number": 3,
        "question": "Who led the Bolshevik Revolution in Russia (1917)?",
        "options": [
            "Vladimir Lenin",
            "Joseph Stalin",
            "Leon Trotsky",
            "Nicholas II",
        ],
        "correct": "Vladimir Lenin",
    },
    {
        "question_number": 3,
        "question": "Who nailed the Ninety-Five Theses and sparked the Protestant Reformation?",
        "options": [
            "Martin Luther",
            "John Calvin",
            "Henry VIII",
            "Ulrich Zwingli",
        ],
        "correct": "Martin Luther",
    },
    {
        "question_number": 3,
        "question": "Who led the Indian independence movement with nonviolent resistance?",
        "options": [
            "Mahatma Gandhi",
            "Jawaharlal Nehru",
            "Subhas Chandra Bose",
            "Bhagat Singh",
        ],
        "correct": "Mahatma Gandhi",
    },
    {
        "question_number": 3,
        "question": "Who led the Cuban Revolution that brought Castro to power?",
        "options": [
            "Fidel Castro",
            "Che Guevara",
            "Fulgencio Batista",
            "Raúl Castro",
        ],
        "correct": "Fidel Castro",
    },
    {
        "question_number": 3,
        "question": "Who was the British Prime Minister famous for leading the UK in WWII?",
        "options": [
            "Winston Churchill",
            "Neville Chamberlain",
            "Clement Attlee",
            "Stanley Baldwin",
        ],
        "correct": "Winston Churchill",
    },
    {
        "question_number": 3,
        "question": "Who was President of the United States during the Civil War?",
        "options": [
            "Abraham Lincoln",
            "Ulysses S. Grant",
            "Andrew Johnson",
            "James Buchanan",
        ],
        "correct": "Abraham Lincoln",
    },
    {
        "question_number": 3,
        "question": "Which Japanese era name marks the modernization beginning in 1868?",
        "options": [
            "Meiji",
            "Taishō",
            "Showa",
            "Heisei",
        ],
        "correct": "Meiji",
    },
    {
        "question_number": 3,
        "question": "Who was a famous Carthaginian general who crossed the Alps to fight Rome?",
        "options": [
            "Hannibal",
            "Scipio Africanus",
            "Carthalo",
            "Hasdrubal",
        ],
        "correct": "Hannibal",
    },
    {
        "question_number": 3,
        "question": "Who principally authored the United States Declaration of Independence?",
        "options": [
            "Thomas Jefferson",
            "Benjamin Franklin",
            "John Adams",
            "James Madison",
        ],
        "correct": "Thomas Jefferson",
    },
    {
        "question_number": 3,
        "question": "Who became ruler of France after the Revolution and crowned himself Emperor in 1804?",
        "options": [
            "Napoleon Bonaparte",
            "Louis XVI",
            "Robespierre",
            "Louis XVIII",
        ],
        "correct": "Napoleon Bonaparte",
    },

    # ====================== question_number = 4 (wars & diplomacy) ======================
    {
        "question_number": 4,
        "question": "Where was Archduke Franz Ferdinand assassinated in 1914?",
        "options": [
            "Sarajevo",
            "Vienna",
            "Belgrade",
            "Prague",
        ],
        "correct": "Sarajevo",
    },
    {
        "question_number": 4,
        "question": "Which treaty formally ended World War I with Germany?",
        "options": [
            "Treaty of Versailles (1919)",
            "Treaty of Brest-Litovsk",
            "Treaty of Paris (1815)",
            "Treaty of Tordesillas",
        ],
        "correct": "Treaty of Versailles (1919)",
    },
    {
        "question_number": 4,
        "question": "Which naval battle was a decisive turning point in the Pacific in WWII (1942)?",
        "options": [
            "Battle of Midway",
            "Battle of the Coral Sea",
            "Battle of Leyte Gulf",
            "Battle of Guadalcanal",
        ],
        "correct": "Battle of Midway",
    },
    {
        "question_number": 4,
        "question": "Which conference in 1945 established the United Nations?",
        "options": [
            "Yalta Conference",
            "Potsdam Conference",
            "Tehran Conference",
            "San Francisco Conference",
        ],
        "correct": "San Francisco Conference",
    },
    {
        "question_number": 4,
        "question": "What was the primary goal of the Marshall Plan after WWII?",
        "options": [
            "Rebuild European economies and prevent communism",
            "Punish Germany",
            "Partition Eastern Europe",
            "Create NATO",
        ],
        "correct": "Rebuild European economies and prevent communism",
    },
    {
        "question_number": 4,
        "question": "Which operation was the Allied invasion of Normandy in 1944?",
        "options": [
            "Operation Overlord",
            "Operation Torch",
            "Operation Market Garden",
            "Operation Husky",
        ],
        "correct": "Operation Overlord",
    },
    {
        "question_number": 4,
        "question": "Which 19th-century congress attempted to restore the European balance after Napoleon?",
        "options": [
            "Congress of Vienna (1814–1815)",
            "Congress of Berlin",
            "Congress of Aix-la-Chapelle",
            "Congress of Paris (1856)",
        ],
        "correct": "Congress of Vienna (1814–1815)",
    },
    {
        "question_number": 4,
        "question": "Which Asian country was partitioned in 1947 creating two states?",
        "options": [
            "British India (India and Pakistan)",
            "Korea",
            "Vietnam",
            "Indonesia",
        ],
        "correct": "British India (India and Pakistan)",
    },
    {
        "question_number": 4,
        "question": "Which treaty ended the Thirty Years' War and impacted state sovereignty?",
        "options": [
            "Peace of Westphalia (1648)",
            "Treaty of Utrecht",
            "Treaty of Paris (1763)",
            "Treaty of Tilsit",
        ],
        "correct": "Peace of Westphalia (1648)",
    },
    {
        "question_number": 4,
        "question": "Which event directly led the United States to enter World War II?",
        "options": [
            "Attack on Pearl Harbor",
            "Sinking of the Lusitania",
            "Invasion of Poland",
            "D-Day landings",
        ],
        "correct": "Attack on Pearl Harbor",
    },

    # ====================== question_number = 5 (decolonization & Cold War) ======================
    {
        "question_number": 5,
        "question": "Which battle in 1954 ended major French colonial rule in Indochina?",
        "options": [
            "Battle of Dien Bien Phu",
            "Battle of the Somme",
            "Battle of Midway",
            "Battle of Algiers",
        ],
        "correct": "Battle of Dien Bien Phu",
    },
    {
        "question_number": 5,
        "question": "Which U.S. foreign-policy doctrine (1947) committed aid to countries resisting communism?",
        "options": [
            "Truman Doctrine",
            "Monroe Doctrine",
            "Marshall Plan",
            "Eisenhower Doctrine",
        ],
        "correct": "Truman Doctrine",
    },
    {
        "question_number": 5,
        "question": "What name describes the Cold War competition in arms, space, and ideology?",
        "options": [
            "Cold War",
            "Great War",
            "Pax Britannica",
            "Thirty Years' Crisis",
        ],
        "correct": "Cold War",
    },
    {
        "question_number": 5,
        "question": "Which 20th-century process refers to former colonies gaining independence?",
        "options": [
            "Decolonization",
            "Industrialization",
            "Feudalization",
            "Urbanization",
        ],
        "correct": "Decolonization",
    },
    {
        "question_number": 5,
        "question": "Which U.S. program provided economic recovery funds to Europe after WWII?",
        "options": [
            "Marshall Plan",
            "New Deal",
            "Point Four Program",
            "Lend-Lease",
        ],
        "correct": "Marshall Plan",
    },
    {
        "question_number": 5,
        "question": "Which crisis in 1962 brought the U.S. and USSR close to nuclear war?",
        "options": [
            "Cuban Missile Crisis",
            "Berlin Blockade",
            "Suez Crisis",
            "Korean War",
        ],
        "correct": "Cuban Missile Crisis",
    },
    {
        "question_number": 5,
        "question": "Which policy described containment of Soviet influence after WWII?",
        "options": [
            "Containment",
            "Appeasement",
            "Isolationism",
            "Collective Security",
        ],
        "correct": "Containment",
    },
    {
        "question_number": 5,
        "question": "Which African country launched a major anti-colonial war against France (1954–1962)?",
        "options": [
            "Algeria",
            "Kenya",
            "Ghana",
            "Nigeria",
        ],
        "correct": "Algeria",
    },
    {
        "question_number": 5,
        "question": "Which 1948 event led to the formal establishment of Israel in 1948?",
        "options": [
            "UN Partition Plan and subsequent war (1947–1949)",
            "Balfour Declaration (1917)",
            "Sykes-Picot Agreement",
            "Camp David Accords",
        ],
        "correct": "UN Partition Plan and subsequent war (1947–1949)",
    },
    {
        "question_number": 5,
        "question": "Which ideology opposed liberal capitalism and influenced many 20th-century states?",
        "options": [
            "Communism",
            "Monarchism",
            "Liberalism",
            "Mercantilism",
        ],
        "correct": "Communism",
    },

    # ====================== question_number = 6 (economic & social history) ======================
    {
        "question_number": 6,
        "question": "Which revolution introduced mass industrial production in the 18th century?",
        "options": [
            "Industrial Revolution",
            "Agricultural Revolution",
            "Neolithic Revolution",
            "Scientific Revolution",
        ],
        "correct": "Industrial Revolution",
    },
    {
        "question_number": 6,
        "question": "Which 19th-century invention dramatically improved long-distance communication?",
        "options": [
            "The telegraph",
            "The steam engine",
            "The spinning jenny",
            "The printing press",
        ],
        "correct": "The telegraph",
    },
    {
        "question_number": 6,
        "question": "Which economic system is characterized by private ownership and market exchange?",
        "options": [
            "Capitalism",
            "Feudalism",
            "Communism",
            "Mercantilism",
        ],
        "correct": "Capitalism",
    },
    {
        "question_number": 6,
        "question": "Which movement sought political rights and representation for working classes in 19th-century Europe?",
        "options": [
            "Labor movement",
            "Enlightenment",
            "Romanticism",
            "Absolutism",
        ],
        "correct": "Labor movement",
    },
    {
        "question_number": 6,
        "question": "Which 1848 publication argued that class struggle drives historical change?",
        "options": [
            "The Communist Manifesto",
            "On Liberty",
            "Das Kapital",
            "Wealth of Nations",
        ],
        "correct": "The Communist Manifesto",
    },
    {
        "question_number": 6,
        "question": "Which policy in Britain (19th century) removed many trade restrictions and promoted free trade?",
        "options": [
            "Repeal of the Corn Laws",
            "Navigation Acts",
            "Enclosure Acts",
            "Factory Acts",
        ],
        "correct": "Repeal of the Corn Laws",
    },
    {
        "question_number": 6,
        "question": "Which agricultural improvement increased yields before industrialization in Britain?",
        "options": [
            "Selective breeding and crop rotation",
            "Slash-and-burn",
            "Three-field system only",
            "Terracing",
        ],
        "correct": "Selective breeding and crop rotation",
    },
    {
        "question_number": 6,
        "question": "Which process describes mass movement from countryside to cities during industrialization?",
        "options": [
            "Urbanization",
            "Colonization",
            "Globalization",
            "Suburbanization",
        ],
        "correct": "Urbanization",
    },
    {
        "question_number": 6,
        "question": "Which 19th-century ideology emphasized national self-determination and unity?",
        "options": [
            "Nationalism",
            "Liberalism",
            "Conservatism",
            "Socialism",
        ],
        "correct": "Nationalism",
    },
    {
        "question_number": 6,
        "question": "Which economic measure tracks average price change over time for goods and services?",
        "options": [
            "Inflation rate (CPI)",
            "GDP growth rate",
            "Unemployment rate",
            "Balance of trade",
        ],
        "correct": "Inflation rate (CPI)",
    },

    # ====================== question_number = 7 (historiography & methods) ======================
    {
        "question_number": 7,
        "question": "Which historian is associated with the Annales School?",
        "options": [
            "Fernand Braudel",
            "Edward Gibbon",
            "Leopold von Ranke",
            "Will Durant",
        ],
        "correct": "Fernand Braudel",
    },
    {
        "question_number": 7,
        "question": "What does 'primary source' mean in historical research?",
        "options": [
            "Original material produced at the time under study",
            "A modern textbook summary",
            "A later historian's interpretation",
            "A fictional account",
        ],
        "correct": "Original material produced at the time under study",
    },
    {
        "question_number": 7,
        "question": "Which method emphasizes long-term social structures over events?",
        "options": [
            "Longue durée",
            "Great man theory",
            "Positivist chronology",
            "Whig history",
        ],
        "correct": "Longue durée",
    },
    {
        "question_number": 7,
        "question": "What does 'revisionist history' typically involve?",
        "options": [
            "Reinterpreting established narratives in light of new evidence",
            "Repeating classic accounts without change",
            "Ignoring primary sources",
            "Creating myths",
        ],
        "correct": "Reinterpreting established narratives in light of new evidence",
    },
    {
        "question_number": 7,
        "question": "Which historian emphasized empirical archival research and political narrative?",
        "options": [
            "Leopold von Ranke",
            "Fernand Braudel",
            "Herodotus",
            "Thucydides",
        ],
        "correct": "Leopold von Ranke",
    },
    {
        "question_number": 7,
        "question": "Which concept studies how ordinary people's experiences shape history?",
        "options": [
            "Social history",
            "Diplomatic history",
            "Military history",
            "Intellectual history",
        ],
        "correct": "Social history",
    },
    {
        "question_number": 7,
        "question": "Which source type is oral history?",
        "options": [
            "Primary source (interviews and testimonies)",
            "Secondary source only",
            "Tertiary compilation",
            "Fictional narrative",
        ],
        "correct": "Primary source (interviews and testimonies)",
    },
    {
        "question_number": 7,
        "question": "What does 'anachronism' mean in historical interpretation?",
        "options": [
            "Assigning later ideas to earlier periods erroneously",
            "Using only primary sources",
            "Studying many time periods",
            "Comparing two contemporaries",
        ],
        "correct": "Assigning later ideas to earlier periods erroneously",
    },
    {
        "question_number": 7,
        "question": "Which approach examines gender roles and relations in history?",
        "options": [
            "Gender history",
            "Economic determinism",
            "Whig interpretation",
            "Diplomatic analysis",
        ],
        "correct": "Gender history",
    },
    {
        "question_number": 7,
        "question": "Which term describes a bias favoring one's own nation's history?",
        "options": [
            "Nationalist bias",
            "Chronological bias",
            "Methodological skepticism",
            "Pluralist approach",
        ],
        "correct": "Nationalist bias",
    },

    # ====================== question_number = 8 (primary documents & interpretation) ======================
    {
        "question_number": 8,
        "question": "Which document begins with 'When in the Course of human events'?",
        "options": [
            "United States Declaration of Independence",
            "Magna Carta",
            "Bill of Rights (US)",
            "English Petition of Right",
        ],
        "correct": "United States Declaration of Independence",
    },
    {
        "question_number": 8,
        "question": "The 'Letter from Birmingham Jail' (1963) was written by which leader?",
        "options": [
            "Martin Luther King Jr.",
            "Malcolm X",
            "Rosa Parks",
            "W. E. B. Du Bois",
        ],
        "correct": "Martin Luther King Jr.",
    },
    {
        "question_number": 8,
        "question": "Which 18th-century document established principles of popular sovereignty in France?",
        "options": [
            "Declaration of the Rights of Man and of the Citizen (1789)",
            "Code Napoleon",
            "Edict of Nantes",
            "Treaty of Paris (1783)",
        ],
        "correct": "Declaration of the Rights of Man and of the Citizen (1789)",
    },
    {
        "question_number": 8,
        "question": "Which primary source is most useful to study economic life in a city?",
        "options": [
            "Tax records and merchants' account books",
            "Poems and plays only",
            "Military dispatches",
            "Royal decrees only",
        ],
        "correct": "Tax records and merchants' account books",
    },
    {
        "question_number": 8,
        "question": "Which report exposed social conditions in industrial Britain (1840s) and influenced reform?",
        "options": [
            "Reports by social investigators and commissions",
            "Magna Carta",
            "Federalist Papers",
            "Treaty of Westphalia",
        ],
        "correct": "Reports by social investigators and commissions",
    },
    {
        "question_number": 8,
        "question": "Which 19th-century British act reformed parliamentary representation (1832)?",
        "options": [
            "Great Reform Act (Reform Act 1832)",
            "Corn Laws",
            "Factory Act",
            "Navigation Acts",
        ],
        "correct": "Great Reform Act (Reform Act 1832)",
    },
    {
        "question_number": 8,
        "question": "Which primary evidence would best show public opinion in the 18th century?",
        "options": [
            "Pamphlets, newspapers, and petitions",
            "Official treaties alone",
            "Only royal proclamations",
            "Astronomical charts",
        ],
        "correct": "Pamphlets, newspapers, and petitions",
    },
    {
        "question_number": 8,
        "question": "Which economic cause contributed to the French Revolution's outbreak?",
        "options": [
            "Regressive taxation and fiscal crisis",
            "Excessive industrial growth",
            "Abundant grain harvests",
            "Complete financial stability",
        ],
        "correct": "Regressive taxation and fiscal crisis",
    },
    {
        "question_number": 8,
        "question": "Which feature distinguishes a primary from a secondary source?",
        "options": [
            "Primary is contemporary to the events described",
            "Primary is always written by historians",
            "Secondary is older than primary",
            "Primary is fictional",
        ],
        "correct": "Primary is contemporary to the events described",
    },
    {
        "question_number": 8,
        "question": "Which type of source best reveals elite diplomatic intentions?",
        "options": [
            "Privileged diplomatic correspondence and treaties",
            "Oral folklore only",
            "Agricultural manuals",
            "Fiction novels",
        ],
        "correct": "Privileged diplomatic correspondence and treaties",
    },

    # ====================== question_number = 9 (comparative & thematic analysis) ======================
    {
        "question_number": 9,
        "question": "Which concept compares imperial control across different empires?",
        "options": [
            "Comparative imperialism",
            "National exceptionalism",
            "Localism",
            "Isolationism",
        ],
        "correct": "Comparative imperialism",
    },
    {
        "question_number": 9,
        "question": "What is a macrohistorical approach?",
        "options": [
            "Studying large-scale patterns across centuries",
            "Focusing only on individual biographies",
            "Examining a single document in isolation",
            "Performing laboratory experiments",
        ],
        "correct": "Studying large-scale patterns across centuries",
    },
    {
        "question_number": 9,
        "question": "Which theme analyzes how trade networks shaped early modern globalization?",
        "options": [
            "Atlantic and Indian Ocean trade networks",
            "Space exploration",
            "Industrial labor laws",
            "Modern welfare states",
        ],
        "correct": "Atlantic and Indian Ocean trade networks",
    },
    {
        "question_number": 9,
        "question": "Which method studies how environmental factors influence historical change?",
        "options": [
            "Environmental history",
            "Purely political history",
            "Numismatics only",
            "Astrology",
        ],
        "correct": "Environmental history",
    },
    {
        "question_number": 9,
        "question": "Which ideological movement influenced 19th-century national unifications (Italy, Germany)?",
        "options": [
            "Romantic nationalism",
            "Classical liberalism",
            "Orthodoxy",
            "Feudalism",
        ],
        "correct": "Romantic nationalism",
    },
    {
        "question_number": 9,
        "question": "Which factor was central to the Industrial Revolution's geographic origins in Britain?",
        "options": [
            "Access to coal, capital, and markets",
            "Absence of waterways",
            "Low population density",
            "Complete isolation from trade",
        ],
        "correct": "Access to coal, capital, and markets",
    },
    {
        "question_number": 9,
        "question": "Which historiographical turn emphasized culture, language, and symbols since the 1970s?",
        "options": [
            "The cultural turn",
            "The political turn",
            "The mechanistic turn",
            "The numerical turn",
        ],
        "correct": "The cultural turn",
    },
    {
        "question_number": 9,
        "question": "Which comparative question would a historian ask about revolutions?",
        "options": [
            "How did social structure influence revolutionary outcomes?",
            "What is the color of the flag?",
            "Who wrote the national anthem?",
            "What is the exact temperature on the first day?",
        ],
        "correct": "How did social structure influence revolutionary outcomes?",
    },
    {
        "question_number": 9,
        "question": "Which global process after 1945 reshaped former colonies politically and economically?",
        "options": [
            "Decolonization and Cold War competition",
            "Renaissance",
            "Feudal restoration",
            "Mercantilist expansion",
        ],
        "correct": "Decolonization and Cold War competition",
    },
    {
        "question_number": 9,
        "question": "Which evidence best supports an argument about popular protest patterns?",
        "options": [
            "Cross-regional protest records, petitions, and police reports",
            "Single elite diary only",
            "Weather reports alone",
            "Architectural plans",
        ],
        "correct": "Cross-regional protest records, petitions, and police reports",
    },

    # ====================== question_number = 10 (synthesis & original thinking) ======================
    {
        "question_number": 10,
        "question": "Which explanation best synthesizes causes of large-scale revolutions?",
        "options": [
            "Interaction of structural economic stress, political crisis, and cultural shifts",
            "Only individual leaders cause revolutions",
            "Weather is the sole cause",
            "Revolutions are random events with no cause",
        ],
        "correct": "Interaction of structural economic stress, political crisis, and cultural shifts",
    },
    {
        "question_number": 10,
        "question": "Which approach best analyzes empire decline across centuries?",
        "options": [
            "Integrate economic, military, cultural, and environmental factors comparatively",
            "Focus only on military defeat",
            "Ignore internal political factors",
            "Study a single biography only",
        ],
        "correct": "Integrate economic, military, cultural, and environmental factors comparatively",
    },
    {
        "question_number": 10,
        "question": "Which historiographical debate centers on whether ideology or material conditions drive change?",
        "options": [
            "Structure vs. agency (materialist vs. ideational explanations)",
            "Ancient vs. modern debate",
            "Textual vs. oral triviality",
            "Chronological ordering dispute",
        ],
        "correct": "Structure vs. agency (materialist vs. ideational explanations)",
    },
    {
        "question_number": 10,
        "question": "Which research design is strongest to test a causal claim about economic growth and democratization?",
        "options": [
            "Cross-national statistical analysis combined with case studies",
            "Single anecdote",
            "Random selection of songs",
            "Ignoring data entirely",
        ],
        "correct": "Cross-national statistical analysis combined with case studies",
    },
    {
        "question_number": 10,
        "question": "Which primary-source critique is essential when using colonial archives?",
        "options": [
            "Consider author perspective, purpose, and power relations",
            "Assume all documents are unbiased",
            "Use only translated summaries",
            "Ignore context",
        ],
        "correct": "Consider author perspective, purpose, and power relations",
    },
    {
        "question_number": 10,
        "question": "Which concept addresses historical continuity amid change?",
        "options": [
            "Longue durée",
            "Whig teleology",
            "Epic chronology",
            "Selective amnesia",
        ],
        "correct": "Longue durée",
    },
    {
        "question_number": 10,
        "question": "Which comparative method helps identify causal mechanisms in history?",
        "options": [
            "Most-similar and most-different systems design",
            "Random guessing",
            "Only reading poetry",
            "Excluding counterexamples",
        ],
        "correct": "Most-similar and most-different systems design",
    },
    {
        "question_number": 10,
        "question": "Which practice improves reliability of quantitative history research?",
        "options": [
            "Transparency in data sources, coding decisions, and robustness checks",
            "Hiding raw data",
            "Reporting only favorable results",
            "Using single-case evidence only",
        ],
        "correct": "Transparency in data sources, coding decisions, and robustness checks",
    },
    {
        "question_number": 10,
        "question": "Which argument best exemplifies synthesis across ecological and social history?",
        "options": [
            "Climate variability altered agricultural surplus and hence social institutions",
            "Climate had no historical effect",
            "Only elites mattered in all changes",
            "Technology is irrelevant",
        ],
        "correct": "Climate variability altered agricultural surplus and hence social institutions",
    },
    {
        "question_number": 10,
        "question": "Which research output demonstrates original historical contribution?",
        "options": [
            "A well-argued thesis combining new sources and methodologically sound analysis",
            "A list of dates without argument",
            "A translation without commentary",
            "A summary of Wikipedia entries",
        ],
        "correct": "A well-argued thesis combining new sources and methodologically sound analysis",
    },
    ],

  "Science": [
    # questionNumber 1
    {"questionNumber": 1, "question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "correct": "H2O"},
    {"questionNumber": 1, "question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correct": "Mars"},
    {"questionNumber": 1, "question": "What gas do humans exhale?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "correct": "Carbon Dioxide"},
    {"questionNumber": 1, "question": "What is the center of an atom called?", "options": ["Electron", "Proton", "Nucleus", "Neutron"], "correct": "Nucleus"},
    {"questionNumber": 1, "question": "Which part of the plant makes food?", "options": ["Root", "Stem", "Leaf", "Flower"], "correct": "Leaf"},
    {"questionNumber": 1, "question": "What is the speed of light?", "options": ["3×10⁸ m/s", "3×10⁶ m/s", "1×10⁸ m/s", "5×10⁷ m/s"], "correct": "3×10⁸ m/s"},
    {"questionNumber": 1, "question": "What force keeps us on the ground?", "options": ["Friction", "Gravity", "Magnetism", "Inertia"], "correct": "Gravity"},
    {"questionNumber": 1, "question": "What is the boiling point of water?", "options": ["90°C", "95°C", "100°C", "110°C"], "correct": "100°C"},
    {"questionNumber": 1, "question": "What part of the human body pumps blood?", "options": ["Brain", "Lungs", "Heart", "Liver"], "correct": "Heart"},
    {"questionNumber": 1, "question": "What type of energy does a moving object have?", "options": ["Potential", "Thermal", "Kinetic", "Chemical"], "correct": "Kinetic"},

    # questionNumber 2
    {"questionNumber": 2, "question": "What gas do plants absorb during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Carbon Dioxide"},
    {"questionNumber": 2, "question": "Which planet is closest to the Sun?", "options": ["Venus", "Mercury", "Earth", "Mars"], "correct": "Mercury"},
    {"questionNumber": 2, "question": "What is the hardest natural substance on Earth?", "options": ["Iron", "Diamond", "Gold", "Quartz"], "correct": "Diamond"},
    {"questionNumber": 2, "question": "Which part of the cell controls its activities?", "options": ["Nucleus", "Cytoplasm", "Membrane", "Vacuole"], "correct": "Nucleus"},
    {"questionNumber": 2, "question": "What is measured in Newtons?", "options": ["Force", "Energy", "Speed", "Mass"], "correct": "Force"},
    {"questionNumber": 2, "question": "What is the main gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Nitrogen"},
    {"questionNumber": 2, "question": "What type of energy is stored in food?", "options": ["Thermal", "Kinetic", "Chemical", "Electrical"], "correct": "Chemical"},
    {"questionNumber": 2, "question": "What instrument measures temperature?", "options": ["Barometer", "Thermometer", "Hygrometer", "Anemometer"], "correct": "Thermometer"},
    {"questionNumber": 2, "question": "Which blood cells help fight infection?", "options": ["Red cells", "White cells", "Platelets", "Plasma"], "correct": "White cells"},
    {"questionNumber": 2, "question": "What is the main source of energy for Earth?", "options": ["Wind", "Sun", "Water", "Geothermal"], "correct": "Sun"},

    # questionNumber 3
    {"questionNumber": 3, "question": "What is the largest planet in our Solar System?", "options": ["Earth", "Saturn", "Jupiter", "Neptune"], "correct": "Jupiter"},
    {"questionNumber": 3, "question": "What part of the human body controls movement and balance?", "options": ["Cerebrum", "Cerebellum", "Brainstem", "Spinal cord"], "correct": "Cerebellum"},
    {"questionNumber": 3, "question": "What is the chemical symbol for gold?", "options": ["G", "Ag", "Au", "Go"], "correct": "Au"},
    {"questionNumber": 3, "question": "What phenomenon causes rainbows?", "options": ["Reflection", "Refraction", "Diffraction", "Dispersion"], "correct": "Dispersion"},
    {"questionNumber": 3, "question": "What is the process by which liquid water changes to vapor?", "options": ["Condensation", "Freezing", "Evaporation", "Melting"], "correct": "Evaporation"},
    {"questionNumber": 3, "question": "What gas do humans need to survive?", "options": ["Carbon Dioxide", "Nitrogen", "Oxygen", "Hydrogen"], "correct": "Oxygen"},
    {"questionNumber": 3, "question": "What is the unit of electrical current?", "options": ["Volt", "Ampere", "Ohm", "Watt"], "correct": "Ampere"},
    {"questionNumber": 3, "question": "What type of blood cells carry oxygen?", "options": ["Red cells", "White cells", "Platelets", "Plasma"], "correct": "Red cells"},
    {"questionNumber": 3, "question": "Which organ in the body filters blood?", "options": ["Heart", "Kidneys", "Lungs", "Liver"], "correct": "Kidneys"},
    {"questionNumber": 3, "question": "What is the main organ of the nervous system?", "options": ["Heart", "Brain", "Lungs", "Liver"], "correct": "Brain"},

    # questionNumber 4
    {"questionNumber": 4, "question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"], "correct": "Mitochondria"},
    {"questionNumber": 4, "question": "What planet has the most moons?", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "correct": "Saturn"},
    {"questionNumber": 4, "question": "What is the process by which plants make their food?", "options": ["Respiration", "Photosynthesis", "Fermentation", "Transpiration"], "correct": "Photosynthesis"},
    {"questionNumber": 4, "question": "What is the study of living organisms called?", "options": ["Physics", "Chemistry", "Biology", "Astronomy"], "correct": "Biology"},
    {"questionNumber": 4, "question": "What part of the human eye controls the amount of light entering?", "options": ["Pupil", "Iris", "Lens", "Cornea"], "correct": "Iris"},
    {"questionNumber": 4, "question": "Which vitamin is produced by the skin in sunlight?", "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin E"], "correct": "Vitamin D"},
    {"questionNumber": 4, "question": "What is the smallest unit of matter?", "options": ["Molecule", "Atom", "Proton", "Cell"], "correct": "Atom"},
    {"questionNumber": 4, "question": "What part of the plant absorbs water?", "options": ["Stem", "Root", "Leaf", "Flower"], "correct": "Root"},
    {"questionNumber": 4, "question": "What is the process by which ice turns directly into vapor?", "options": ["Condensation", "Sublimation", "Evaporation", "Melting"], "correct": "Sublimation"},
    {"questionNumber": 4, "question": "What is the closest star to Earth?", "options": ["Sirius", "Alpha Centauri", "Sun", "Proxima Centauri"], "correct": "Sun"},

    # questionNumber 5
    {"questionNumber": 5, "question": "What is Newton’s third law of motion?", "options": ["F=ma", "For every action, there is an equal and opposite reaction", "Energy cannot be created or destroyed", "An object at rest stays at rest"], "correct": "For every action, there is an equal and opposite reaction"},
    {"questionNumber": 5, "question": "What type of blood does the universal donor have?", "options": ["A", "B", "AB", "O negative"], "correct": "O negative"},
    {"questionNumber": 5, "question": "What is the main function of red blood cells?", "options": ["Fight infection", "Carry oxygen", "Produce hormones", "Store nutrients"], "correct": "Carry oxygen"},
    {"questionNumber": 5, "question": "Which element is necessary for respiration?", "options": ["Hydrogen", "Oxygen", "Nitrogen", "Helium"], "correct": "Oxygen"},
    {"questionNumber": 5, "question": "What is the SI unit of power?", "options": ["Volt", "Newton", "Watt", "Joule"], "correct": "Watt"},
    {"questionNumber": 5, "question": "Which part of the brain controls breathing?", "options": ["Cerebrum", "Cerebellum", "Medulla Oblongata", "Hippocampus"], "correct": "Medulla Oblongata"},
    {"questionNumber": 5, "question": "What is the most abundant element in the universe?", "options": ["Oxygen", "Hydrogen", "Carbon", "Helium"], "correct": "Hydrogen"},
    {"questionNumber": 5, "question": "What process do living organisms use to release energy from food?", "options": ["Photosynthesis", "Respiration", "Fermentation", "Transpiration"], "correct": "Respiration"},
    {"questionNumber": 5, "question": "Which metal is liquid at room temperature?", "options": ["Mercury", "Iron", "Sodium", "Lead"], "correct": "Mercury"},
    {"questionNumber": 5, "question": "What is the main gas responsible for the greenhouse effect?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "correct": "Carbon Dioxide"},

    # questionNumber 6
    {"questionNumber": 6, "question": "What is the main function of red blood cells?", "options": ["Fight infection", "Carry oxygen", "Digest food", "Transport hormones"], "correct": "Carry oxygen"},
    {"questionNumber": 6, "question": "Which vitamin is produced when skin is exposed to sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "correct": "Vitamin D"},
    {"questionNumber": 6, "question": "What is the center of the Solar System?", "options": ["Earth", "Sun", "Moon", "Jupiter"], "correct": "Sun"},
    {"questionNumber": 6, "question": "What process converts sugar into energy in cells?", "options": ["Respiration", "Photosynthesis", "Fermentation", "Osmosis"], "correct": "Respiration"},
    {"questionNumber": 6, "question": "What type of energy is stored in food?", "options": ["Thermal", "Chemical", "Kinetic", "Potential"], "correct": "Chemical"},
    {"questionNumber": 6, "question": "What part of the cell contains genetic material?", "options": ["Cytoplasm", "Nucleus", "Cell wall", "Ribosome"], "correct": "Nucleus"},
    {"questionNumber": 6, "question": "What is the main gas responsible for global warming?", "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"], "correct": "Carbon Dioxide"},
    {"questionNumber": 6, "question": "What is H2SO4 commonly known as?", "options": ["Nitric acid", "Sulfuric acid", "Hydrochloric acid", "Acetic acid"], "correct": "Sulfuric acid"},
    {"questionNumber": 6, "question": "What is the most abundant element in the universe?", "options": ["Helium", "Oxygen", "Hydrogen", "Carbon"], "correct": "Hydrogen"},
    {"questionNumber": 6, "question": "What instrument measures atmospheric pressure?", "options": ["Thermometer", "Barometer", "Anemometer", "Hygrometer"], "correct": "Barometer"},

    # questionNumber 7
    {"questionNumber": 7, "question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "1,000 km/s", "3,000 km/s"], "correct": "300,000 km/s"},
    {"questionNumber": 7, "question": "What organ filters blood in the human body?", "options": ["Liver", "Heart", "Kidneys", "Lungs"], "correct": "Kidneys"},
    {"questionNumber": 7, "question": "Which metal is liquid at room temperature?", "options": ["Mercury", "Iron", "Sodium", "Zinc"], "correct": "Mercury"},
    {"questionNumber": 7, "question": "Which planet is known for its Great Red Spot?", "options": ["Earth", "Saturn", "Jupiter", "Mars"], "correct": "Jupiter"},
    {"questionNumber": 7, "question": "What is the chemical symbol for gold?", "options": ["Ag", "Au", "Pb", "Fe"], "correct": "Au"},
    {"questionNumber": 7, "question": "What is the smallest unit of life?", "options": ["Atom", "Molecule", "Cell", "Organ"], "correct": "Cell"},
    {"questionNumber": 7, "question": "What is the process by which plants lose water through leaves?", "options": ["Photosynthesis", "Transpiration", "Condensation", "Evaporation"], "correct": "Transpiration"},
    {"questionNumber": 7, "question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Chloroplast", "Ribosome"], "correct": "Mitochondria"},
    {"questionNumber": 7, "question": "What is the freezing point of water?", "options": ["-5°C", "0°C", "10°C", "32°C"], "correct": "0°C"},
    {"questionNumber": 7, "question": "What is Earth's primary source of energy?", "options": ["Coal", "Wind", "Sun", "Nuclear"], "correct": "Sun"},

    # questionNumber 8
    {"questionNumber": 8, "question": "Which blood type is known as the universal donor?", "options": ["A", "B", "O", "AB"], "correct": "O"},
    {"questionNumber": 8, "question": "What part of the plant absorbs water and minerals?", "options": ["Stem", "Root", "Leaf", "Flower"], "correct": "Root"},
    {"questionNumber": 8, "question": "What natural phenomenon is measured by the Richter scale?", "options": ["Hurricanes", "Earthquakes", "Floods", "Volcanoes"], "correct": "Earthquakes"},
    {"questionNumber": 8, "question": "What is the most common gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Nitrogen"},
    {"questionNumber": 8, "question": "What part of the human body produces insulin?", "options": ["Liver", "Pancreas", "Kidneys", "Heart"], "correct": "Pancreas"},
    {"questionNumber": 8, "question": "What is the main source of energy for photosynthesis?", "options": ["Soil", "Water", "Sunlight", "Oxygen"], "correct": "Sunlight"},
    {"questionNumber": 8, "question": "What is the study of living organisms called?", "options": ["Geology", "Biology", "Chemistry", "Physics"], "correct": "Biology"},
    {"questionNumber": 8, "question": "Which planet has the most moons?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "correct": "Saturn"},
    {"questionNumber": 8, "question": "What is the largest organ of the human body?", "options": ["Liver", "Brain", "Skin", "Heart"], "correct": "Skin"},
    {"questionNumber": 8, "question": "What scientist proposed the three laws of motion?", "options": ["Einstein", "Newton", "Galileo", "Kepler"], "correct": "Newton"},

    # questionNumber 9
    {"questionNumber": 9, "question": "What is the main component of the Sun?", "options": ["Oxygen", "Hydrogen", "Helium", "Carbon"], "correct": "Hydrogen"},
    {"questionNumber": 9, "question": "Which planet is called Earth’s twin?", "options": ["Mars", "Venus", "Mercury", "Jupiter"], "correct": "Venus"},
    {"questionNumber": 9, "question": "What part of the eye controls the amount of light entering?", "options": ["Retina", "Cornea", "Pupil", "Lens"], "correct": "Pupil"},
    {"questionNumber": 9, "question": "Which element has the symbol O?", "options": ["Osmium", "Oxygen", "Oganesson", "Oxide"], "correct": "Oxygen"},
    {"questionNumber": 9, "question": "What is measured in ohms?", "options": ["Current", "Voltage", "Resistance", "Power"], "correct": "Resistance"},
    {"questionNumber": 9, "question": "What type of energy is associated with moving objects?", "options": ["Potential", "Kinetic", "Chemical", "Thermal"], "correct": "Kinetic"},
    {"questionNumber": 9, "question": "What organ helps maintain body balance?", "options": ["Heart", "Lungs", "Inner ear", "Liver"], "correct": "Inner ear"},
    {"questionNumber": 9, "question": "What is the main function of chlorophyll?", "options": ["Absorb sunlight", "Store water", "Support plant", "Transport minerals"], "correct": "Absorb sunlight"},
    {"questionNumber": 9, "question": "What planet has the largest volcano?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "correct": "Mars"},
    {"questionNumber": 9, "question": "Which metal is used in batteries?", "options": ["Zinc", "Lead", "Lithium", "Copper"], "correct": "Lithium"},

    # questionNumber 10
    {"questionNumber": 10, "question": "What is the chemical symbol for sodium?", "options": ["S", "Na", "N", "Sn"], "correct": "Na"},
    {"questionNumber": 10, "question": "Which scientist discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Isaac Newton"], "correct": "Alexander Fleming"},
    {"questionNumber": 10, "question": "What is the main function of white blood cells?", "options": ["Clot blood", "Fight infection", "Carry oxygen", "Transport nutrients"], "correct": "Fight infection"},
    {"questionNumber": 10, "question": "What planet is farthest from the Sun?", "options": ["Neptune", "Uranus", "Saturn", "Pluto"], "correct": "Neptune"},
    {"questionNumber": 10, "question": "What is the most common element in the human body?", "options": ["Carbon", "Hydrogen", "Oxygen", "Nitrogen"], "correct": "Oxygen"},
    {"questionNumber": 10, "question": "What part of the brain controls breathing?", "options": ["Cerebrum", "Cerebellum", "Medulla Oblongata", "Hypothalamus"], "correct": "Medulla Oblongata"},
    {"questionNumber": 10, "question": "What is the SI unit of force?", "options": ["Watt", "Newton", "Pascal", "Joule"], "correct": "Newton"},
    {"questionNumber": 10, "question": "What is the process by which liquids change to gas?", "options": ["Condensation", "Evaporation", "Freezing", "Melting"], "correct": "Evaporation"},
    {"questionNumber": 10, "question": "What part of an atom has a positive charge?", "options": ["Electron", "Neutron", "Proton", "Nucleus"], "correct": "Proton"},
    {"questionNumber": 10, "question": "What is the main gas used in balloons?", "options": ["Oxygen", "Helium", "Hydrogen", "Nitrogen"], "correct": "Helium"}
  ],
   
  "Geography": [
    {"questionNumber": 1, "question": "What is the largest continent on Earth?", "options": ["Africa", "Asia", "Europe", "North America"], "correct": "Asia"},
    {"questionNumber": 1, "question": "Which ocean is the deepest?", "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "correct": "Pacific Ocean"},
    {"questionNumber": 1, "question": "What is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct": "Nile"},
    {"questionNumber": 1, "question": "Which country has the largest population?", "options": ["India", "China", "USA", "Indonesia"], "correct": "China"},
    {"questionNumber": 1, "question": "What is the capital city of Kazakhstan?", "options": ["Almaty", "Astana", "Shymkent", "Atyrau"], "correct": "Astana"},
    {"questionNumber": 1, "question": "Which desert is the largest in the world?", "options": ["Gobi", "Sahara", "Arabian", "Kalahari"], "correct": "Sahara"},
    {"questionNumber": 1, "question": "What mountain range separates Europe and Asia?", "options": ["Himalayas", "Alps", "Ural Mountains", "Andes"], "correct": "Ural Mountains"},
    {"questionNumber": 1, "question": "What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"], "correct": "Vatican City"},
    {"questionNumber": 1, "question": "What ocean surrounds Japan?", "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "correct": "Pacific Ocean"},
    {"questionNumber": 1, "question": "Which country is known as the ‘Land of a Thousand Lakes’?", "options": ["Norway", "Finland", "Canada", "Sweden"], "correct": "Finland"},

    {"questionNumber": 2, "question": "What is the longest mountain range in the world?", "options": ["Rockies", "Andes", "Himalayas", "Alps"], "correct": "Andes"},
    {"questionNumber": 2, "question": "Which continent has the most countries?", "options": ["Europe", "Asia", "Africa", "South America"], "correct": "Africa"},
    {"questionNumber": 2, "question": "What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"], "correct": "Ottawa"},
    {"questionNumber": 2, "question": "Which river flows through Paris?", "options": ["Thames", "Danube", "Seine", "Rhine"], "correct": "Seine"},
    {"questionNumber": 2, "question": "What is the largest island in the world?", "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"], "correct": "Greenland"},
    {"questionNumber": 2, "question": "What is the highest mountain in the world?", "options": ["K2", "Everest", "Kangchenjunga", "Lhotse"], "correct": "Everest"},
    {"questionNumber": 2, "question": "Which sea is the saltiest?", "options": ["Dead Sea", "Caspian Sea", "Black Sea", "Red Sea"], "correct": "Dead Sea"},
    {"questionNumber": 2, "question": "What is the capital of Japan?", "options": ["Osaka", "Tokyo", "Kyoto", "Nagoya"], "correct": "Tokyo"},
    {"questionNumber": 2, "question": "Which country has the longest coastline?", "options": ["Australia", "Canada", "Russia", "Indonesia"], "correct": "Canada"},
    {"questionNumber": 2, "question": "What river runs through Egypt?", "options": ["Amazon", "Nile", "Tigris", "Euphrates"], "correct": "Nile"},

    {"questionNumber": 3, "question": "What is the largest lake in the world by area?", "options": ["Caspian Sea", "Lake Superior", "Lake Victoria", "Lake Baikal"], "correct": "Caspian Sea"},
    {"questionNumber": 3, "question": "Which desert covers most of northern Africa?", "options": ["Sahara", "Gobi", "Kalahari", "Namib"], "correct": "Sahara"},
    {"questionNumber": 3, "question": "What is the capital of France?", "options": ["Berlin", "Rome", "Madrid", "Paris"], "correct": "Paris"},
    {"questionNumber": 3, "question": "Which continent is known as the ‘Dark Continent’?", "options": ["Asia", "Africa", "South America", "Europe"], "correct": "Africa"},
    {"questionNumber": 3, "question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "correct": "Canberra"},
    {"questionNumber": 3, "question": "Which country is home to the Amazon rainforest?", "options": ["Peru", "Brazil", "Colombia", "Venezuela"], "correct": "Brazil"},
    {"questionNumber": 3, "question": "What is the capital of Russia?", "options": ["St. Petersburg", "Moscow", "Kazan", "Novosibirsk"], "correct": "Moscow"},
    {"questionNumber": 3, "question": "Which continent is completely in the Southern Hemisphere?", "options": ["Australia", "Africa", "South America", "Antarctica"], "correct": "Antarctica"},
    {"questionNumber": 3, "question": "What river flows through London?", "options": ["Thames", "Seine", "Danube", "Elbe"], "correct": "Thames"},
    {"questionNumber": 3, "question": "What is the capital city of Turkey?", "options": ["Istanbul", "Ankara", "Izmir", "Bursa"], "correct": "Ankara"},

    {"questionNumber": 4, "question": "What is the largest country in the world by area?", "options": ["USA", "China", "Russia", "Canada"], "correct": "Russia"},
    {"questionNumber": 4, "question": "Which sea borders Kazakhstan to the west?", "options": ["Caspian Sea", "Black Sea", "Aral Sea", "Baltic Sea"], "correct": "Caspian Sea"},
    {"questionNumber": 4, "question": "Which continent has the highest population density?", "options": ["Europe", "Asia", "Africa", "South America"], "correct": "Asia"},
    {"questionNumber": 4, "question": "Which volcano erupted in 1883?", "options": ["Krakatoa", "Vesuvius", "Etna", "Mount Fuji"], "correct": "Krakatoa"},
    {"questionNumber": 4, "question": "What is the capital of Kazakhstan?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Astana"},
    {"questionNumber": 4, "question": "Which river is the longest in Kazakhstan?", "options": ["Ili", "Irtysh", "Ural", "Syr Darya"], "correct": "Irtysh"},
    {"questionNumber": 4, "question": "Which desert is located in southern Kazakhstan?", "options": ["Kyzylkum", "Gobi", "Karakum", "Sahara"], "correct": "Kyzylkum"},
    {"questionNumber": 4, "question": "Which mountain range is in eastern Kazakhstan?", "options": ["Altai", "Tian Shan", "Himalayas", "Ural"], "correct": "Altai"},
    {"questionNumber": 4, "question": "Which body of water is shrinking due to irrigation?", "options": ["Caspian Sea", "Aral Sea", "Black Sea", "Dead Sea"], "correct": "Aral Sea"},
    {"questionNumber": 4, "question": "What is the largest city in Kazakhstan?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Almaty"},

    {"questionNumber": 5, "question": "Which country has the most natural lakes?", "options": ["Canada", "Finland", "Russia", "USA"], "correct": "Canada"},
    {"questionNumber": 5, "question": "Which river forms part of the Kazakhstan–Russia border?", "options": ["Ural", "Ili", "Irtysh", "Syr Darya"], "correct": "Ural"},
    {"questionNumber": 5, "question": "Which peninsula separates the Black Sea from the Sea of Azov?", "options": ["Crimea", "Balkan", "Scandinavia", "Iberian"], "correct": "Crimea"},
    {"questionNumber": 5, "question": "Which plateau covers much of central Kazakhstan?", "options": ["Kazakh Uplands", "Deccan Plateau", "Colorado Plateau", "Tibetan Plateau"], "correct": "Kazakh Uplands"},
    {"questionNumber": 5, "question": "Which strait connects the Black Sea and the Sea of Marmara?", "options": ["Bosphorus", "Dardanelles", "Malacca", "Magellan"], "correct": "Bosphorus"},
    {"questionNumber": 5, "question": "Which country contains the most volcanoes?", "options": ["Japan", "Indonesia", "USA", "Russia"], "correct": "Indonesia"},
    {"questionNumber": 5, "question": "What is the northernmost capital city?", "options": ["Reykjavik", "Oslo", "Helsinki", "Stockholm"], "correct": "Reykjavik"},
    {"questionNumber": 5, "question": "Which river flows through Almaty?", "options": ["Ili", "Syr Darya", "Irtysh", "Ural"], "correct": "Ili"},
    {"questionNumber": 5, "question": "What is the largest desert in Kazakhstan?", "options": ["Kyzylkum", "Betpak-Dala", "Karakum", "Sahara"], "correct": "Betpak-Dala"},
    {"questionNumber": 5, "question": "Which mountain is the highest in Kazakhstan?", "options": ["Khan Tengri", "Belukha", "Mount Elbrus", "Mount Ararat"], "correct": "Khan Tengri"},

    {"questionNumber": 6, "question": "Which river is considered the longest in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct": "Nile"},
    {"questionNumber": 6, "question": "Which Kazakh city is famous for Charyn Canyon?", "options": ["Almaty", "Astana", "Shymkent", "Aktau"], "correct": "Almaty"},
    {"questionNumber": 6, "question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "correct": "Pacific"},
    {"questionNumber": 6, "question": "What is the southernmost country in Africa?", "options": ["South Africa", "Namibia", "Botswana", "Zimbabwe"], "correct": "South Africa"},
    {"questionNumber": 6, "question": "Which lake is the largest in Kazakhstan?", "options": ["Lake Balkhash", "Caspian Sea", "Aral Sea", "Lake Zaysan"], "correct": "Lake Balkhash"},
    {"questionNumber": 6, "question": "What is the deepest ocean trench?", "options": ["Mariana Trench", "Tonga Trench", "Java Trench", "Kuril Trench"], "correct": "Mariana Trench"},
    {"questionNumber": 6, "question": "Which desert is in western Kazakhstan?", "options": ["Karakum", "Betpak-Dala", "Kyzylkum", "Sahara"], "correct": "Karakum"},
    {"questionNumber": 6, "question": "What is the highest peak in Central Asia?", "options": ["Pik Pobeda", "Khan Tengri", "Belukha", "Peak Lenin"], "correct": "Pik Pobeda"},
    {"questionNumber": 6, "question": "Which river flows into the Aral Sea?", "options": ["Amu Darya", "Syr Darya", "Ural", "Ili"], "correct": "Syr Darya"},
    {"questionNumber": 6, "question": "Which strait connects the Pacific and Arctic Oceans?", "options": ["Bering Strait", "Malacca Strait", "Bosporus", "Magellan"], "correct": "Bering Strait"},

    {"questionNumber": 7, "question": "What is the largest island in the world?", "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"], "correct": "Greenland"},
    {"questionNumber": 7, "question": "Which Kazakh mountain range is part of the Tian Shan?", "options": ["Altai", "Dzungarian Alatau", "Zailiysky Alatau", "Karkaraly"], "correct": "Zailiysky Alatau"},
    {"questionNumber": 7, "question": "Which country has the most time zones?", "options": ["Russia", "USA", "China", "Canada"], "correct": "Russia"},
    {"questionNumber": 7, "question": "Which desert lies on the Kazakhstan–Uzbekistan border?", "options": ["Kyzylkum", "Gobi", "Karakum", "Betpak-Dala"], "correct": "Kyzylkum"},
    {"questionNumber": 7, "question": "Which Kazakh river flows into Lake Balkhash?", "options": ["Ili", "Syr Darya", "Ural", "Emba"], "correct": "Ili"},
    {"questionNumber": 7, "question": "Which plateau is in western Kazakhstan?", "options": ["Ustyurt Plateau", "Kazakh Uplands", "Tian Shan", "Altai"], "correct": "Ustyurt Plateau"},
    {"questionNumber": 7, "question": "What is the longest mountain range in the world?", "options": ["Andes", "Himalayas", "Rockies", "Alps"], "correct": "Andes"},
    {"questionNumber": 7, "question": "Which Kazakh city is closest to the Aral Sea?", "options": ["Aktobe", "Kyzylorda", "Shymkent", "Oral"], "correct": "Kyzylorda"},
    {"questionNumber": 7, "question": "Which river forms part of the Kazakhstan–China border?", "options": ["Ili", "Irtysh", "Ural", "Syr Darya"], "correct": "Ili"},
    {"questionNumber": 7, "question": "Which sea is almost entirely enclosed by land?", "options": ["Caspian Sea", "Black Sea", "Aral Sea", "Baltic Sea"], "correct": "Caspian Sea"},

    {"questionNumber": 8, "question": "Which country has the largest number of islands?", "options": ["Indonesia", "Canada", "Philippines", "Japan"], "correct": "Sweden"},
    {"questionNumber": 8, "question": "Which river passes through Astana?", "options": ["Ishim", "Ili", "Irtysh", "Syr Darya"], "correct": "Ishim"},
    {"questionNumber": 8, "question": "Which is the smallest continent by area?", "options": ["Europe", "Australia", "Antarctica", "South America"], "correct": "Australia"},
    {"questionNumber": 8, "question": "What is the climate of southern Kazakhstan?", "options": ["Tropical", "Continental", "Mediterranean", "Arctic"], "correct": "Continental"},
    {"questionNumber": 8, "question": "Which Kazakh city is a major oil center?", "options": ["Atyrau", "Almaty", "Astana", "Karaganda"], "correct": "Atyrau"},
    {"questionNumber": 8, "question": "What is the highest waterfall in the world?", "options": ["Niagara Falls", "Angel Falls", "Victoria Falls", "Iguazu Falls"], "correct": "Angel Falls"},
    {"questionNumber": 8, "question": "Which ocean touches the eastern coast of Africa?", "options": ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"], "correct": "Indian Ocean"},
    {"questionNumber": 8, "question": "Which Kazakh city is located near the Altai Mountains?", "options": ["Ust-Kamenogorsk", "Almaty", "Astana", "Aktobe"], "correct": "Ust-Kamenogorsk"},
    {"questionNumber": 8, "question": "What is the longest river in Russia?", "options": ["Volga", "Ob", "Lena", "Yenisei"], "correct": "Lena"},
    {"questionNumber": 8, "question": "Which peninsula is in the north of Kazakhstan?", "options": ["Mangyshlak", "Emba", "Ustyurt", "Saryarka"], "correct": "Mangyshlak"},

    {"questionNumber": 9, "question": "Which Kazakh lake has both freshwater and saltwater parts?", "options": ["Lake Balkhash", "Lake Zaysan", "Caspian Sea", "Aral Sea"], "correct": "Lake Balkhash"},
    {"questionNumber": 9, "question": "Which desert in Kazakhstan is semi-arid?", "options": ["Betpak-Dala", "Kyzylkum", "Karakum", "Gobi"], "correct": "Betpak-Dala"},
    {"questionNumber": 9, "question": "Which mountain range is on the Kazakhstan–China border?", "options": ["Tien Shan", "Altai", "Ural", "Himalayas"], "correct": "Tien Shan"},
    {"questionNumber": 9, "question": "Which Kazakh river flows into the Caspian Sea?", "options": ["Ural", "Ili", "Syr Darya", "Irtysh"], "correct": "Ural"},
    {"questionNumber": 9, "question": "Which city is the southernmost in Kazakhstan?", "options": ["Shymkent", "Taraz", "Almaty", "Aktau"], "correct": "Shymkent"},
    {"questionNumber": 9, "question": "What is the largest island in Kazakhstan?", "options": ["Barsa-Kelmes", "Kokaral", "Komsomol", "Vladimir"], "correct": "Barsa-Kelmes"},
    {"questionNumber": 9, "question": "Which Kazakh mountain peak exceeds 7000 meters?", "options": ["Khan Tengri", "Belukha", "Pik Pobeda", "Peak Lenin"], "correct": "Khan Tengri"},
    {"questionNumber": 9, "question": "Which is the coldest inhabited city in Kazakhstan?", "options": ["Petropavl", "Astana", "Karaganda", "Oskemen"], "correct": "Oskemen"},
    {"questionNumber": 9, "question": "Which desert stretches into Uzbekistan from Kazakhstan?", "options": ["Kyzylkum", "Betpak-Dala", "Karakum", "Gobi"], "correct": "Kyzylkum"},
    {"questionNumber": 9, "question": "Which Kazakh city lies on the Irtysh River?", "options": ["Pavlodar", "Semey", "Ust-Kamenogorsk", "Aktobe"], "correct": "Pavlodar"},

    {"questionNumber": 10, "question": "What is the largest steppe in Kazakhstan?", "options": ["Kazakh Steppe", "Ili Steppe", "Ustyurt Steppe", "Betpak-Dala"], "correct": "Kazakh Steppe"},
    {"questionNumber": 10, "question": "Which river is important for irrigation in southern Kazakhstan?", "options": ["Syr Darya", "Ili", "Ural", "Irtysh"], "correct": "Syr Darya"},
    {"questionNumber": 10, "question": "Which Kazakh lake is rapidly shrinking due to water diversion?", "options": ["Aral Sea", "Balkhash", "Zaysan", "Alakol"], "correct": "Aral Sea"},
    {"questionNumber": 10, "question": "Which mountain range separates Kazakhstan from Kyrgyzstan?", "options": ["Tien Shan", "Altai", "Zailiysky Alatau", "Ural"], "correct": "Tien Shan"},
    {"questionNumber": 10, "question": "Which sea is west of Kazakhstan?", "options": ["Caspian Sea", "Aral Sea", "Black Sea", "Baltic Sea"], "correct": "Caspian Sea"},
    {"questionNumber": 10, "question": "What is the largest plateau in Kazakhstan?", "options": ["Ustyurt Plateau", "Kazakh Uplands", "Altai Plateau", "Betpak-Dala Plateau"], "correct": "Kazakh Uplands"},
    {"questionNumber": 10, "question": "Which city in Kazakhstan is a former capital of the Kazakh SSR?", "options": ["Almaty", "Astana", "Semey", "Karaganda"], "correct": "Almaty"},
    {"questionNumber": 10, "question": "Which Kazakh river forms part of the border with China?", "options": ["Ili", "Irtysh", "Syr Darya", "Ural"], "correct": "Ili"},
    {"questionNumber": 10, "question": "Which mountain is considered sacred in Kazakhstan?", "options": ["Kok-Tobe", "Khan Tengri", "Mount Aral", "Belukha"], "correct": "Khan Tengri"},
    {"questionNumber": 10, "question": "Which desert stretches into Uzbekistan from Kazakhstan?", "options": ["Kyzylkum", "Betpak-Dala", "Karakum", "Gobi"], "correct": "Kyzylkum"}
  ],

  "Technology": [

      # questionNumber 1
      {"questionNumber": 1, "question": "Who is known as the father of computers?", "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"], "correct": "Charles Babbage"},
      {"questionNumber": 1, "question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Primary Unit", "Control Processing Unit", "Central Peripheral Unit"], "correct": "Central Processing Unit"},
      {"questionNumber": 1, "question": "Which company created the first smartphone?", "options": ["Apple", "IBM", "Samsung", "Nokia"], "correct": "IBM"},
      {"questionNumber": 1, "question": "What year was the Internet made publicly available?", "options": ["1985", "1989", "1991", "1995"], "correct": "1991"},
      {"questionNumber": 1, "question": "Who founded Microsoft?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"], "correct": "Bill Gates"},
      {"questionNumber": 1, "question": "What is the first Kazakh IT company?", "options": ["Kcell", "KazTech Innovations", "Beeline", "Astana IT"], "correct": "KazTech Innovations"},
      {"questionNumber": 1, "question": "Which programming language is used for AI the most?", "options": ["Python", "C++", "Java", "PHP"], "correct": "Python"},
      {"questionNumber": 1, "question": "What does RAM stand for?", "options": ["Random Access Memory", "Read Access Memory", "Rapid Access Memory", "Run All Memory"], "correct": "Random Access Memory"},
      {"questionNumber": 1, "question": "What is considered the first computer virus?", "options": ["Creeper", "ILOVEYOU", "Melissa", "Code Red"], "correct": "Creeper"},
      {"questionNumber": 1, "question": "Which Kazakh city has the largest tech park?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},

      # questionNumber 2
      {"questionNumber": 2, "question": "What is the main function of an operating system?", "options": ["Manage software", "Run applications", "Manage hardware and software", "Store files"], "correct": "Manage hardware and software"},
      {"questionNumber": 2, "question": "Who invented the World Wide Web?", "options": ["Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Mark Zuckerberg"], "correct": "Tim Berners-Lee"},
      {"questionNumber": 2, "question": "What year was Google founded?", "options": ["1996", "1998", "2000", "2002"], "correct": "1998"},
      {"questionNumber": 2, "question": "Which Kazakh university specializes in IT and robotics?", "options": ["Kazakh-British Technical University", "Nazarbayev University", "Al-Farabi KazNU", "KBTU"], "correct": "KBTU"},
      {"questionNumber": 2, "question": "What is open-source software?", "options": ["Free software with accessible code", "Paid software", "Software for students only", "Proprietary software"], "correct": "Free software with accessible code"},
      {"questionNumber": 2, "question": "Which company owns the Android operating system?", "options": ["Apple", "Google", "Microsoft", "Samsung"], "correct": "Google"},
      {"questionNumber": 2, "question": "What does GPU stand for?", "options": ["Graphics Processing Unit", "General Processing Unit", "Graphical Power Unit", "General Purpose Unit"], "correct": "Graphics Processing Unit"},
      {"questionNumber": 2, "question": "Which Kazakh city hosted the first tech startup festival?", "options": ["Almaty", "Astana", "Karaganda", "Shymkent"], "correct": "Almaty"},
      {"questionNumber": 2, "question": "What year was Facebook launched?", "options": ["2002", "2003", "2004", "2005"], "correct": "2004"},
      {"questionNumber": 2, "question": "What is blockchain technology mainly used for?", "options": ["Cryptocurrency", "AI", "Cloud storage", "Robotics"], "correct": "Cryptocurrency"},

      # questionNumber 3
      {"questionNumber": 3, "question": "Which programming language was created by James Gosling?", "options": ["C++", "Python", "Java", "Ruby"], "correct": "Java"},
      {"questionNumber": 3, "question": "What does IoT stand for?", "options": ["Internet of Things", "Input of Technology", "Intelligent of Things", "Interface of Tech"], "correct": "Internet of Things"},
      {"questionNumber": 3, "question": "Which Kazakh IT company focuses on fintech solutions?", "options": ["Kcell", "Finstar Kazakhstan", "KazTech Innovations", "Beeline"], "correct": "Finstar Kazakhstan"},
      {"questionNumber": 3, "question": "Which device is used to connect to a network wirelessly?", "options": ["Router", "Modem", "Switch", "Access Point"], "correct": "Access Point"},
      {"questionNumber": 3, "question": "What is the primary function of a compiler?", "options": ["Convert code into machine language", "Run applications", "Manage memory", "Store files"], "correct": "Convert code into machine language"},
      {"questionNumber": 3, "question": "Which Kazakh city has a growing AI development hub?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
      {"questionNumber": 3, "question": "What is cloud computing?", "options": ["Storing data on remote servers", "Computing on local PC", "Building a home server", "Downloading games"], "correct": "Storing data on remote servers"},
      {"questionNumber": 3, "question": "Who created Linux?", "options": ["Linus Torvalds", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"], "correct": "Linus Torvalds"},
      {"questionNumber": 3, "question": "Which Kazakh city has the largest number of IT startups?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
      {"questionNumber": 3, "question": "What is 5G technology mainly used for?", "options": ["Faster mobile networks", "Artificial intelligence", "Quantum computing", "Virtual reality"], "correct": "Faster mobile networks"},

      # questionNumber 4
      {"questionNumber": 4, "question": "What is a database?", "options": ["Collection of organized data", "Software application", "Programming language", "Network device"], "correct": "Collection of organized data"},
      {"questionNumber": 4, "question": "Which Kazakh university offers courses in cybersecurity?", "options": ["KBTU", "KazNU", "Nazarbayev University", "Al-Farabi KazNU"], "correct": "Nazarbayev University"},
      {"questionNumber": 4, "question": "Who is the co-founder of Apple?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"], "correct": "Steve Jobs"},
      {"questionNumber": 4, "question": "What is the main purpose of HTML?", "options": ["Create web pages", "Program apps", "Manage databases", "Encrypt data"], "correct": "Create web pages"},
      {"questionNumber": 4, "question": "Which Kazakh city hosts the annual tech expo 'Astana Hub'?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
      {"questionNumber": 4, "question": "What is VR technology used for?", "options": ["Virtual reality experiences", "Video recording", "Voice recognition", "Data storage"], "correct": "Virtual reality experiences"},
      {"questionNumber": 4, "question": "Which programming language is used to develop iOS apps?", "options": ["Swift", "Python", "Java", "C#"], "correct": "Swift"},
      {"questionNumber": 4, "question": "What does SEO stand for?", "options": ["Search Engine Optimization", "Software Engineering Output", "System Execution Order", "Search Entity Output"], "correct": "Search Engine Optimization"},
      {"questionNumber": 4, "question": "What is 3D printing?", "options": ["Creating objects layer by layer", "Digital animation", "Laser cutting", "Robotic assembly"], "correct": "Creating objects layer by layer"},
      {"questionNumber": 4, "question": "Which Kazakh city launched a blockchain-based city project?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

      # questionNumber 5
      {"questionNumber": 5, "question": "What is AI?", "options": ["Artificial Intelligence", "Automated Input", "Advanced Internet", "Algorithm Interface"], "correct": "Artificial Intelligence"},
      {"questionNumber": 5, "question": "Which Kazakh IT company develops e-government solutions?", "options": ["Beeline", "Astana IT", "Zerde", "Kcell"], "correct": "Zerde"},
      {"questionNumber": 5, "question": "Which technology is used for online payments?", "options": ["Fintech", "Blockchain", "VPN", "Cloud Computing"], "correct": "Fintech"},
      {"questionNumber": 5, "question": "What is the main function of a firewall?", "options": ["Protect network from attacks", "Store files", "Encrypt emails", "Connect devices"], "correct": "Protect network from attacks"},
      {"questionNumber": 5, "question": "Which Kazakh city has a tech incubator for startups?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
      {"questionNumber": 5, "question": "Which programming language is used for web backend?", "options": ["PHP", "Python", "JavaScript", "All of the above"], "correct": "All of the above"},
      {"questionNumber": 5, "question": "What is cloud storage?", "options": ["Online data storage", "Local hard drive storage", "Flash drive storage", "External HDD storage"], "correct": "Online data storage"},
      {"questionNumber": 5, "question": "What year was the first computer created?", "options": ["1830", "1843", "1936", "1943"], "correct": "Charles Babbage 1836"},
      {"questionNumber": 5, "question": "Which Kazakh city has an AI lab at Nazarbayev University?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
      {"questionNumber": 5, "question": "What is cybersecurity mainly concerned with?", "options": ["Protecting computers and networks", "Developing apps", "Artificial intelligence", "Designing websites"], "correct": "Protecting computers and networks"},

      # questionNumber 6
      {"questionNumber": 6, "question": "What is the main purpose of an algorithm?", "options": ["Solve problems", "Store data", "Run programs", "Connect networks"], "correct": "Solve problems"},
      {"questionNumber": 6, "question": "Which Kazakh city has a coding school for children?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Almaty"},
      {"questionNumber": 6, "question": "What is machine learning?", "options": ["AI technique to learn from data", "Programming language", "Cloud service", "Database type"], "correct": "AI technique to learn from data"},
      {"questionNumber": 6, "question": "Who developed the first electronic computer?", "options": ["Charles Babbage", "Alan Turing", "John von Neumann", "Steve Jobs"], "correct": "John von Neumann"},
      {"questionNumber": 6, "question": "Which Kazakh company develops AI solutions for healthcare?", "options": ["Astana IT", "KazTech Innovations", "Finstar Kazakhstan", "Beeline"], "correct": "KazTech Innovations"},
      {"questionNumber": 6, "question": "What does VPN stand for?", "options": ["Virtual Private Network", "Visual Private Network", "Virtual Public Network", "Verified Private Network"], "correct": "Virtual Private Network"},
      {"questionNumber": 6, "question": "Which technology is used for digital currency?", "options": ["Blockchain", "Cloud computing", "IoT", "VR"], "correct": "Blockchain"},
      {"questionNumber": 6, "question": "Which programming language is known for data analysis?", "options": ["Python", "C#", "Swift", "HTML"], "correct": "Python"},
      {"questionNumber": 6, "question": "What is augmented reality (AR)?", "options": ["Overlaying digital info on real world", "Virtual gaming", "3D printing", "Cloud computing"], "correct": "Overlaying digital info on real world"},
      {"questionNumber": 6, "question": "Which Kazakh city hosts international IT conferences?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

      # questionNumber 7
      {"questionNumber": 7, "question": "What is the main use of a microprocessor?", "options": ["Process data in a computer", "Store files", "Display graphics", "Connect networks"], "correct": "Process data in a computer"},
      {"questionNumber": 7, "question": "Who is the founder of Tesla and SpaceX?", "options": ["Elon Musk", "Jeff Bezos", "Steve Jobs", "Mark Zuckerberg"], "correct": "Elon Musk"},
      {"questionNumber": 7, "question": "Which Kazakh city launched a robotics center for students?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
      {"questionNumber": 7, "question": "What does HTML stand for?", "options": ["HyperText Markup Language", "HighText Markup Language", "Hyper Tool Markup Language", "HyperText Machine Language"], "correct": "HyperText Markup Language"},
      {"questionNumber": 7, "question": "What is a server?", "options": ["Computer providing services over network", "Programming tool", "Mobile app", "Database"], "correct": "Computer providing services over network"},
      {"questionNumber": 7, "question": "What is SaaS?", "options": ["Software as a Service", "System as a Server", "Security as a Service", "Storage as a Service"], "correct": "Software as a Service"},
      {"questionNumber": 7, "question": "Which Kazakh university offers robotics courses?", "options": ["KBTU", "KazNU", "Nazarbayev University", "Al-Farabi KazNU"], "correct": "KBTU"},
      {"questionNumber": 7, "question": "What is Python mainly used for?", "options": ["Web development, AI, data science", "Gaming only", "Networking only", "Databases only"], "correct": "Web development, AI, data science"},
      {"questionNumber": 7, "question": "Which technology powers virtual assistants like Siri?", "options": ["AI and Natural Language Processing", "Blockchain", "Cloud storage", "IoT"], "correct": "AI and Natural Language Processing"},
      {"questionNumber": 7, "question": "Which Kazakh city has an AI accelerator program?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

      # questionNumber 8
      {"questionNumber": 8, "question": "What is a cloud service provider?", "options": ["Company offering cloud computing", "Software developer", "Hardware manufacturer", "AI startup"], "correct": "Company offering cloud computing"},
      {"questionNumber": 8, "question": "Who created the programming language C?", "options": ["Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"], "correct": "Dennis Ritchie"},
      {"questionNumber": 8, "question": "What does API stand for?", "options": ["Application Programming Interface", "Automated Programming Instruction", "Advanced Program Integration", "Application Process Info"], "correct": "Application Programming Interface"},
      {"questionNumber": 8, "question": "Which Kazakh city opened a cybersecurity training center?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Astana"},
      {"questionNumber": 8, "question": "What is the main feature of IoT?", "options": ["Connect devices via Internet", "Store files locally", "Process offline", "Encrypt emails"], "correct": "Connect devices via Internet"},
      {"questionNumber": 8, "question": "What is edge computing?", "options": ["Data processing near data source", "Cloud computing", "Mobile computing", "Desktop computing"], "correct": "Data processing near data source"},
      {"questionNumber": 8, "question": "Which Kazakh city has an innovation hub for IoT projects?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
      {"questionNumber": 8, "question": "What is cryptocurrency?", "options": ["Digital currency using blockchain", "Physical currency", "Online banking", "Credit card payment"], "correct": "Digital currency using blockchain"},
      {"questionNumber": 8, "question": "Which programming language is used for Android development?", "options": ["Java", "Python", "C#", "Swift"], "correct": "Java"},
      {"questionNumber": 8, "question": "Which Kazakh city promotes smart city projects?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},

      # questionNumber 9
      {"questionNumber": 9, "question": "What is the purpose of machine learning?", "options": ["Learn patterns from data", "Run apps", "Encrypt data", "Store files"], "correct": "Learn patterns from data"},
      {"questionNumber": 9, "question": "Who is the founder of Google?", "options": ["Larry Page", "Bill Gates", "Steve Jobs", "Elon Musk"], "correct": "Larry Page"},
      {"questionNumber": 9, "question": "Which Kazakh city hosts hackathons regularly?", "options": ["Almaty", "Astana", "Shymkent", "Karaganda"], "correct": "Almaty"},
      {"questionNumber": 9, "question": "What is the main function of a database management system (DBMS)?", "options": ["Manage databases", "Develop apps", "Encrypt files", "Run websites"], "correct": "Manage databases"},
      {"questionNumber": 9, "question": "Which Kazakh company develops cloud solutions?", "options": ["KazTech Innovations", "Kcell", "Astana IT", "Beeline"], "correct": "KazTech Innovations"},
      {"questionNumber": 9, "question": "What does SaaS stand for?", "options": ["Software as a Service", "System as a Server", "Storage as a Service", "Security as a Service"], "correct": "Software as a Service"},
      {"questionNumber": 9, "question": "Which programming language is best for AI research?", "options": ["Python", "C++", "Java", "PHP"], "correct": "Python"},
      {"questionNumber": 9, "question": "What is a smart contract?", "options": ["Self-executing contract on blockchain", "Paper contract", "Digital signature", "Cloud document"], "correct": "Self-executing contract on blockchain"},
      {"questionNumber": 9, "question": "Which Kazakh city launched AI-powered public services?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
      {"questionNumber": 9, "question": "What is the main function of a network router?", "options": ["Forward data packets", "Store files", "Run apps", "Encrypt emails"], "correct": "Forward data packets"},

      # questionNumber 10
      {"questionNumber": 10, "question": "What is quantum computing?", "options": ["Computing using quantum bits", "Cloud computing", "Classical computing", "Distributed computing"], "correct": "Computing using quantum bits"},
      {"questionNumber": 10, "question": "Who is the founder of SpaceX?", "options": ["Elon Musk", "Jeff Bezos", "Steve Jobs", "Mark Zuckerberg"], "correct": "Elon Musk"},
      {"questionNumber": 10, "question": "Which Kazakh city established a data science institute?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Almaty"},
      {"questionNumber": 10, "question": "What is deep learning?", "options": ["Subset of machine learning using neural networks", "Cloud computing model", "Programming language", "Database system"], "correct": "Subset of machine learning using neural networks"},
      {"questionNumber": 10, "question": "Which Kazakh university focuses on AI and robotics?", "options": ["KBTU", "KazNU", "Nazarbayev University", "Al-Farabi KazNU"], "correct": "KBTU"},
      {"questionNumber": 10, "question": "What is the main feature of a blockchain?", "options": ["Immutable distributed ledger", "Central database", "Encrypted cloud storage", "Local file system"], "correct": "Immutable distributed ledger"},
      {"questionNumber": 10, "question": "Which programming language is widely used for web frontend?", "options": ["JavaScript", "Python", "Java", "C#"], "correct": "JavaScript"},
      {"questionNumber": 10, "question": "What is a neural network?", "options": ["AI model inspired by the brain", "Database type", "Programming language", "Network device"], "correct": "AI model inspired by the brain"},
      {"questionNumber": 10, "question": "Which Kazakh city runs innovation programs for startups?", "options": ["Astana", "Almaty", "Shymkent", "Karaganda"], "correct": "Astana"},
      {"questionNumber": 10, "question": "What is edge AI?", "options": ["AI processed on devices near data source", "Cloud-based AI", "Robotics AI", "Server AI"], "correct": "AI processed on devices near data source"}

    ]
}


# 5) Insert
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


# 6) Doğrulama logları
cur.execute("SELECT COUNT(*) FROM questions")
count = cur.fetchone()[0]
cur.execute("SELECT category, COUNT(*) FROM questions GROUP BY category")
by_cat = cur.fetchall()

conn.close()
print(f"✔ DB path: {DB_PATH}")
print(f"✔ Toplam satır: {count}")
print(f"✔ Kategori bazında: {by_cat}")