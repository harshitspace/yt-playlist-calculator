# 📺 YouTube Playlist Study Planner

> Paste a YouTube playlist. Tell me your schedule. Get an AI-generated day-by-day study plan.

**Live App →** [ytstudyplanner.streamlit.app](https://ytstudyplanner.streamlit.app)

---

## ✨ What It Does

This app goes beyond a simple duration calculator. It analyzes your YouTube playlist and uses **Gemini AI** to generate a personalized study schedule based on your real availability and deadline.

| Feature | Description |
|---|---|
| ⏱ Duration Calculator | See total playlist length at 1x, 1.25x, 1.5x, and 2x speed |
| 📋 Video Table | Browse all video titles and individual durations |
| 🤖 AI Study Planner | Generate a day-by-day schedule tailored to your availability |
| ⚠️ Deadline Analysis | Know instantly if you can finish on time — and what to adjust |
| 📄 Download Plan | Export your schedule as Markdown or PDF |

---

## 🖼 Preview

![App Screenshot](https://via.placeholder.com/900x500?text=Add+a+screenshot+here)

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/harshitspace/yt-playlist-calculator.git
cd yt-playlist-calculator
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get your API Keys

**YouTube Data API Key**
- Go to [Google Cloud Console](https://console.cloud.google.com)
- Create a new project
- Enable **YouTube Data API v3**
- Go to Credentials → Create API Key

**Gemini API Key**
- Go to [Google AI Studio](https://aistudio.google.com)
- Click **Get API Key** → Create API key in a **new project**
- Free tier gives ~1,000 requests/day — no credit card needed

### 5. Run the app
```bash
streamlit run app.py
```

---

## 💡 How to Use

1. Paste your **YouTube playlist URL** into the input box
2. Select your preferred **playback speed**
3. Click **Analyze Playlist** — video titles and durations will load
4. Set your **weekday/weekend availability** and **deadline**
5. Add an optional note (e.g. *"I take notes while watching"*)
6. Click **Generate My Study Plan**
7. Download your plan as **PDF** or **Markdown**

---

## 🗂 Project Structure

```
yt-playlist-calculator/
│
├── app.py              # Streamlit UI — main application
├── utils.py            # YouTube Data API helpers (fetch videos + durations)
├── planner.py          # Gemini AI integration — study plan generation
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🛠 Tech Stack

- **Frontend/UI** — [Streamlit](https://streamlit.io)
- **Playlist Data** — YouTube Data API v3
- **AI Scheduling** — Google Gemini API (`gemini-2.5-flash`)
- **PDF Export** — ReportLab
- **Deployment** — Streamlit Community Cloud

---

## 🔮 Roadmap

- [x] Playlist duration calculator (1x, 1.25x, 1.5x, 2x)
- [x] Per-video title and duration table
- [x] AI-generated day-by-day study schedule
- [x] Deadline feasibility analysis
- [x] PDF + Markdown export
- [ ] "I missed today" — AI reschedules the remaining plan
- [ ] Google Calendar export (one-click add study blocks)
- [ ] Progress tracker — mark videos as watched, see updated ETA
- [ ] Support for "Watch Later" playlists (requires OAuth)

---

## 🤝 Contributing

Contributions are welcome! If you have a feature idea or bug fix, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

Made with ❤️ by [Harshit Raj](https://harshitspace.in)