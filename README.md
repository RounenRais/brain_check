"use client";
import { useState, useEffect } from "react";

export default function QuizPage() {
  const [categories, setCategories] = useState<string[]>([]);
  const [questions, setQuestions] = useState<any[]>([]);
  const [selectedCategory, setSelectedCategory] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/categories")
      .then(res => res.json())
      .then(data => setCategories(data.categories));
  }, []);

  const loadQuestions = (category: string) => {
    setSelectedCategory(category);
    fetch(`http://127.0.0.1:8000/questions/${category}`)
      .then(res => res.json())
      .then(data => setQuestions(data.questions));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Quiz Game</h1>

      {!selectedCategory ? (
        <>
          <h2>Select a category:</h2>
          {categories.map(cat => (
            <button
              key={cat}
              onClick={() => loadQuestions(cat)}
              style={{ margin: "5px" }}
            >
              {cat}
            </button>
          ))}
        </>
      ) : (
        <>
          <h2>Category: {selectedCategory}</h2>
          {questions.map((q, i) => (
            <div key={i} style={{ marginBottom: "15px" }}>
              <p>{q.question}</p>
              {q.options.map((opt: string, j: number) => (
                <button key={j} style={{ marginRight: "10px" }}>
                  {opt}
                </button>
              ))}
            </div>
          ))}
        </>
      )}
    </div>


uvicorn main:app --reload
    
  );
}
