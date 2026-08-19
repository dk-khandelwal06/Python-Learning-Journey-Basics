# 🤖 JARVIS — AI Voice Assistant

> Your Python-powered personal voice assistant.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Speech Recognition](https://img.shields.io/badge/Speech%20Recognition-Google%20API-brightgreen)
![Text to Speech](https://img.shields.io/badge/Text--to--Speech-gTTS-orange)
![OpenAI](https://img.shields.io/badge/AI-OpenAI%20(optional)-412991?logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📖 Introduction

**Jarvis** is a Python-based personal voice assistant, inspired by assistants like **JARVIS (Iron Man)**, **Alexa**, and **Google Assistant**. It listens for a wake word, understands spoken commands, and responds with synthesized speech — automating everyday tasks like opening websites, playing music, reading the news, and (optionally) answering general questions using OpenAI.

This is **Version 1** of the project, built as a hands-on learning exercise to apply core Python concepts — functions, dictionaries, modules, error handling, and third-party API integration — into a single working application. AI tools were used occasionally along the way to help debug issues and understand errors, but the design and implementation are my own.

> Jarvis is inspired by assistants like Alexa and Google Assistant — it is not a replacement for them, and is intended as a personal learning and portfolio project.

---

## ✨ Features

- 🎙️ **Wake-word activation** — starts listening for commands after hearing "Jarvis"
- 🗣️ **Speech recognition** — converts spoken commands into text using Google's speech recognition engine
- 🔊 **Text-to-speech** — speaks responses back using gTTS + pygame (with a legacy `pyttsx3` option)
- 🌐 **Website automation** — opens 19 popular websites on voice command
- 🎵 **Music playback** — plays songs from a customizable local music library via YouTube links
- 📰 **News headlines** — fetches and reads out top headlines in India using NewsAPI
- 🤖 **Optional OpenAI-powered responses** — falls back to an OpenAI model for general queries
- 🧩 **Modular music library** — songs stored separately in `musicLibrary.py` for easy editing
- 🐍 **Pure Python implementation** — no external frameworks required

---

## 🧠 How Jarvis Works

```text
User
  ↓
Microphone
  ↓
Speech Recognition (Google Speech API)
  ↓
"Jarvis" Wake Word Detected
  ↓
Command Recognition
  ↓
Command Processor
  ├── Website keyword   → Opens site in browser
  ├── "play <song>"     → Looks up musicLibrary.py → Opens YouTube link
  ├── "news"            → Calls NewsAPI → Reads headlines
  └── Anything else     → Sent to OpenAI (aiProcess) → Returns response
  ↓
Text-to-Speech (gTTS + pygame)
  ↓
Voice Response
```

---

## 🛠️ Tech Stack

| Technology                 | Purpose                            |
|-----------------------------|-------------------------------------|
| Python                      | Core programming language          |
| SpeechRecognition            | Capturing & recognizing speech     |
| Google Speech Recognition   | Speech-to-text engine              |
| gTTS                        | Text-to-speech generation          |
| pygame                      | Playing generated audio            |
| pyttsx3                     | Legacy offline text-to-speech (`speak_old`) |
| OpenAI API                  | Optional AI-powered responses      |
| NewsAPI                     | Fetching top headlines             |
| Requests                    | Making HTTP requests to NewsAPI    |
| webbrowser                  | Opening websites automatically     |
| PocketSphinx                | Speech recognition dependency      |

---

## 📁 Project Structure

```text
Jarvis-AI-Voice-Assistant/
│
├── main.py                          # Core application: wake word, commands, TTS, STT
├── client.py                        # Standalone OpenAI API demo/test script
├── musicLibrary.py                  # Song name → YouTube link mapping
├── requirements.txt                 # Python dependencies (renamed from requiremnets.txt)
├── README.md                        # Project documentation
├── LICENSE                          # MIT License
├── .gitignore                       # Files/folders excluded from Git
└── assets/
    └── README-assets-placeholder.md # Placeholder for future screenshots/GIFs
```

### File Descriptions

- **`main.py`** — The main Jarvis application. Handles wake-word detection, voice input, command processing, website automation, music playback, news retrieval, and OpenAI processing.
- **`client.py`** — A standalone script demonstrating a basic OpenAI chat completion request, independent of the voice assistant loop.
- **`musicLibrary.py`** — Stores a dictionary of song names mapped to their YouTube links, used by the `play <song>` command.
- **`requirements.txt`** — Lists all Python dependencies needed to run the project. *(Note: the original file in this project was named `requiremnets.txt` — a typo. It's included here under the corrected, standard filename. See the [Notes on File Naming](#-notes-on-file-naming) section below.)*

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Jarvis-AI-Voice-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

> If you're keeping the original filename in your repo, run `pip install -r requiremnets.txt` instead.

---

## 🔑 API Key Configuration

Jarvis uses two external APIs, both of which currently require you to **directly edit placeholder values in the source code**:

| API      | File          | Placeholder Location                                   |
|----------|---------------|----------------------------------------------------------|
| OpenAI   | `main.py`     | `aiProcess()` function → `OpenAI(api_key="<Your Key Here>")` |
| OpenAI   | `client.py`   | `OpenAI(api_key="<Your Key Here>")`                     |
| NewsAPI  | `main.py`     | `newsapi = "<Your Key Here>"`                            |

**Steps:**
1. Get a free/paid OpenAI API key from [platform.openai.com](https://platform.openai.com).
2. Get a free NewsAPI key from [newsapi.org](https://newsapi.org).
3. Replace each `<Your Key Here>` placeholder with your own key **locally**.

> ⚠️ **Never commit real API keys to GitHub.** Keep placeholders in the version of the code you push publicly. A recommended future improvement is to load keys from environment variables (e.g. via a `.env` file) instead of hardcoding them — see the [Future Roadmap](#-future-roadmap).

---

## ▶️ Running Jarvis

```bash
python main.py
```

**What happens:**
1. Jarvis prints `Initializing Jarvis....` and starts listening.
2. Say **"Jarvis"** to activate it.
3. Jarvis responds **"Ya"**.
4. Speak your command.

**Example commands:**

```text
Jarvis → "Ya"

"Open Google"
"Open YouTube"
"Open GitHub"
"Play Blue Eyes"
"Play Workout Songs"
"News"
```

For anything not matched by a specific command, Jarvis sends your query to OpenAI (if configured):

```text
Jarvis → "Ya"
"What is coding?"
```

---

## 🎵 Adding Your Own Music

Open `musicLibrary.py` and add a new entry to the `music` dictionary:

```python
music = {
    # ...existing songs...
    "my song": "https://www.youtube.com/watch?v=your-video-id",
}
```

Then say:

```text
"Play My Song"
```

Commands are lowercased before lookup, so multi-word song names work naturally. Jarvis does **not** search YouTube dynamically — it only opens links you've manually added to the library. Please don't upload copyrighted music files to the repository; only link references are stored.

---

## 🌐 Supported Website Commands

| Voice Command        | Action               |
|------------------------|------------------------|
| Open Google            | Opens google.com       |
| Open Facebook          | Opens facebook.com     |
| Open YouTube           | Opens youtube.com      |
| Open LinkedIn          | Opens linkedin.com     |
| Open Instagram         | Opens instagram.com    |
| Open WhatsApp          | Opens web.whatsapp.com |
| Open Twitter           | Opens twitter.com      |
| Open X                 | Opens x.com             |
| Open GitHub            | Opens github.com       |
| Open ChatGPT           | Opens chatgpt.com      |
| Open Gmail             | Opens gmail.com        |
| Open Amazon            | Opens amazon.in        |
| Open Netflix           | Opens netflix.com      |
| Open Spotify           | Opens open.spotify.com |
| Open Reddit            | Opens reddit.com       |
| Open Wikipedia         | Opens wikipedia.org    |
| Open Stack Overflow    | Opens stackoverflow.com|
| Open Google Drive      | Opens drive.google.com |
| Open Discord           | Opens discord.com      |
| Open Canva             | Opens canva.com        |

---

## 📰 News

Saying **"News"** triggers a call to NewsAPI's top-headlines endpoint (filtered to India), and Jarvis speaks each returned article title aloud. Requires a valid NewsAPI key configured in `main.py`.

---

## 🤖 OpenAI Integration

Any command that doesn't match a website, music, or news trigger is passed to the `aiProcess()` function, which sends it to an OpenAI chat model (`gpt-3.5-turbo`) with a short system prompt describing Jarvis's persona, and speaks back the response.

`client.py` is a separate, standalone script used to test a basic OpenAI chat completion call outside the main assistant loop — useful for verifying your API key works before running the full assistant.

This feature is **optional** — all website, music, and news commands work without an OpenAI key. OpenAI usage is subject to OpenAI's own pricing; it is not free.

---

## 🧪 Example Interaction

```text
Initializing Jarvis....

recognizing...
Listening...

Jarvis
Ya

Jarvis Active...

User: Open YouTube
Jarvis: [opens https://youtube.com in the browser]

User: Play Blue Eyes
Jarvis: [opens the Blue Eyes YouTube link]

User: What is coding?
Jarvis: [speaks an AI-generated explanation of coding]
```

---

## 🔒 Security

- **Never commit real API keys** to a public repository.
- Keep `<Your Key Here>` placeholders in any code you push publicly.
- If environment variables are introduced later, add `.env` to `.gitignore` (already included here).
- If a key is ever accidentally exposed, **rotate/revoke it immediately** from the provider's dashboard.
- Do not upload personal credentials, tokens, or private config files to the repository.

---

## 🚧 Current Limitations

These are honest, expected limitations of a Version 1 project — and good opportunities for future development:

- Requires microphone access to function.
- Requires an internet connection for Google speech recognition.
- News feature requires a valid NewsAPI key.
- AI responses require a valid OpenAI API key.
- Music links are manually maintained rather than dynamically searched.
- Voice recognition may occasionally misinterpret commands.
- Wake-word detection relies on the same speech recognition engine as commands, rather than a dedicated always-on wake-word engine.
- Error handling is currently basic (a generic `try/except` around the listening loop).
- API keys are currently entered directly as placeholders in source files rather than loaded from environment variables.

---

## 🚀 Future Roadmap

### ✅ Version 1.0 (Current)
- [x] Voice activation with wake word
- [x] Website automation
- [x] Music library playback
- [x] News headlines
- [x] Optional OpenAI integration

### 🔜 Version 2.0 (Planned)
- [ ] Environment variable–based API key management (`.env`)
- [ ] Improved command parsing and matching
- [ ] Better error messages and logging
- [ ] More natural multi-turn conversations
- [ ] Additional voice commands
- [ ] Smarter/fuzzy music search
- [ ] Dedicated always-on wake-word detection

### 🌟 Version 3.0 (Ideas)
- [ ] Graphical user interface (GUI)
- [ ] System-level controls (volume, apps, etc.)
- [ ] Weather integration
- [ ] Reminders and to-do management
- [ ] Email integration
- [ ] Calendar integration
- [ ] Expanded automation capabilities

---

## 🎓 What I Learned

Building Jarvis helped me practice and apply:

- Python fundamentals — variables, functions, conditionals, loops
- Working with dictionaries as lightweight data stores (`musicLibrary.py`)
- Structuring a multi-file Python project
- Making and handling HTTP requests (`requests`, NewsAPI)
- Parsing JSON API responses
- Integrating third-party APIs (OpenAI, NewsAPI)
- Speech recognition and text-to-speech pipelines
- Working with external libraries (`SpeechRecognition`, `gTTS`, `pygame`, `pyttsx3`)
- Basic error handling with `try/except`
- Managing dependencies with `requirements.txt` / virtual environments
- Debugging real-world runtime errors

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m "Add: your feature"`)
5. Push to your branch and open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Daksh Khandelwal**

- [GitHub](https://github.com/dk-khandelwal06)
- [LinkedIn](https://www.linkedin.com/in/daksh-khandelwal-b02748391/)

---

## ⭐ Star the Repository

If you found this project interesting or useful, consider giving it a ⭐ — it helps others discover it and motivates further development!
