# 🏗️ Architecture & Workflow

## System Purpose

The system classifies supported input documents with Gemini and moves each file into an organized category folder.

## Components

- **Input layer** — `Input/` contains incoming files.
- **Processing layer** — `document_organizer.py` validates, reads, and processes each file.
- **AI layer** — Gemini classifies document content.
- **Validation layer** — Categories and file extensions are checked against supported values.
- **Output layer** — Files are moved into `Organized/<category>/`.
- **Observability layer** — `document_organizer.log` records processing activity and errors.

## Workflow

```text
Input Folder
    ↓
File Discovery
    ↓
Extension Validation
    ↓
Read Document
    ↓
Gemini Classification
    ↓
Category Validation
    ↓
Duplicate Check
    ↓
Move File to Organized Folder
    ↓
Console + Log Output
```

## Error Paths

Unsupported files, read failures, AI failures, invalid categories, duplicates, and move failures are handled without stopping the entire batch.

## Entry Point

`main()` coordinates folder preparation, client creation, file discovery, and processing. `process_file()` handles one file, while `classify_document()` isolates the AI classification step.
