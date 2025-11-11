"use client";
import { useEffect, useMemo, useState, useCallback, useRef } from "react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";
const DURATION_MS = 7000; // her soru için 7 saniye

type Question = {
  questionNumber: number;
  question: string;
  options: string[];
  correct: string;
};

export default function QuizPage() {
  const [categories, setCategories] = useState<string[]>([]);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>("");
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<null | "dogru" | "yanlis">(null);

  // setTimeout sızıntılarına karşı (cevap sonrası kısa gecikme)
  const timerRef = useRef<number | null>(null);
  const clearAnswerTimer = () => {
    if (timerRef.current) {
      clearTimeout(timerRef.current);
      timerRef.current = null;
    }
  };

  // Geri sayım için rAF id'si ve kalan süre
  const rafRef = useRef<number | null>(null);
  const [timeLeft, setTimeLeft] = useState<number>(DURATION_MS);
  const clearCountdown = () => {
    if (rafRef.current) {
      cancelAnimationFrame(rafRef.current);
      rafRef.current = null;
    }
  };

  // Kategorileri çek
  useEffect(() => {
    const ac = new AbortController();
    (async () => {
      try {
        setError(null);
        const res = await fetch(`${API}/categories`, {
          signal: ac.signal,
          cache: "no-store",
        });
        if (!res.ok) throw new Error(`/categories ${res.status}`);
        const data = await res.json();
        setCategories(Array.isArray(data?.categories) ? data.categories : []);
      } catch (e:any) {
        if (e?.name !== "AbortError") {
          setError(e?.message || "Error loading categories.");
        }
      }
    })();
    return () => ac.abort();
  }, []);

  // Seçilen kategorinin sorularını çek
  const loadQuestions = useCallback(async (category: string) => {
    const ac = new AbortController();
    try {
      setSelectedCategory(category);
      setLoading(true);
      setError(null);
      setFeedback(null);
      clearAnswerTimer();
      clearCountdown();

      const res = await fetch(`${API}/questions/${encodeURIComponent(category)}`, {
        signal: ac.signal,
        cache: "no-store",
      });
      if (!res.ok) throw new Error(`/questions/${category} ${res.status}`);

      const data = await res.json();
      const qs: Question[] = (data?.questions ?? []).sort(
        (a: Question, b: Question) => (a?.questionNumber ?? 0) - (b?.questionNumber ?? 0)
      );
      setQuestions(qs);
      setCurrentIndex(0);
    } catch (e: any) {
      if (e?.name !== "AbortError") {
        setError(e?.message || "Sorular yüklenirken hata oluştu.");
        setQuestions([]);
        setCurrentIndex(0);
      }
    } finally {
      setLoading(false);
    }
  }, []);

  // Şu anki soru
  const currentQ = useMemo(() => questions[currentIndex], [questions, currentIndex]);

  // Her yeni soruda 7 sn'lik sayaç başlat (feedback gösterilirken sayaç durur)
  useEffect(() => {
    // Sayaç sadece soru görünür ve feedback yokken çalışsın
    if (!selectedCategory || !currentQ || feedback) {
      clearCountdown();
      return;
    }

    setTimeLeft(DURATION_MS);
    const start = performance.now();

    const tick = (now: number) => {
      const elapsed = now - start;
      const remaining = Math.max(0, DURATION_MS - elapsed);
      setTimeLeft(remaining);

      if (remaining === 0) {
        // süre bitti -> yanlış say ve başa dön
        setFeedback("yanlis");
        clearCountdown();
        timerRef.current = window.setTimeout(() => {
          setFeedback(null);
          setCurrentIndex(0);
        }, 400);
        return;
      }

      rafRef.current = requestAnimationFrame(tick);
    };

    rafRef.current = requestAnimationFrame(tick);

    return () => clearCountdown();
  }, [selectedCategory, currentQ, feedback]);

  // Cevap kontrolü
  const handleAnswer = useCallback(
    (opt: string) => {
      if (!currentQ) return;

      clearAnswerTimer();
      clearCountdown();

      if (opt === currentQ.correct) {
        setFeedback("dogru");
        timerRef.current = window.setTimeout(() => {
          setFeedback(null);
            if(currentIndex>=9){
            alert("Congratulations! You have completed all the questions in this category 🎉");
            setSelectedCategory("");
            setQuestions([]);
            setCurrentIndex(0);
          } 
          else if (currentIndex + 1 < questions.length) {
            setCurrentIndex((i) => i + 1);
          }

          else {
            alert("Congratulations! You have completed all the questions in this category 🎉");
            setSelectedCategory("");
            setQuestions([]);
            setCurrentIndex(0);
          }
        }, 400);
      } else {
        setFeedback("yanlis");
        timerRef.current = window.setTimeout(() => {
          setFeedback(null);
          setCurrentIndex(0);
        }, 400);
      }
    },
    [currentQ, currentIndex, questions.length]
  );

  const restartCategory = useCallback(() => {
    clearAnswerTimer();
    clearCountdown();
    setCurrentIndex(0);
    setFeedback(null);
    setTimeLeft(DURATION_MS);
  }, []);

  // Unmount temizlik
  useEffect(() => () => {
    clearAnswerTimer();
    clearCountdown();
  }, []);

  const progress = Math.max(0, Math.min(1, timeLeft / DURATION_MS));

  return (
    <div className="min-h-screen bg-purple-700 text-purple-50">
      <div className="mx-auto flex min-h-screen max-w-4xl flex-col items-center justify-center px-5 py-10">
        <h1 className="mb-4 text-center text-3xl font-extrabold tracking-tight">Quiz Game</h1>

        {error && (
          <p className="mb-4 w-full max-w-2xl rounded-md border border-red-200 bg-red-50 p-3 text-sm text-red-700">
            Hata: {error} — Konsolda ayrıntıya bak (F12 → Console/Network).
          </p>
        )}

        {!selectedCategory ? (
          <section className="w-full max-w-2xl text-center">
            <h2 className="mb-4 text-lg font-semibold">Choose Category:</h2>

            {categories.length === 0 && (
              <p className="text-sm/6 text-purple-100/90">No categories found.</p>
            )}

            <div className="mx-auto flex flex-wrap justify-center gap-2">
              {categories.map((cat) => (
                <button
                  key={cat}
                  onClick={() => loadQuestions(cat)}
                  className="rounded-xl border border-white/20 bg-white/10 px-4 py-2 text-sm font-medium text-white backdrop-blur transition hover:bg-white/20 active:translate-y-px"
                >
                  {cat}
                </button>
              ))}
            </div>
          </section>
        ) : (
          <section className="w-full max-w-2xl">
            {/* Üst bar */}
            <div className="mb-3 flex items-center gap-2 text-purple-100">
              <button
                onClick={() => {
                  setSelectedCategory("");
                  clearAnswerTimer();
                  clearCountdown();
                }}
                className="rounded-md border border-white/20 bg-white/10 px-3 py-1.5 text-sm font-medium text-white backdrop-blur transition hover:bg-white/20"
              >
                ← Back to Categories
              </button>

              <span className="text-sm"><span className="font-semibold">Category:</span> {selectedCategory}</span>

              {questions.length > 0 && (
                <span className="ml-auto text-sm text-purple-100/80">
                  Soru {questions.length ? currentIndex + 1 : 0}/{questions.length}
                </span>
              )}
            </div>

            {/* Sayaç barı */}
            <div className="mb-4 h-2 w-full overflow-hidden rounded-full bg-green-200/40">
              <div
                className="h-full bg-green-500"
                style={{ width: `${progress * 100}%` }}
              />
            </div>

            {loading && (
              <p className="text-center text-sm text-purple-100/90">Yükleniyor…</p>
            )}

            {!loading && questions.length === 0 && (
              <p className="text-center text-sm text-purple-100/90">There is no question in this category.</p>
            )}

            {!loading && currentQ && (
              <div className="mx-auto max-w-lg rounded-2xl border border-white/10 bg-white p-6 text-gray-900 shadow-xl">
                <p className="mb-5 text-center text-lg font-semibold">{currentQ.question}</p>

                <div className="mx-auto flex max-w-xl flex-wrap items-center justify-center gap-2 text-center">
                  {currentQ.options.map((opt, j) => {
                    const isCorrect = opt === currentQ.correct;
                    const showCorrect = !!feedback && isCorrect;
                    return (
                      <button
                        key={j}
                        onClick={() => handleAnswer(opt)}
                        disabled={!!feedback}
                        className={[
                          "min-w-40 rounded-xl border px-4 py-2 text-sm font-medium shadow-sm transition",
                          feedback
                            ? "cursor-not-allowed opacity-100"
                            : "hover:bg-gray-50 active:translate-y-px",
                          showCorrect
                            ? "border-green-300 bg-green-100 text-green-900"
                            : "border-gray-300 bg-white text-gray-900",
                        ].join(" ")}
                      >
                        {opt}
                      </button>
                    );
                  })}
                </div>

                {feedback === "dogru" && (
                  <p className="mt-4 text-center text-sm font-medium text-green-600">Correct! </p>
                )}
                {feedback === "yanlis" && (
                  <p className="mt-4 text-center text-sm font-medium text-rose-600">Wrong Answer/Times Up</p>
                )}


              </div>
            )}
          </section>
        )}
      </div>
    </div>
  );
}
