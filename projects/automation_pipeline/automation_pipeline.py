import requests
from dotenv import load_dotenv
import os
from google import genai

# Load Gemini API key from this project's .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print(api_key is not None)

# Get data from GitHub API
response = requests.get("https://api.github.com")

data = response.json()

# Extract useful information
print(data["current_user_url"])
print(data["repository_search_url"])

info = {
    "user_url": data["current_user_url"],
    "repository_search": data["repository_search_url"]
}

print(info)

# Send data to Gemini
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Briefly summarize this data: {info}"
)

print(response.text)
with open("ai_result.txt", "w", encoding="utf-8") as file:
    file.write(response.text)
