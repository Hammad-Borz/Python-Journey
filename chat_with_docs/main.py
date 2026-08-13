from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
import os
from dotenv import load_dotenv
from google import genai
load_dotenv(dotenv_path=".env")

api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))

client_ai = genai.Client(api_key=api_key)
file_path = Path("documents/company_policy.txt")

text = file_path.read_text(encoding="utf-8")

chunk_size = 100

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)


# Display chunks

for number, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {number} ---")
    print(chunk)
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

print(embeddings.shape)
client = chromadb.Client()

collection = client.create_collection(
    name="company_policy"
)

collection.add(
    ids=[str(i) for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings.tolist()
)

print("Documents stored successfully!")
question = "How many vacation days do employees receive?"
question_embedding = model.encode([question])
results = collection.query(
    query_embeddings=question_embedding.tolist(),
    n_results=1
)

print("\n--- Retrieved Chunk ---")

print(results["documents"][0][0])
context = results["documents"][0][0]

response = client_ai.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
"""
)
print("\n--- AI Answer ---")

print(response.text)