from pathlib import Path

import document_organizer as organizer


class FakeResponse:
    def __init__(self, text):
        self.text = text


class FakeModels:
    def __init__(self, text):
        self.text = text

    def generate_content(self, **kwargs):
        return FakeResponse(self.text)


class FakeClient:
    def __init__(self, text):
        self.models = FakeModels(text)


def test_classify_document_normalizes_category():
    client = FakeClient("Invoice\n")

    assert organizer.classify_document(client, "Payment details") == "invoice"


def test_process_file_moves_valid_document(tmp_path, monkeypatch, capsys):
    source_folder = tmp_path / "Input"
    source_folder.mkdir()
    source = source_folder / "bill.txt"
    source.write_text("Invoice content", encoding="utf-8")

    monkeypatch.setattr(organizer, "ORGANIZED_FOLDER", tmp_path / "Organized")

    organizer.process_file(FakeClient("invoice"), source)

    destination = tmp_path / "Organized" / "invoice" / "bill.txt"
    assert destination.exists()
    assert not source.exists()
    assert "MOVED: bill.txt" in capsys.readouterr().out


def test_process_file_skips_unsupported_extension(tmp_path, capsys):
    source = tmp_path / "image.pdf"
    source.write_text("Not a supported file", encoding="utf-8")

    organizer.process_file(FakeClient("invoice"), source)

    assert source.exists()
    assert "SKIPPED UNSUPPORTED FILE" in capsys.readouterr().out


def test_process_file_rejects_invalid_ai_category(tmp_path, monkeypatch, capsys):
    source = tmp_path / "document.txt"
    source.write_text("Document content", encoding="utf-8")
    monkeypatch.setattr(organizer, "ORGANIZED_FOLDER", tmp_path / "Organized")

    organizer.process_file(FakeClient("unknown"), source)

    assert source.exists()
    assert not (tmp_path / "Organized").exists()
    assert "INVALID CATEGORY: unknown" in capsys.readouterr().out


def test_process_file_skips_duplicate_destination(tmp_path, monkeypatch, capsys):
    source = tmp_path / "document.txt"
    source.write_text("Document content", encoding="utf-8")
    organized = tmp_path / "Organized" / "meeting"
    organized.mkdir(parents=True)
    (organized / "document.txt").write_text("Existing", encoding="utf-8")
    monkeypatch.setattr(organizer, "ORGANIZED_FOLDER", tmp_path / "Organized")

    organizer.process_file(FakeClient("meeting"), source)

    assert source.exists()
    assert "DUPLICATE FILE: document.txt" in capsys.readouterr().out
