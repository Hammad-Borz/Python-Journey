from pathlib import Path

NOTES_FILE = Path(__file__).parent / "note.txt"


def add_note():
    note = input("Write your note: ").strip()
    if not note:
        print("Note cannot be empty.")
        return

    with NOTES_FILE.open("a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Note saved successfully.")


def view_notes():
    if not NOTES_FILE.exists():
        print("No notes found yet.")
        return

    notes = NOTES_FILE.read_text(encoding="utf-8").strip()
    print(notes or "No notes found yet.")


def search_notes():
    search = input("Enter a word to search: ").strip().lower()
    if not search:
        print("Search term cannot be empty.")
        return

    if not NOTES_FILE.exists():
        print("No notes found yet.")
        return

    matches = [
        line.strip()
        for line in NOTES_FILE.read_text(encoding="utf-8").splitlines()
        if search in line.lower()
    ]

    if matches:
        for note in matches:
            print(f"Found: {note}")
    else:
        print("No matching note found.")


def delete_note():
    if not NOTES_FILE.exists():
        print("No notes found yet.")
        return

    target = input("Enter the exact note to delete: ").strip().lower()
    notes = NOTES_FILE.read_text(encoding="utf-8").splitlines()
    remaining_notes = [note for note in notes if note.lower() != target]

    if len(remaining_notes) == len(notes):
        print("Note not found.")
        return

    content = "\n".join(remaining_notes)
    if content:
        content += "\n"
    NOTES_FILE.write_text(content, encoding="utf-8")
    print("Note deleted successfully.")


def main():
    actions = {
        "1": add_note,
        "2": view_notes,
        "3": search_notes,
        "4": delete_note,
    }

    while True:
        print("\n" + "=" * 40)
        print("Welcome to Smart Note Tool")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")
        print("=" * 40)

        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Thank you for using Smart Note Tool.")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
