import smart_note_tool as app


def test_add_note_saves_note(tmp_path, monkeypatch, capsys):
    app.NOTES_FILE = tmp_path / "notes.txt"
    monkeypatch.setattr("builtins.input", lambda _: "Learn pytest")

    app.add_note()

    assert app.NOTES_FILE.read_text(encoding="utf-8") == "Learn pytest\n"
    assert "Note saved successfully." in capsys.readouterr().out


def test_add_note_rejects_empty_note(tmp_path, monkeypatch, capsys):
    app.NOTES_FILE = tmp_path / "notes.txt"
    monkeypatch.setattr("builtins.input", lambda _: "   ")

    app.add_note()

    assert not app.NOTES_FILE.exists()
    assert "Note cannot be empty." in capsys.readouterr().out


def test_view_notes_handles_missing_file(tmp_path, capsys):
    app.NOTES_FILE = tmp_path / "missing.txt"

    app.view_notes()

    assert "No notes found yet." in capsys.readouterr().out


def test_search_notes_finds_case_insensitive_match(tmp_path, monkeypatch, capsys):
    app.NOTES_FILE = tmp_path / "notes.txt"
    app.NOTES_FILE.write_text("Python Testing\nLearn APIs\n", encoding="utf-8")
    monkeypatch.setattr("builtins.input", lambda _: "python")

    app.search_notes()

    assert "Found: Python Testing" in capsys.readouterr().out


def test_delete_note_removes_matching_note(tmp_path, monkeypatch, capsys):
    app.NOTES_FILE = tmp_path / "notes.txt"
    app.NOTES_FILE.write_text("Keep this\nDelete this\n", encoding="utf-8")
    monkeypatch.setattr("builtins.input", lambda _: "delete this")

    app.delete_note()

    assert app.NOTES_FILE.read_text(encoding="utf-8") == "Keep this\n"
    assert "Note deleted successfully." in capsys.readouterr().out
