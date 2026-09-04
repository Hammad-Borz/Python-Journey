import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"
DOCUMENT_PATH = BASE_DIR / "documents" / "company_policy.txt"
MODEL_NAME = "gemini-2.5-flash"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "company_policy"
CHUNK_SIZE = 100
QUESTION = "How many vacation days do employees receive?"


def get_ai_client():
    """Load the Gemini API key and create an AI client."""
    load_dotenv(ENV_FILE)
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY was not found in the environment.")

    return genai.Client(api_key=api_key)


def read_document(path: Path) -> str:
    """Read a UTF-8 text document."""
    if not path.is_file():
        raise FileNotFoundError(f"Document not found: {path}")

    return path.read_text(encoding="utf-8")


def create_chunks(text: str, chunk_size: int) -> list[str]:
    """Split text into fixed-size chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def build_collection(chunks: list[str], embedding_model):
    """Create an in-memory vector collection for the document chunks."""
    embeddings = embedding_model.encode(chunks)
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name=COLLECTION_NAME)

    collection.add(
        ids=[str(index) for index in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings.tolist(),
    )

    return collection


def retrieve_context(collection, embedding_model, question: str) -> str:
    """Retrieve the most relevant document chunk for a question."""
    question_embedding = embedding_model.encode([question])
    results = collection.query(
        query_embeddings=question_embedding.tolist(),
        n_results=1,
    )

    documents = results.get("documents", [[]])
    if not documents or not documents[0]:
        raise RuntimeError("No relevant context was retrieved.")

    return documents[0][0]


def generate_answer(ai_client, context: str, question: str) -> str:
    """Generate an answer using only the retrieved context."""
    response = ai_client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""Answer the question using only the context below.

Context:
{context}

Question:
{question}
""",
    )
    return response.text


def main() -> None:
    """Run the complete document retrieval and question-answering workflow."""
    try:
        ai_client = get_ai_client()
        text = read_document(DOCUMENT_PATH)
        chunks = create_chunks(text, CHUNK_SIZE)

        if not chunks:
            print("The document is empty.")
            return

        embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        collection = build_collection(chunks, embedding_model)
        context = retrieve_context(collection, embedding_model, QUESTION)
        answer = generate_answer(ai_client, context, QUESTION)

        print("\n--- Retrieved Context ---")
        print(context)
        print("\n--- AI Answer ---")
        print(answer)

    except (FileNotFoundError, RuntimeError, ValueError, OSError) as error:
        print("ERROR:", error)
    except Exception as error:
        print("UNEXPECTED ERROR:", error)


if __name__ == "__main__":
    main()
