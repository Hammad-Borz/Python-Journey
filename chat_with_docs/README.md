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
├── main.py
└── README.md
```

## ⚙️ Configuration

The script expects a Gemini API key in an environment variable named `GEMINI_API_KEY`.

Never commit API keys or other secrets to the repository.

## 🚀 Current Scope

This is a learning-stage RAG implementation. It is intentionally simple and provides a foundation for later improvements such as better chunking, metadata, persistent vector storage, multiple document formats, retrieval evaluation, and a user-facing interface.

## 👤 Author

**Hammad Borz** — Python & AI Automation
