import logging
import os
import shutil
from pathlib import Path

from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent
INPUT_FOLDER = BASE_DIR / "Input"
ORGANIZED_FOLDER = BASE_DIR / "Organized"
LOG_FILE = BASE_DIR / "document_organizer.log"
ENV_FILE = BASE_DIR.parent / "chat_with_docs" / ".env"

ALLOWED_CATEGORIES = {"invoice", "job", "meeting"}
ALLOWED_EXTENSIONS = {".txt"}
MODEL_NAME = "gemini-2.5-flash"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_client():
    """Load the Gemini API key and create an AI client."""
    load_dotenv(ENV_FILE)
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY was not found in the environment.")

    return genai.Client(api_key=api_key)


def classify_document(client, content: str) -> str:
    """Classify document content into one supported category."""
    prompt = f"""Classify this document into exactly one category:
invoice, job, or meeting.

Document:
{content}

Return only the category name.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    return response.text.strip().lower()


def process_file(client, file: Path) -> None:
    """Read, classify, and move one supported document."""
    if not file.is_file():
        logging.warning("Skipped non-file item: %s", file)
        return

    if file.suffix.lower() not in ALLOWED_EXTENSIONS:
        print("SKIPPED UNSUPPORTED FILE:", file.name)
        logging.warning("Skipped unsupported file: %s", file.name)
        return

    print("\nPROCESSING:", file.name)
    logging.info("Processing file: %s", file.name)

    try:
        content = file.read_text(encoding="utf-8")
    except OSError as error:
        print("READ ERROR:", error)
        logging.error("Read error for %s: %s", file.name, error)
        return

    try:
        category = classify_document(client, content)
    except Exception as error:
        print("AI ERROR:", error)
        logging.error("AI error while processing %s: %s", file.name, error)
        return

    if category not in ALLOWED_CATEGORIES:
        print("INVALID CATEGORY:", category)
        logging.error("Invalid category for %s: %s", file.name, category)
        return

    destination_folder = ORGANIZED_FOLDER / category
    destination_folder.mkdir(parents=True, exist_ok=True)
    destination = destination_folder / file.name

    if destination.exists():
        print("DUPLICATE FILE:", file.name)
        logging.warning("Duplicate file skipped: %s", file.name)
        return

    try:
        shutil.move(str(file), str(destination))
        print("MOVED:", file.name)
        logging.info("Moved %s to %s", file.name, destination)
    except OSError as error:
        print("MOVE ERROR:", error)
        logging.error("Move error for %s: %s", file.name, error)


def main() -> None:
    """Process all supported documents in the input directory."""
    INPUT_FOLDER.mkdir(exist_ok=True)
    files = list(INPUT_FOLDER.iterdir())

    if not files:
        print("No files found in Input.")
        logging.info("No files found in Input.")
        return

    try:
        client = get_client()
    except RuntimeError as error:
        print("CONFIGURATION ERROR:", error)
        logging.error("Configuration error: %s", error)
        return

    for file in files:
        process_file(client, file)


if __name__ == "__main__":
    main()
