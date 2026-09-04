import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from google import genai

GITHUB_API_URL = "https://api.github.com"
MODEL_NAME = "gemini-2.5-flash"
OUTPUT_FILE = Path(__file__).parent / "ai_result.txt"


def get_github_data():
    response = requests.get(GITHUB_API_URL, timeout=15)
    response.raise_for_status()
    data = response.json()

    return {
        "user_url": data["current_user_url"],
        "repository_search": data["repository_search_url"],
    }


def summarize_data(client, data):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"Briefly summarize this data: {data}",
    )
    return response.text


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("GEMINI_API_KEY is not configured.")
        return

    try:
        info = get_github_data()
        print(info)

        client = genai.Client(api_key=api_key)
        summary = summarize_data(client, info)

        print(summary)
        OUTPUT_FILE.write_text(summary, encoding="utf-8")
        print(f"Result saved to: {OUTPUT_FILE.name}")

    except requests.RequestException as error:
        print(f"GitHub API error: {error}")
    except Exception as error:
        print(f"Automation error: {error}")


if __name__ == "__main__":
    main()
