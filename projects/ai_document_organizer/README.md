# 🏆 AI Document Organizer

An AI-powered Python automation project that reads text documents, uses Google Gemini to classify them, and automatically moves them into category-based folders.

## 🎯 What It Does

The project processes supported files from the `Input/` directory and classifies each document into one of these categories:

- `invoice`
- `job`
- `meeting`

After classification, the file is moved into the matching directory inside `Organized/`.

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
├── document_organizer.py
├── document_organizer.log
└── README.md
```

## ⚙️ Configuration

The project requires a Gemini API key through the `GEMINI_API_KEY` environment variable.

Never commit API keys or other secrets to GitHub.

## 🚀 How to Run

Install the required dependencies in your environment, configure `GEMINI_API_KEY`, and run:

```bash
python document_organizer.py
```

Place supported input files in the `Input/` directory before running the script.

## 📌 Current Scope

The current implementation is a learning-stage AI automation capstone focused on `.txt` files and three document categories. Future improvements could add more file formats, configurable categories, improved path configuration, tests, and a more modular architecture.

## 👤 Author

**Hammad Borz** — Python & AI Automation
