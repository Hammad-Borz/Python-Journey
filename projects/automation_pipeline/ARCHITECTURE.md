# 🏗️ Architecture & Workflow

## System Purpose

The pipeline retrieves selected data from the GitHub API, summarizes it with Gemini, and writes the generated result to a local text file.

## Components

- **Configuration layer** — Loads `GEMINI_API_KEY` from the environment.
- **API layer** — `requests` retrieves data from the GitHub API.
- **Transformation layer** — `get_github_data()` extracts the selected response fields.
- **AI layer** — Gemini summarizes the structured data.
- **Output layer** — The summary is printed and saved to `ai_result.txt`.
- **Error boundary** — Request and general runtime failures are reported to the user.

## Workflow

```text
Environment Variables
       ↓
API Key Validation
       ↓
GitHub API Request
       ↓
HTTP Status Validation
       ↓
JSON Response
       ↓
Extract Required Fields
       ↓
Gemini Summarization
       ↓
Console Output + Text File
```

## Entry Point and Responsibilities

`main()` orchestrates configuration, data retrieval, AI processing, and file output. `get_github_data()` isolates the external API interaction, while `summarize_data()` isolates the AI-generation step.

## Failure Handling

GitHub request failures and other runtime errors are caught at the orchestration layer so the user receives a clear error message instead of an unhandled crash.
