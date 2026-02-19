"use client"
import { useState } from "react"
import Link from "next/link"

export default function LoginForm() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [message, setMessage] = useState("")
  const [error, setError] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    setIsLoading(true)
    try {
      const res = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      })
      const data = await res.json()

      if (data.error) {
        setError(data.error)
        setMessage("")
      } else {
        setMessage(data.message)
        setError("")
        setUsername("")
        setPassword("")
      }
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-purple-700 px-4  ">
      <div className="w-full max-w-md">
        <div className="bg-white p-8 rounded-lg shadow-md text-black">
          <h1 className="text-3xl font-bold text-center mb-6 text-black">Login</h1>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                disabled={isLoading}
              />
            </div>

            <div>
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                disabled={isLoading}
              />
            </div>

            <button
              type="submit"
              className="w-full bg-blue-500 text-white py-2 rounded-lg font-semibold hover:bg-blue-600 disabled:opacity-50"
              disabled={isLoading}
            >
              {isLoading ? "Signing in..." : "Sign In"}
            </button>
          </form>

          {message && <p className="text-green-600 mt-4 text-center">{message}</p>}
          {error && <p className="text-red-600 mt-4 text-center">{error}</p>}

          <p className="text-center mt-6 text-gray-600">
            Don't have an account? <Link href="/sign-up" className="text-blue-500 hover:underline">Sign up</Link>
          </p>
        </div>
      </div>
    </div>
  )
}
