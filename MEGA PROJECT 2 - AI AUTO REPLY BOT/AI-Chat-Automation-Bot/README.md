# 🤖 AI-Chat-Automation-Bot

**An experimental AI-powered WhatsApp chat automation project — Version 1**

Built with Python, the OpenAI SDK (routed through OpenRouter), and PyAutoGUI-based screen automation.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Experimental%20%7C%20v1-orange)

This is a personal learning project that automates reading the latest WhatsApp Web conversation, generating a contextual AI reply in the sender's voice, and sending it back — all through clipboard and screen-coordinate automation. It is **not** a polished product; it's a working first version built to understand how LLM APIs, clipboard automation, and GUI automation can be wired together.

---

## 📚 Table of Contents

- [⚠️ Important: Customize Before Running](#️-important-customize-before-running)
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How the Three Python Files Work](#how-the-three-python-files-work)
- [Installation](#installation)
- [OpenRouter API Setup](#-openrouter-api-setup)
- [Personalize the Bot](#personalize-the-bot)
- [Coordinate Setup](#-coordinate-setup)
- [Running the Project](#-running-the-project)
- [Safety & Security Notes](#️-important-safety--security-notes)
- [Limitations of Version 1](#limitations-of-version-1)
- [Troubleshooting](#️-troubleshooting)
- [Future Improvements](#-future-improvements)
- [Inspiration](#inspiration--learning)
- [License](#license)
- [Disclaimer](#disclaimer)

---

## ⚠️ Important: Customize Before Running

This repository will **not work out of the box** on your machine. Before running anything, you must personalize **four things**:

| # | What to change | Where |
|---|---|---|
| 1 | 🔑 Your own OpenRouter API key | `02_openai.py`, `03_bot.py` |
| 2 | 🧑 Your personal identity/persona | `02_openai.py`, `03_bot.py` (system prompts) |
| 3 | 💬 The system prompt / conversational style | `02_openai.py`, `03_bot.py` |
| 4 | 📍 Your own screen coordinates | `03_bot.py` |

Each is explained in detail below — please read all four sections before running the bot.

### 1. Add Your Own OpenRouter API Key

The code currently contains a **placeholder** value:

```python
api_key="<Your API Key Here>",
```

You must replace this with your own key from [OpenRouter](https://openrouter.ai/).

> 🔒 **Security reminder**
> - Never commit a real API key to GitHub.
> - Never publish your key publicly in any file, issue, or screenshot.
> - In this Version 1, the key is hardcoded as a placeholder — this is fine for local, personal experimentation, but it is **not** a secure pattern.
> - A recommended future improvement is to load the key from an environment variable (e.g. via `python-dotenv`) instead of hardcoding it. This is **not yet implemented** in Version 1.

### 2. Replace Daksh's Personal Information

The system prompts in `02_openai.py` and `03_bot.py` currently describe a specific persona — *Daksh, a B.S. student in Applied AI and Data Science at IIT Jodhpur, who replies in Hindi/English/Hinglish*.

This persona is **specific to my own use case**. If you clone this repo, you should **not** copy my personal details — instead, replace them with your own:

- Your name
- Your background / education
- Your personality and conversational style
- Your preferred reply language
- Any other identity details relevant to how *you* text

The system prompt is what makes the AI sound like "you" instead of a generic assistant, so this step matters more than it might seem.

### 3. Customize the System Prompt / Conversational Instructions

The AI's tone, personality, and reply style are entirely controlled by the system prompt text in `02_openai.py` and `03_bot.py`. You can adjust things like:

- Tone (formal / casual / witty)
- Language mix (Hindi / English / Hinglish / other)
- Reply length
- Use of emojis
- How context-aware or terse the replies should be

A generic example of what a customized instruction block might look like:

```python
"content": "You are [Your Name], a [your background]. Reply in [preferred language/style], keep responses short, and match the tone of the conversation."
```

This is illustrative only — it does not replace or represent the actual prompt already in the code.

### 4. Use YOUR OWN Screen Coordinates

This is the most critical step. The coordinates hardcoded in `03_bot.py` (e.g. `pyautogui.click(1023, 1054)`) were recorded **on my computer, at my screen resolution, browser window size, zoom level, and WhatsApp Web layout.**

They will almost certainly **not** work on your machine. Screen coordinates change based on:

- Screen resolution
- Display/DPI scaling
- Browser window size and position
- Browser zoom level
- WhatsApp Web's current layout

Run the coordinate helper first:

```bash
python 01_get_cursor.py
```

Move your mouse to each relevant UI element (Chrome icon, chat selection area, message input box, etc.), note the printed coordinates, and manually update the corresponding values in `03_bot.py`.

> **Do not copy my coordinates and expect them to work on your computer.**

---

## Overview

`AI-Chat-Automation-Bot` is a **Version 1, experimental** project that automates a simple loop:

1. Read the latest WhatsApp Web conversation from the screen.
2. Check whether the last message needs a reply.
3. Ask an LLM (via OpenRouter) to generate a short, in-character response.
4. Paste and send that response back into WhatsApp Web.

It exists as a hands-on way to learn how LLM APIs, clipboard-based text extraction, and GUI automation (PyAutoGUI) can be combined into an end-to-end workflow. It is **not production-ready**, and it is designed to be improved in future versions.

---

## How It Works

```text
 WhatsApp Web
      │
      ▼
  PyAutoGUI (drag-select chat)
      │
      ▼
  Ctrl+C  →  Pyperclip (read clipboard)
      │
      ▼
  Chat History (plain text)
      │
      ▼
  Sender Check (is the last message not already from "me"?)
      │
      ▼
  OpenRouter (openrouter/free model via OpenAI SDK)
      │
      ▼
  AI-Generated Reply
      │
      ▼
  Pyperclip (copy reply) → PyAutoGUI (click message box, paste, press Enter)
      │
      ▼
  Message Sent on WhatsApp Web
```

---

## Features

Only functionality that currently exists in the code is listed here:

- 🖱️ **Coordinate helper** (`01_get_cursor.py`) for finding screen positions
- 💬 **WhatsApp Web automation** via PyAutoGUI (click, drag-select, paste, send)
- 📋 **Clipboard-based chat extraction** using Pyperclip
- 🤖 **AI-generated contextual replies** based on the copied chat history
- 🔌 **OpenRouter integration** through the OpenAI Python SDK
- 🌐 **Hindi / English / Hinglish-oriented** reply behavior (configurable via system prompt)
- 🔁 **Continuous polling loop** that checks the chat every few seconds
- ↩️ **Automated message insertion and sending**

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core language for all scripts |
| **OpenAI Python SDK** | Client library used to call the chat completion API |
| **OpenRouter** | LLM API provider (accessed via the OpenAI SDK's custom `base_url`) |
| **PyAutoGUI** | Screen automation — mouse clicks, drags, keyboard shortcuts |
| **Pyperclip** | Reading from and writing to the system clipboard |
| **WhatsApp Web** | The messaging platform being automated |
| **Google Chrome** (or a Chromium-based browser) | Browser used to host WhatsApp Web |

---

## Project Structure

```text
AI-Chat-Automation-Bot/
│
├── 01_get_cursor.py    # Coordinate helper — prints live mouse position
├── 02_openai.py         # OpenRouter connection test / persona system prompt
├── 03_bot.py             # Main automation script (the actual bot)
├── .gitignore            # Standard Python .gitignore
├── LICENSE                # MIT License
└── README.md              # This file
```

---

## How the Three Python Files Work

### `01_get_cursor.py`

A tiny utility that continuously prints the current mouse cursor position:

```python
import pyautogui

while True:
    a = pyautogui.position()
    print(a)
```

**Purpose:** Since `03_bot.py` relies entirely on hardcoded screen coordinates, this script lets you discover the correct coordinates for *your* screen by moving the mouse over the relevant UI elements and reading the printed `(x, y)` values. Run it with:

```bash
python 01_get_cursor.py
```
Press `Ctrl+C` in the terminal to stop it once you've recorded the coordinates you need.

### `02_openai.py`

A minimal connection test that verifies the OpenRouter setup works before running the full bot. It:

- Configures the OpenAI SDK to point at `https://openrouter.ai/api/v1`
- Sends a single test message using the `openrouter/free` model
- Uses a system prompt that defines a specific persona (Daksh — customize this for yourself)
- Prints the model's reply

Run it standalone with `python 02_openai.py` to confirm your API key and persona prompt are working before moving on to the full bot.

### `03_bot.py`

The main automation script. It runs in a loop and, roughly every 5 seconds:

1. Drags to select the visible WhatsApp Web chat text on screen.
2. Copies the selection (`Ctrl+C`).
3. Reads the copied text via Pyperclip.
4. Checks (via `is_last_message_from_sender`) whether the last message in the copied text is **not** already from the configured sender name — i.e., whether a reply is needed.
5. If a reply is needed, sends the chat history to OpenRouter with a persona-driven system prompt.
6. Copies the AI's reply to the clipboard.
7. Clicks the WhatsApp message input box, pastes the reply, and presses Enter to send it.

This script depends entirely on the screen coordinates and window layout being correct for your machine (see [Coordinate Setup](#-coordinate-setup)).

---

## Installation

### Prerequisites

- Python 3.x installed
- Google Chrome (or another Chromium-based browser)
- A WhatsApp account with WhatsApp Web access
- An OpenRouter account and API key

### Install Dependencies

Based on the imports used in the source files, install the following packages:

```bash
pip install openai pyautogui pyperclip
```

### Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Chat-Automation-Bot.git
cd AI-Chat-Automation-Bot
```

---

## 🔑 OpenRouter API Setup

1. Create a free account at [openrouter.ai](https://openrouter.ai/).
2. Generate a new API key from your OpenRouter dashboard.
3. Copy the key.
4. Paste it into the `api_key` field in **both** `02_openai.py` and `03_bot.py`, replacing `<Your API Key Here>`.
5. **Never publish this key** — keep it local and out of version control.

The current implementation uses:

```python
base_url="https://openrouter.ai/api/v1"
```

```python
model="openrouter/free"
```

`openrouter/free` refers to OpenRouter's free-tier model routing. Availability and behavior of free models can change over time — this is not guaranteed to remain free or available indefinitely.

---

## Personalize the Bot

Before running the bot for real, walk through this checklist:

- [ ] Replace the placeholder API key in `02_openai.py` and `03_bot.py`
- [ ] Replace the persona name (currently "Daksh") with your own
- [ ] Replace the educational/background details in the system prompt
- [ ] Customize the system prompt's tone and personality
- [ ] Set your preferred reply language (Hindi / English / Hinglish / other)
- [ ] Set your preferred reply length/style
- [ ] Record and set your own screen coordinates in `03_bot.py`

---

## 📍 Coordinate Setup

PyAutoGUI automation is driven entirely by **absolute screen coordinates**, which are unique to your machine's display setup. The coordinates currently in `03_bot.py` were recorded on my computer and **will not be accurate on yours**.

To set your own:

1. Open WhatsApp Web in Chrome and arrange the window as you intend to use it during automation.
2. Run the coordinate helper:
   ```bash
   python 01_get_cursor.py
   ```
3. Hover your mouse over each relevant UI element one at a time (the Chrome taskbar icon, the top and bottom corners of the chat area you want to select, the message input box) and note the `(x, y)` values printed in the terminal.
4. Stop the script (`Ctrl+C`) and update the corresponding coordinates in `03_bot.py` (`pyautogui.click(...)`, `pyautogui.moveTo(...)`, `pyautogui.dragTo(...)` calls).

Coordinates can be affected by:

- Screen resolution
- Windows/macOS display scaling
- Browser window size and position
- Browser zoom level
- Changes to WhatsApp Web's layout

> **Do not copy my coordinates and expect them to work on your computer.**

---

## 🚀 Running the Project

1. Clone the repository.
2. Open the project folder in a terminal.
3. Install dependencies (`pip install openai pyautogui pyperclip`).
4. Add your OpenRouter API key to `02_openai.py` and `03_bot.py`.
5. Replace the persona/system prompt details with your own.
6. Customize the system prompt's tone, language, and style.
7. Run `python 01_get_cursor.py` and record your coordinates.
8. Update the coordinates in `03_bot.py`.
9. Open Chrome, log in to WhatsApp Web, and open the chat you want to test with.
10. Make sure the chat you want automated is visible on screen.
11. Run the bot:
    ```bash
    python 03_bot.py
    ```
12. Watch the terminal output (copied chat text, AI response) and observe WhatsApp Web to confirm it behaves as expected.

---

## ⚠️ Important Safety / Security Notes

- The bot sends **copied chat text** to a third-party API (OpenRouter) for processing — be mindful of what conversations you run this on.
- Never commit real API keys or personal chat data to a public repository.
- This automation **clicks and sends messages automatically** — a coordinate or timing error could send an unintended message to a real contact.
- **Test with a safe/private chat first** (e.g., a chat with yourself or a test contact) before pointing it at any real conversation.
- Automating your personal WhatsApp account carries inherent risk — proceed carefully and understand what the script is doing before running it unattended.

---

## Limitations of Version 1

This is an early, experimental implementation with real constraints:

- Fully dependent on hardcoded screen coordinates (no dynamic UI element detection)
- Sensitive to screen resolution, display scaling, browser size/zoom, and window position
- Relies on drag-selecting and copying visible text rather than reading WhatsApp Web's underlying DOM/data
- Requires manual personalization before it will work correctly
- No duplicate-message or race-condition protection
- No structured error handling for failed API calls or failed clipboard reads
- Only tested against a single browser/WhatsApp Web layout at a time

---

## 🛠️ Troubleshooting

| Issue | Likely Cause | Solution |
|---|---|---|
| Bot clicks the wrong location | Coordinates don't match your screen | Recalibrate using `python 01_get_cursor.py` |
| Text is not copied (empty clipboard) | WhatsApp Web not visible, or selection coordinates/timing are off | Ensure WhatsApp Web is on screen and adjust the drag-select coordinates/delays |
| Message is pasted in the wrong place | Message box coordinate is incorrect | Re-check the message input box coordinate with `01_get_cursor.py` |
| API request fails | Invalid API key, no internet, or model unavailable | Verify your OpenRouter API key, internet connection, and that `openrouter/free` is still available |
| AI response doesn't sound like you | System prompt still uses default/placeholder persona | Update the system prompt with your own name, background, tone, and language preferences |

---

## 🚀 Future Improvements

These are **ideas for future versions** — none of the following are currently implemented:

- Environment-variable-based API key management (e.g. `.env` + `python-dotenv`)
- Dynamic UI element detection instead of fixed coordinates
- More reliable message/sender detection logic
- Duplicate-message prevention
- Proper error handling and retries for API and clipboard failures
- A configuration file for personas, coordinates, and prompt settings
- Support for multiple AI models/providers
- Logging of sent/received messages
- A simple GUI or settings interface for configuration

---

## Inspiration / Learning

This project was built as a personal learning and experimentation exercise, inspired by the general idea of AI-powered WhatsApp automation tutorials/workflows found in the developer community. It is **not** an official project of, or affiliated with, any specific tutorial creator — it is my own independent implementation, built to understand how the underlying pieces (LLM APIs, clipboard automation, GUI scripting) fit together.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details. In short, you're free to use, copy, modify, and distribute this code, provided the original copyright notice is included.

---

## Disclaimer

This is an experimental automation project built for learning purposes. It interacts directly with your WhatsApp Web session and can send messages automatically. Users are solely responsible for configuring, testing, and using this project appropriately. Automated messaging can have unintended consequences (e.g., sending an incorrect or poorly timed message) — please test thoroughly with a safe chat before using it on real conversations.
