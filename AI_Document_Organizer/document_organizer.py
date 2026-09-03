from pathlib import Path
from dotenv import load_dotenv
import os
from google import genai
import shutil
import logging


logging.basicConfig(
    filename="document_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


Input_folder = Path("Input")
Organized_folder = Path("Organized")

allowed_categories = {"invoice", "job", "meeting"}
allowed_extensions = {".txt"}


files = list(Input_folder.iterdir())


if not files:
    print("No files found in Input.")
    logging.info("No files found in Input.")


load_dotenv("../chat_with_docs/.env")

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


for file in files:

    if not file.is_file():
        print("SKIPPED NON-FILE:", file.name)

        logging.warning(
            f"Skipped non-file item: {file}"
        )

        continue


    if file.suffix.lower() not in allowed_extensions:
        print("SKIPPED UNSUPPORTED FILE:", file.name)

        logging.warning(
            f"Skipped unsupported file: {file.name}"
        )

        continue


    print("\nPROCESSING:", file.name)

    logging.info(
        f"Processing file: {file.name}"
    )


    try:
        content = file.read_text(
            encoding="utf-8"
        )

    except Exception as error:

        print(
            "READ ERROR:",
            error
        )

        logging.error(
            f"Read error for {file.name}: {error}"
        )

        continue


    prompt = f"""
Classify this document into exactly one category:
invoice, job, or meeting.

Document:
{content}

Return only the category name.
"""


    try:

        ai_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        category = (
            ai_response.text
            .strip()
            .lower()
        )


    except Exception as error:

        print(
            "AI ERROR:",
            error
        )

        logging.error(
            f"AI error while processing {file.name}: {error}"
        )

        continue


    if category not in allowed_categories:

        print(
            "INVALID CATEGORY:",
            category
        )

        logging.error(
            f"Invalid category for {file.name}: {category}"
        )

        continue


    logging.info(
        f"AI category for {file.name}: {category}"
    )


    print(
        "CATEGORY:",
        category
    )


    category_folder = (
        Organized_folder / category
    )


    category_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    destination = (
        category_folder / file.name
    )


    if destination.exists():

        print(
            "DUPLICATE FILE:",
            file.name
        )

        logging.warning(
            f"Duplicate file skipped: {file.name}"
        )

    else:

        try:

            shutil.move(
                str(file),
                str(destination)
            )

            logging.info(
                f"Moved {file.name} to {destination}"
            )

            print(
                "MOVED:",
                file.name
            )

        except Exception as error:

            print(
                "MOVE ERROR:",
                error
            )

            logging.error(
                f"Move error for {file.name}: {error}"
            )