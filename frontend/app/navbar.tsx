"use client";

import Link from "next/link";
import { useSyncExternalStore } from "react";

const USER_KEY = "brain_check_username";
const AUTH_EVENT = "brain-check-auth-changed";

function subscribe(onStoreChange: () => void) {
  if (typeof window === "undefined") {
    return () => {};
  }

  const handler = () => onStoreChange();
  window.addEventListener("storage", handler);
  window.addEventListener(AUTH_EVENT, handler);

  return () => {
    window.removeEventListener("storage", handler);
    window.removeEventListener(AUTH_EVENT, handler);
  };
}

function getSnapshot() {
  if (typeof window === "undefined") return "";
  return window.localStorage.getItem(USER_KEY) || "";
}

export default function Navbar() {
  const username = useSyncExternalStore(subscribe, getSnapshot, () => "");

  const handleSignOut = () => {
    if (typeof window === "undefined") return;
    window.localStorage.removeItem(USER_KEY);
    window.dispatchEvent(new Event(AUTH_EVENT));
  };

  return (
    <nav className="flex items-center justify-between bg-purple-700 px-2 py-2 text-white">
      <div className="home">
        <Link href="/">Home</Link>
      </div>

      {username ? (
        <div className="flex items-center gap-3">
          <div className="text-sm font-medium">Welcome, {username}</div>
          <button
            type="button"
            onClick={handleSignOut}
            className="rounded-md border border-white/30 px-3 py-1 text-sm hover:bg-white/10"
          >
            Sign Out
          </button>
        </div>
      ) : (
        <div className="flex gap-5">
          <Link href="/log-in">LogIn</Link>
          <Link href="/sign-up">SignUp</Link>
        </div>
      )}
    </nav>
  );
}
