from ai_assistant_tools import AIAssistant


def test_read_file_prints_content(tmp_path, capsys):
    document = tmp_path / "note.txt"
    document.write_text("Hello world", encoding="utf-8")
    assistant = AIAssistant(str(document))
    assistant.file_path = document

    assistant.read_file()

    output = capsys.readouterr().out
    assert "Hello world" in output


def test_read_file_handles_missing_file(tmp_path, capsys):
    assistant = AIAssistant("missing.txt")
    assistant.file_path = tmp_path / "missing.txt"

    assistant.read_file()

    assert "File not found." in capsys.readouterr().out


def test_count_words_counts_words(tmp_path, capsys):
    document = tmp_path / "note.txt"
    document.write_text("one two three", encoding="utf-8")
    assistant = AIAssistant(str(document))
    assistant.file_path = document

    assistant.count_words()

    assert "Total Words: 3" in capsys.readouterr().out
