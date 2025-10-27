import React, { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleGenerate = async () => {
    if (!text.trim()) return alert("Please enter a prompt!");
    setLoading(true);
    setResult(null);
    try {
      const res = await axios.post("http://127.0.0.1:5000/generate", { text });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error generating video");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-[#0f172a] to-[#1e293b] text-white relative overflow-hidden">
      {/* Animated background glow */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_20%,rgba(56,189,248,0.3),transparent_60%)] animate-pulse"></div>
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_70%_80%,rgba(147,51,234,0.3),transparent_60%)] animate-pulse"></div>

      {/* Main content */}
      <div className="z-10 text-center w-full max-w-2xl px-6">
        <h1 className="text-4xl md:text-5xl font-bold mb-6 bg-gradient-to-r from-blue-400 via-cyan-300 to-purple-500 bg-clip-text text-transparent">
          Text-to-Video Generator 🎥
        </h1>

        <textarea
          className="w-full p-4 text-gray-900 rounded-xl border border-gray-300 focus:ring-4 focus:ring-cyan-400 focus:outline-none shadow-lg"
          rows="4"
          placeholder="Describe your video idea... (e.g., Naruto Uzumaki training scene)"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button
          onClick={handleGenerate}
          disabled={loading}
          className={`mt-6 px-8 py-3 rounded-full font-semibold text-lg tracking-wide transition-all duration-300 transform 
            ${
              loading
                ? "bg-gray-600 cursor-not-allowed"
                : "bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-blue-600 hover:to-purple-600 hover:scale-105 shadow-lg shadow-blue-800/50"
            }`}
        >
          {loading ? "⚙️ Generating..." : "✨ Generate Video"}
        </button>

        {result && (
          <div className="mt-10 bg-gray-800/60 p-6 rounded-xl shadow-lg backdrop-blur-md border border-gray-700 text-left">
            <h2 className="text-2xl font-semibold mb-2 text-cyan-300">Result:</h2>
            <p className="text-gray-300">{result.message}</p>
            <a
              href="http://127.0.0.1:5000/static/generated_video.mp4"
              target="_blank"
              rel="noopener noreferrer"
              className="block mt-3 text-blue-400 hover:text-purple-400 underline"
            >
              ▶ View Generated Video
            </a>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
