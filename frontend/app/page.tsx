"use client";
import { useState, useEffect, useMemo } from "react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

type Question = {
  questionNumber: number;
  question: string;
  options: string[];
  correct: string;
};

export default function QuizPage() {
  const [categories, setCategories] = useState<string[]>([]);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<null | "dogru" | "yanlis">(null);

  // Kategorileri çek
  useEffect(() => {
    (async () => {
      try {
        setErr(null);
        const res = await fetch(`${API}/categories`);
        if (!res.ok) throw new Error(`/categories ${res.status}`);
        const data = await res.json();
        setCategories(data.categories || []);
      } catch (e: any) {
        setErr(e.message || "Kategori yüklenirken hata oluştu.");
      }
    })();
  }, []);

  // Seçilen kategorinin sorularını çek
  const loadQuestions = async (category: string) => {
    try {
      setSelectedCategory(category);
      setLoading(true);
      setErr(null);
      setFeedback(null);
      const cat = encodeURIComponent(category);
      const res = await fetch(`${API}/questions/${cat}`);
      if (!res.ok) throw new Error(`questions/${category} ${res.status}`);
      const data = await res.json();
      const qs: Question[] = (data.questions || []).sort(
        (a: Question, b: Question) => (a.questionNumber ?? 0) - (b.questionNumber ?? 0)
      );
      setQuestions(qs);
      setCurrentIndex(0);
    } catch (e: any) {
      setErr(e.message || "Sorular yüklenirken hata oluştu.");
      setQuestions([]);
      setCurrentIndex(0);
    } finally {
      setLoading(false);
    }
  };

  // Şu anki soru
  const currentQ = useMemo(() => questions[currentIndex], [questions, currentIndex]);

  // Cevap kontrolü
  const handleAnswer = (opt: string) => {
    if (!currentQ) return;

    if (opt === currentQ.correct) {
      setFeedback("dogru");
      // küçük bir gecikmeyle sonraki soruya geç
      setTimeout(() => {
        setFeedback(null);
        if (currentIndex + 1 < questions.length) {
          setCurrentIndex((i) => i + 1);
        } else {
          // bitti
          alert("Tebrikler! Bu kategorideki tüm soruları bitirdin 🎉");
          // istersen otomatik sıfırlayabilir veya kategorilere dönebilirsin:
          setSelectedCategory(""); // kategorilere dön
          setQuestions([]);
          setCurrentIndex(0);
        }
      }, 400);
    } else {
      setFeedback("yanlis");
      // yanlışta sıfırla
      setTimeout(() => {
        setFeedback(null);
        setCurrentIndex(0);
      }, 400);
    }
  };

  const restartCategory = () => {
    setCurrentIndex(0);
    setFeedback(null);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Quiz Game</h1>

      {err && (
        <p style={{ color: "red" }}>
          Hata: {err} — Konsolda ayrıntıya bak (F12 → Console/Network).
        </p>
      )}

      {!selectedCategory ? (
        <>
          <h2>Kategori seç:</h2>
          {categories.length === 0 && <p>Kategori bulunamadı.</p>}
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => loadQuestions(cat)}
              style={{ margin: 5 }}
            >
              {cat}
            </button>
          ))}
        </>
      ) : (
        <>
          <div style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 10 }}>
            <button onClick={() => setSelectedCategory("")}>← Kategorilere Dön</button>
            <strong>Kategori:</strong> {selectedCategory}
            {questions.length > 0 && (
              <span style={{ marginLeft: "auto" }}>
                Soru {questions.length ? currentIndex + 1 : 0}/{questions.length}
              </span>
            )}
          </div>

          {loading && <p>Yükleniyor…</p>}

          {!loading && questions.length === 0 && (
            <p>Bu kategoride soru bulunamadı.</p>
          )}

          {!loading && currentQ && (
            <div
              style={{
                border: "1px solid #ddd",
                borderRadius: 8,
                padding: 16,
                maxWidth: 700,
              }}
            >
              <p style={{ fontWeight: 600, marginBottom: 12 }}>
                {currentQ.question}
              </p>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 10 }}>
                {currentQ.options.map((opt, j) => (
                  <button
                    key={j}
                    onClick={() => handleAnswer(opt)}
                    disabled={!!feedback}
                    style={{
                      padding: "8px 12px",
                      borderRadius: 6,
                      border: "1px solid #ccc",
                      cursor: feedback ? "not-allowed" : "pointer",
                      background:
                        feedback && opt === currentQ.correct
                          ? "#d4edda"
                          : "#fff",
                    }}
                  >
                    {opt}
                  </button>
                ))}
              </div>

              {feedback === "dogru" && (
                <p style={{ color: "green", marginTop: 10 }}>Doğru! ✅</p>
              )}
              {feedback === "yanlis" && (
                <p style={{ color: "crimson", marginTop: 10 }}>
                  Yanlış! ⚠️ Baştan başlıyorsun.
                </p>
              )}

              <div style={{ marginTop: 12 }}>
                <button onClick={restartCategory}>Baştan Başla</button>
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
}
