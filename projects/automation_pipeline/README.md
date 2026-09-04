# ⚙️ AI Automation Pipeline

A small Python automation pipeline that retrieves data from the GitHub API, extracts selected information, sends that information to Google Gemini for summarization, and saves the AI-generated result to a text file.

## 🐍 Requirements

- Python 3.10 or newer
- A Google Gemini API key

## 🔄 Workflow

```text
GitHub API
    ↓
HTTP Request
    ↓
JSON Response
    ↓
Extract Useful Data
    ↓
Gemini AI
    ↓
Generate Summary
    ↓
Save Result
```

## ✨ Features

- Retrieves live data from the GitHub API
- Parses JSON API responses
- Extracts selected fields
- Sends structured information to Gemini
- Generates an AI summary
- Saves the generated result to `ai_result.txt`

## 🛠️ Technologies

- Python
- `requests`
- Google Gemini API
- `google-genai`
- `python-dotenv`
- Environment variables

## 📁 Project Structure

```text
automation_pipeline/
├── .env.example
├── automation_pipeline.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
python -m venv .venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Configuration

Copy `.env.example` to `.env` and add your Gemini API key:

```text
GEMINI_API_KEY=your_real_api_key
```

Never commit `.env` or real API keys to GitHub.

## 🚀 How to Run

```bash
python automation_pipeline.py
```

The script requests data, processes it with Gemini, prints the generated summary, and writes the result to `ai_result.txt`.

## 🎯 Learning Focus

This project demonstrates an end-to-end automation flow connecting an external API, Python data processing, an AI model, and file output.

## 👤 Author

**Hammad Borz** — Python & AI Automation
