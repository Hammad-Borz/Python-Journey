# 🏆 AI Document Organizer

An AI-powered Python automation project that reads text documents, uses Google Gemini to classify them, and automatically moves them into category-based folders.

## 🎯 What It Does

The project processes supported files from the `Input/` directory and classifies each document into one of these categories:

- `invoice`
- `job`
- `meeting`

After classification, the file is moved into the matching directory inside `Organized/`.

## 🐍 Requirements

- Python 3.10 or newer
- A Google Gemini API key

## 🔄 Workflow

```text
Input Document
      ↓
Read File Content
      ↓
Gemini AI Classification
      ↓
Validate Category
      ↓
Create Category Folder
      ↓
Move Document
      ↓
Log the Result
```

## ✨ Features

- AI-powered document classification
- Automatic file organization
- Supported category validation
- File-extension validation
- Duplicate-file detection
- Error handling for reading, AI, and file-moving operations
- Activity logging

## 🛠️ Technologies

- Python
- Google Gemini API
- `google-genai`
- `python-dotenv`
- `pathlib`
- `shutil`
- `logging`

## 📁 Project Structure

```text
ai_document_organizer/
├── Input/
├── Organized/
├── .env.example
├── document_organizer.py
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

Copy `.env.example` to `.env` and add your real Gemini API key:

```text
GEMINI_API_KEY=your_real_api_key
```

Never commit `.env` or real API keys to GitHub.

## 🚀 How to Run

```bash
python document_organizer.py
```

Place supported input files in the `Input/` directory before running the script.

## 📌 Current Scope

The current implementation is a learning-stage AI automation capstone focused on `.txt` files and three document categories.

## 👤 Author

**Hammad Borz** — Python & AI Automation
