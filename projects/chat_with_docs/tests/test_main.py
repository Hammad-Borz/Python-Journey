from pathlib import Path

import pytest

import main


def test_read_document_reads_existing_file(tmp_path):
    document = tmp_path / "document.txt"
    document.write_text("Hello RAG", encoding="utf-8")

    assert main.read_document(document) == "Hello RAG"


def test_read_document_raises_for_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        main.read_document(tmp_path / "missing.txt")


def test_create_chunks_splits_text():
    assert main.create_chunks("abcdefghij", 4) == ["abcd", "efgh", "ij"]


@pytest.mark.parametrize("chunk_size", [0, -1, -10])
def test_create_chunks_rejects_invalid_size(chunk_size):
    with pytest.raises(ValueError, match="chunk_size must be greater than zero"):
        main.create_chunks("text", chunk_size)


def test_create_chunks_handles_empty_text():
    assert main.create_chunks("", 10) == []


class FakeEmbeddingModel:
    def encode(self, values):
        assert values == ["question"]
        return FakeEmbeddings([[0.1, 0.2]])


class FakeEmbeddings:
    def __init__(self, values):
        self.values = values

    def tolist(self):
        return self.values


class FakeCollection:
    def __init__(self, documents):
        self.documents = documents

    def query(self, **kwargs):
        return {"documents": self.documents}


def test_retrieve_context_returns_best_document():
    collection = FakeCollection([["Relevant context"]])

    assert main.retrieve_context(collection, FakeEmbeddingModel(), "question") == "Relevant context"


def test_retrieve_context_raises_when_nothing_is_found():
    collection = FakeCollection([[]])

    with pytest.raises(RuntimeError, match="No relevant context was retrieved"):
        main.retrieve_context(collection, FakeEmbeddingModel(), "question")
