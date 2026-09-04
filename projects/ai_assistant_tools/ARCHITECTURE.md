# 🏗️ Architecture & Workflow

## System Purpose

A command-line assistant that routes user choices to calculator, file-reading, and word-counting tools.

## Components

- **User interface** — Interactive terminal menu.
- **Controller** — `start()` manages the application loop and routes actions.
- **Calculator tool** — Performs validated arithmetic operations.
- **File tool** — Reads the configured text file.
- **Word-count tool** — Counts words in the configured text file.
- **Validation layer** — Handles invalid menu choices, invalid numbers, invalid operators, division by zero, missing files, and file errors.

## Workflow

```text
User
  ↓
Command-Line Menu
  ↓
Validate Choice
  ↓
Selected Tool
  ├── Calculator → Validate Input → Calculate → Result
  ├── Read File → Check File → Read → Display
  └── Count Words → Check File → Read → Count → Display
  ↓
Return to Menu or Exit
```

## Entry Point

The application creates an `AIAssistant` instance and starts the menu loop. Individual methods keep each tool responsibility separate.
