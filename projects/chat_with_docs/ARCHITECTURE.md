# 🏗️ Architecture & Workflow

## System Purpose

This project implements a compact RAG pipeline that answers a question using context retrieved from a local document.

## Components

- **Configuration layer** — Loads the Gemini API key from `.env`.
- **Document layer** — Reads the source text document.
- **Chunking layer** — Splits text into fixed-size chunks.
- **Embedding layer** — `SentenceTransformer` converts chunks and questions into vectors.
- **Vector layer** — ChromaDB stores document chunks and embeddings in memory.
- **Retrieval layer** — The most relevant chunk is selected for the question.
- **Generation layer** — Gemini receives the retrieved context and produces an answer.
- **Output layer** — The retrieved context and final answer are printed.

## Workflow

```text
.env + Document
       ↓
Configuration + Text Loading
       ↓
Chunk Creation
       ↓
Document Embeddings
       ↓
ChromaDB Collection
       ↓
User Question
       ↓
Question Embedding
       ↓
Similarity Retrieval
       ↓
Relevant Context
       ↓
Gemini Answer Generation
       ↓
Console Output
```

## Entry Point and Responsibilities

`main()` orchestrates the pipeline. Individual functions separate document reading, chunking, collection creation, retrieval, and answer generation.

## Failure Handling

The workflow explicitly handles missing documents, missing API configuration, invalid chunk sizes, empty documents, and retrieval failures. Unexpected failures are also reported at the application boundary.
