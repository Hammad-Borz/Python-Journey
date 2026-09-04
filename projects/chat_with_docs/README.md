# 📚 Chat with Documents — RAG Practice

A practical Retrieval-Augmented Generation (RAG) learning project that demonstrates a basic document-question-answering pipeline.

## 🎯 What It Demonstrates

The current implementation:

1. Reads a text document from the `documents/` directory.
2. Splits the document into chunks.
3. Generates vector embeddings with `SentenceTransformer`.
4. Stores the chunks and embeddings in ChromaDB.
5. Embeds a user question.
6. Retrieves the most relevant document chunk.
7. Sends the retrieved context to Gemini.
8. Generates an answer using the retrieved context.

## 🐍 Requirements

- Python 3.10 or newer
- A Google Gemini API key

## 🏗️ Workflow

```text
Document
   ↓
Text Extraction
   ↓
Chunking
   ↓
SentenceTransformer Embeddings
   ↓
ChromaDB Vector Store
   ↓
Question Embedding
   ↓
Similarity Retrieval
   ↓
Relevant Context
   ↓
Gemini
   ↓
Answer
```

## 🛠️ Technologies

- Python
- Google Gemini API
- Sentence Transformers
- ChromaDB
- python-dotenv
- pathlib

## 📁 Structure

```text
chat_with_docs/
├── documents/
├── .env.example
├── main.py
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
python main.py
```

## 📌 Current Scope

This is a learning-stage RAG implementation with intentionally simple retrieval and document handling.

## 👤 Author

**Hammad Borz** — Python & AI Automation
