"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";
const DURATION_MS = 7000;
const USER_KEY = "brain_check_username";
const AUTH_EVENT = "brain-check-auth-changed";

const isAbortError = (error: unknown) => {
  return !!error && typeof error === "object" && "name" in error && (error as { name?: unknown }).name === "AbortError";
};

const getErrorMessage = (error: unknown, fallback: string) => {
  if (error && typeof error === "object" && "message" in error) {
    const message = (error as { message?: unknown }).message;
    if (typeof message === "string" && message.trim()) return message;
  }
  return fallback;
};

type ApiQuestion = {
  question_number?: number;
  questionNumber?: number;
  question: string;
  options: string[];
  correct: string;
};

type Question = {
  questionNumber: number;
  question: string;
  options: string[];
  correct: string;
};

type LeaderboardRow = {
  username: string;
  best_score: number;
  attempts: number;
  last_played?: string;
};

export default function QuizPage() {
  const [categories, setCategories] = useState<string[]>([]);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>("");
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<null | "dogru" | "yanlis">(null);
  const [timeLeft, setTimeLeft] = useState<number>(DURATION_MS);
  const [username, setUsername] = useState<string>("");
  const [runScore, setRunScore] = useState<number>(0);
  const [saveStatus, setSaveStatus] = useState<string | null>(null);

  const [leaderboardCategory, setLeaderboardCategory] = useState<string>("");
  const [leaderboardRows, setLeaderboardRows] = useState<LeaderboardRow[]>([]);
  const [leaderboardLoading, setLeaderboardLoading] = useState<boolean>(false);
  const [leaderboardError, setLeaderboardError] = useState<string | null>(null);

  const timerRef = useRef<number | null>(null);
  const rafRef = useRef<number | null>(null);

  const clearAnswerTimer = () => {
    if (timerRef.current) {
      clearTimeout(timerRef.current);
      timerRef.current = null;
    }
  };

  const clearCountdown = () => {
    if (rafRef.current) {
      cancelAnimationFrame(rafRef.current);
      rafRef.current = null;
    }
  };

  const resetQuizState = useCallback(() => {
    clearAnswerTimer();
    clearCountdown();
    setSelectedCategory("");
    setQuestions([]);
    setCurrentIndex(0);
    setFeedback(null);
    setRunScore(0);
    setTimeLeft(DURATION_MS);
  }, []);

  const fetchLeaderboard = useCallback(async (category: string) => {
    if (!category) {
      setLeaderboardRows([]);
      return;
    }

    try {
      setLeaderboardLoading(true);
      setLeaderboardError(null);
      const res = await fetch(`${API}/leaderboard/${encodeURIComponent(category)}`, {
        cache: "no-store",
      });
      const data = await res.json();

      if (!res.ok || data?.error) {
        throw new Error(data?.error || `Leaderboard request failed (${res.status})`);
      }

      setLeaderboardRows(Array.isArray(data?.leaderboard) ? data.leaderboard : []);
    } catch (e: unknown) {
      setLeaderboardRows([]);
      setLeaderboardError(getErrorMessage(e, "Leaderboard could not be loaded."));
    } finally {
      setLeaderboardLoading(false);
    }
  }, []);

  const submitScore = useCallback(
    async (category: string, score: number) => {
      const activeUser = username || (typeof window !== "undefined" ? window.localStorage.getItem(USER_KEY) || "" : "");

      if (!activeUser) {
        setSaveStatus("Score was not saved. Please log in first.");
        return;
      }

      try {
        setSaveStatus(null);
        const res = await fetch(`${API}/add_score`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username: activeUser, score, category }),
        });
        const data = await res.json();

        if (!res.ok || data?.error) {
          throw new Error(data?.error || `Score save failed (${res.status})`);
        }

        setSaveStatus(`Score saved for ${activeUser}: ${score}`);
        if (leaderboardCategory && leaderboardCategory.toLowerCase() === category.toLowerCase()) {
          void fetchLeaderboard(category);
        }
      } catch (e: unknown) {
        setSaveStatus(getErrorMessage(e, "Score could not be saved."));
      }
    },
    [fetchLeaderboard, leaderboardCategory, username]
  );

  useEffect(() => {
    if (typeof window === "undefined") return;
    const syncUser = () => {
      setUsername(window.localStorage.getItem(USER_KEY) || "");
    };

    syncUser();
    window.addEventListener("storage", syncUser);
    window.addEventListener(AUTH_EVENT, syncUser);

    return () => {
      window.removeEventListener("storage", syncUser);
      window.removeEventListener(AUTH_EVENT, syncUser);
    };
  }, []);

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
        const nextCategories = Array.isArray(data?.categories) ? data.categories : [];
        setCategories(nextCategories);
        setLeaderboardCategory((prev) => prev || nextCategories[0] || "");
      } catch (e: unknown) {
        if (!isAbortError(e)) {
          setError(getErrorMessage(e, "Error loading categories."));
        }
      }
    })();
    return () => ac.abort();
  }, []);

  useEffect(() => {
    if (!leaderboardCategory) return;
    void fetchLeaderboard(leaderboardCategory);
  }, [fetchLeaderboard, leaderboardCategory]);

  const loadQuestions = useCallback(async (category: string) => {
    const ac = new AbortController();
    try {
      setSelectedCategory(category);
      setLeaderboardCategory(category);
      setLoading(true);
      setError(null);
      setFeedback(null);
      setRunScore(0);
      setSaveStatus(null);
      clearAnswerTimer();
      clearCountdown();

      const res = await fetch(`${API}/questions/${encodeURIComponent(category)}`, {
        signal: ac.signal,
        cache: "no-store",
      });
      if (!res.ok) throw new Error(`/questions/${category} ${res.status}`);

      const data = await res.json();
      const qs: Question[] = (data?.questions ?? [])
        .map((q: ApiQuestion) => ({
          questionNumber: q.questionNumber ?? q.question_number ?? 0,
          question: q.question,
          options: Array.isArray(q.options) ? q.options : [],
          correct: q.correct,
        }))
        .sort((a: Question, b: Question) => (a.questionNumber ?? 0) - (b.questionNumber ?? 0));

      setQuestions(qs);
      setCurrentIndex(0);
      setTimeLeft(DURATION_MS);
    } catch (e: unknown) {
      if (!isAbortError(e)) {
        setError(getErrorMessage(e, "Questions could not be loaded."));
        setQuestions([]);
        setCurrentIndex(0);
      }
    } finally {
      setLoading(false);
    }
  }, []);

  const currentQ = useMemo(() => questions[currentIndex], [questions, currentIndex]);

  useEffect(() => {
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
        setFeedback("yanlis");
        clearCountdown();
        timerRef.current = window.setTimeout(() => {
          setFeedback(null);
          setCurrentIndex(0);
          setRunScore(0);
        }, 400);
        return;
      }

      rafRef.current = requestAnimationFrame(tick);
    };

    rafRef.current = requestAnimationFrame(tick);

    return () => clearCountdown();
  }, [selectedCategory, currentQ, feedback]);

  const handleAnswer = useCallback(
    (opt: string) => {
      if (!currentQ) return;

      clearAnswerTimer();
      clearCountdown();

      if (opt === currentQ.correct) {
        const nextScore = runScore + 1;
        setRunScore(nextScore);
        setFeedback("dogru");

        timerRef.current = window.setTimeout(() => {
          setFeedback(null);

          const isLastQuestion = currentIndex >= questions.length - 1;
          if (isLastQuestion) {
            if (selectedCategory) {
              void submitScore(selectedCategory, nextScore);
            }
            alert("Congratulations! You have completed all the questions in this category.");
            resetQuizState();
            return;
          }

          setCurrentIndex((i) => i + 1);
        }, 400);
      } else {
        setFeedback("yanlis");
        timerRef.current = window.setTimeout(() => {
          setFeedback(null);
          setCurrentIndex(0);
          setRunScore(0);
        }, 400);
      }
    },
    [currentQ, currentIndex, questions.length, resetQuizState, runScore, selectedCategory, submitScore]
  );

  const restartCategory = useCallback(() => {
    clearAnswerTimer();
    clearCountdown();
    setCurrentIndex(0);
    setFeedback(null);
    setRunScore(0);
    setTimeLeft(DURATION_MS);
  }, []);

  useEffect(
    () => () => {
      clearAnswerTimer();
      clearCountdown();
    },
    []
  );

  const progress = Math.max(0, Math.min(1, timeLeft / DURATION_MS));

  return (
    <div className="min-h-screen bg-purple-700 text-purple-50">
      <div className="mx-auto flex min-h-screen max-w-4xl flex-col items-center justify-center px-5 py-10">
        <h1 className="mb-2 text-center text-3xl font-extrabold tracking-tight">Quiz Game</h1>

        <p className="mb-6 text-sm text-purple-100/90">
          {username ? (
            <>Welcome, <span className="font-semibold text-white">{username}</span></>
          ) : (
            <>
              You are not logged in. <Link href="/log-in" className="underline">Login</Link> to save scores.
            </>
          )}
        </p>

        {saveStatus && (
          <p className="mb-4 w-full max-w-2xl rounded-md border border-white/20 bg-white/10 p-3 text-sm text-white">
            {saveStatus}
          </p>
        )}

        {error && (
          <p className="mb-4 w-full max-w-2xl rounded-md border border-red-200 bg-red-50 p-3 text-sm text-red-700">
            Error: {error}
          </p>
        )}

        {!selectedCategory ? (
          <section className="w-full max-w-2xl text-center">
            <h2 className="mb-4 text-lg font-semibold">Choose Category</h2>

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

            <div className="mt-8 rounded-2xl border border-white/15 bg-white/10 p-5 text-left backdrop-blur">
              <div className="mb-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                <h3 className="text-lg font-semibold text-white">Leaderboard</h3>
                <select
                  value={leaderboardCategory}
                  onChange={(e) => setLeaderboardCategory(e.target.value)}
                  className="rounded-md border border-white/20 bg-purple-800/80 px-3 py-2 text-sm text-white outline-none"
                  disabled={categories.length === 0}
                >
                  {categories.map((cat) => (
                    <option key={cat} value={cat}>
                      {cat}
                    </option>
                  ))}
                </select>
              </div>

              {leaderboardLoading && (
                <p className="text-sm text-purple-100/90">Loading leaderboard...</p>
              )}

              {leaderboardError && !leaderboardLoading && (
                <p className="text-sm text-rose-200">{leaderboardError}</p>
              )}

              {!leaderboardLoading && !leaderboardError && leaderboardRows.length === 0 && leaderboardCategory && (
                <p className="text-sm text-purple-100/90">No scores yet for this category.</p>
              )}

              {!leaderboardLoading && leaderboardRows.length > 0 && (
                <div className="space-y-2">
                  {leaderboardRows.map((row, index) => (
                    <div
                      key={`${row.username}-${index}`}
                      className="flex items-center justify-between rounded-lg border border-white/10 bg-white/5 px-3 py-2 text-sm"
                    >
                      <div className="flex items-center gap-3">
                        <span className="w-6 text-center font-semibold text-white">{index + 1}</span>
                        <span className="text-purple-50">{row.username}</span>
                      </div>
                      <div className="flex items-center gap-3 text-purple-100/90">
                        <span>Best: {row.best_score}</span>
                        <span>Attempts: {row.attempts}</span>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </section>
        ) : (
          <section className="w-full max-w-2xl">
            <div className="mb-3 flex flex-wrap items-center gap-2 text-purple-100">
              <button
                onClick={resetQuizState}
                className="rounded-md border border-white/20 bg-white/10 px-3 py-1.5 text-sm font-medium text-white backdrop-blur transition hover:bg-white/20"
              >
                Back to Categories
              </button>

              <span className="text-sm"><span className="font-semibold">Category:</span> {selectedCategory}</span>
              <span className="text-sm"><span className="font-semibold">Score:</span> {runScore}</span>

              {questions.length > 0 && (
                <span className="ml-auto text-sm text-purple-100/80">
                  Question {questions.length ? currentIndex + 1 : 0}/{questions.length}
                </span>
              )}
            </div>

            <div className="mb-4 h-2 w-full overflow-hidden rounded-full bg-green-200/40">
              <div className="h-full bg-green-500" style={{ width: `${progress * 100}%` }} />
            </div>

            {loading && <p className="text-center text-sm text-purple-100/90">Loading...</p>}

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
                  <p className="mt-4 text-center text-sm font-medium text-green-600">Correct!</p>
                )}
                {feedback === "yanlis" && (
                  <p className="mt-4 text-center text-sm font-medium text-rose-600">Wrong answer / Time is up</p>
                )}

                <div className="mt-4 flex justify-center">
                  <button
                    type="button"
                    onClick={restartCategory}
                    className="rounded-md border border-gray-300 px-3 py-1.5 text-sm font-medium text-gray-700 hover:bg-gray-50"
                  >
                    Restart Category
                  </button>
                </div>
              </div>
            )}
          </section>
        )}
      </div>
    </div>
  );
}
