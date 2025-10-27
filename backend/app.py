import os
import requests
import traceback
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from gtts import gTTS
from dotenv import load_dotenv
import google.generativeai as genai

# -----------------------------
# 🔹 Load Environment Variables
# -----------------------------
load_dotenv()

# API Keys
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "YOUR_PEXELS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# -----------------------------
# 🔹 Flask App Setup
# -----------------------------
app = Flask(__name__)
CORS(app)

STATIC_DIR = "static"
os.makedirs(STATIC_DIR, exist_ok=True)

PEXELS_URL = "https://api.pexels.com/videos/search"

# -----------------------------
# 🔹 Helper Functions
# -----------------------------
def fetch_videos(query, count=3):
    """Fetch multiple related video clips from Pexels."""
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": count}
    response = requests.get(PEXELS_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    video_links = []
    for v in data.get("videos", []):
        files = sorted(v["video_files"], key=lambda f: f["width"], reverse=True)
        video_links.append(files[0]["link"])
    return video_links


def create_combined_video(query, tts_audio_path):
    """Download multiple Pexels clips, merge, and attach narration audio."""
    urls = fetch_videos(query, count=3)
    clips = []
    temp_files = []

    for i, url in enumerate(urls):
        filename = os.path.join(STATIC_DIR, f"temp_clip_{i}.mp4")
        temp_files.append(filename)
        os.system(f"curl -L -o {filename} {url}")
        clip = VideoFileClip(filename)
        clip = clip.subclip(0, min(10, clip.duration))
        clips.append(clip)

    # Merge all clips
    final_clip = concatenate_videoclips(clips, method="compose")

    # Add audio
    audio_clip = AudioFileClip(tts_audio_path)
    final_clip = final_clip.set_audio(audio_clip)

    # Save output
    output_path = os.path.join(STATIC_DIR, "generated_video.mp4")
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # ✅ Safely close all clips before deleting temp files
    final_clip.close()
    audio_clip.close()
    for c in clips:
        c.close()

    # ✅ Delete temp files safely
    for temp in temp_files:
        try:
            os.remove(temp)
        except Exception as e:
            print(f"⚠ Could not delete {temp}: {e}")

    return output_path


# -----------------------------
# 🔹 Flask Routes
# -----------------------------
@app.route("/")
def home():
    return "<h2>✅ Gemini + TTS + Pexels Video API is running successfully!</h2>"


@app.route("/generate", methods=["POST"])
def generate_video():
    try:
        data = request.get_json()
        prompt = data.get("text", "").strip()

        if not prompt:
            return jsonify({"error": "Text prompt is required"}), 400

        # Step 1️⃣: Generate cinematic description from Gemini
        model = genai.GenerativeModel("gemini-2.0-flash")
        description = model.generate_content(
            f"Create a cinematic, vivid scene description for: {prompt}"
        ).text

        # Step 2️⃣: Generate TTS narration
        tts_path = os.path.join(STATIC_DIR, "narration.mp3")
        tts = gTTS(description)
        tts.save(tts_path)

        # Step 3️⃣: Create combined video with narration
        output_path = create_combined_video(prompt, tts_path)

        return jsonify({
            "status": "success",
            "prompt": prompt,
            "description": description,
            "message": "🎬 Video generated successfully!",
            "video_url": f"http://127.0.0.1:5000/static/generated_video.mp4"
        })

    except Exception as e:
        print("❌ Error occurred:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)


# -----------------------------
# 🔹 Run Flask Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)