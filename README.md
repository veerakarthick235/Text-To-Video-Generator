# 🧠 AI Text-to-Video Generator 🎥  

**AI Text-to-Video Generator** is a full-stack project that transforms text prompts into short AI-generated videos.  
It uses **Flask (Python)** as the backend, **React (JavaScript)** for the frontend, and integrates with **Pexels API** for generating background visuals.  

---

## 🚀 Features  

- 📝 Convert text descriptions into short, themed videos  
- 🎨 AI-inspired futuristic UI with glowing gradient design  
- ⚡ Fast Flask API integration  
- 🌐 Frontend built with React + TailwindCSS  
- 📦 Easy local setup & execution  
- 🔒 CORS & error handling for smooth API communication  

---

## 🧩 Tech Stack  

| Layer | Technology |
|--------|-------------|
| **Frontend** | React.js, TailwindCSS |
| **Backend** | Flask (Python) |
| **API Integration** | Pexels API |
| **Styling** | Gradient + Animated UI |
| **Language** | JavaScript, Python |

---

## 📂 Project Structure  

```
Gemini_Text2Video_FullStack/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── static/
│   │   └── generated_video.mp4
│   └── templates/ (optional)
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── index.css
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

---

## ⚙️ Installation Steps  

### 🖥️ 1. Clone the Repository  

```bash
git clone https://github.com/your-username/AI-Text2Video-Generator.git
cd AI-Text2Video-Generator
```

---

### 🧠 2. Backend Setup (Flask)  

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # On Windows
# or source venv/bin/activate for macOS/Linux

pip install -r requirements.txt
python app.py
```

🟢 Flask backend will run at:  
`http://127.0.0.1:5000`

---

### 💻 3. Frontend Setup (React)  

```bash
cd ../frontend
npm install
npm start
```

🟢 React frontend will run at:  
`http://localhost:3000`

---

## 🔑 Pexels API Setup  

1. Visit [Pexels Developers](https://www.pexels.com/api/)  
2. Create an account (free)  
3. Click **"Get API Key"**  
4. Copy your API key  
5. In your `app.py`, add:

   ```python
   PEXELS_API_KEY = "your_api_key_here"
   ```

6. Restart the Flask server  

---

## 🧪 Usage  

1. Open your browser at `http://localhost:3000`  
2. Enter a description (e.g., “Naruto Uzumaki training in a forest”)  
3. Click **✨ Generate Video**  
4. Wait for generation → click **▶ View Video** to watch  

---

## 🌌 Preview  

| UI | Description |
|----|--------------|
| ![UI Screenshot](assets/ui-preview.png) | AI-Themed Interface |
| ![Video Example](assets/video-preview.gif) | Generated Short Video |

---

## 🧱 Future Enhancements  

- 🧬 Add OpenAI Video or Stability AI integration for direct AI rendering  
- 🔉 Add background music or narration using ElevenLabs API  
- 💾 Add database for saving generated videos  
- 🌈 Introduce multiple style themes  

---

## 🧑‍💻 Author  

**Veera Karthick**  
_AI & Data Science Student | Passionate about solving real-world problems_  

📧 **Contact:** veerakarthick.dev@example.com  
🌐 **Portfolio:** [https://veerakarthick.dev](https://veerakarthick.dev)  

---

## 📜 License  

This project is licensed under the **MIT License** — feel free to use and modify.
