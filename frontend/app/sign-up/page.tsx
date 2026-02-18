"use client";
import { useState } from "react";
import { redirect } from "next/navigation";
export default function SignUp() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e:React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if(!username||!password||!email){
        setError("Sections cant be empty")
    }
    else{

  
    const res = await fetch("http://localhost:8000/sign_up", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username,mail: email, password }),
    });
    const data = await res.json();

    if (data.error) {
      setError(data.error);
      setMessage("");
    } else {
      setMessage(data.message);
      setError("");
      redirect("/log-in")
    }  }
        setEmail("")
    setUsername("")
    setPassword("")
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">Login</button>
      </form>

      {message && <p style={{ color: "green" }}>{message}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
