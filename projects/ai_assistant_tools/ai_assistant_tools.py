from pathlib import Path


class AIAssistant:
    """A menu-driven assistant with calculator and text-file utilities."""

    def __init__(self, filename="note1.txt"):
        self.file_path = Path(__file__).parent / filename
        print("🤖 AI Assistant is Ready!")

    def calculator(self):
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
        }

        if operator == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        elif operator in operations:
            result = operations[operator](num1, num2)
        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    def read_file(self):
        if not self.file_path.exists():
            print("File not found.")
            return

        try:
            text = self.file_path.read_text(encoding="utf-8")
            print("\n📄 File Content:\n")
            print(text)
        except OSError as error:
            print(f"File error: {error}")

    def count_words(self):
        if not self.file_path.exists():
            print("File not found.")
            return

        try:
            word_count = len(self.file_path.read_text(encoding="utf-8").split())
            print(f"\n📊 Total Words: {word_count}")
        except OSError as error:
            print(f"File error: {error}")

    def start(self):
        actions = {
            "1": self.calculator,
            "2": self.read_file,
            "3": self.count_words,
        }

        while True:
            print("\n========== AI Assistant ==========")
            print("1. Calculator")
            print("2. Read File")
            print("3. Count Words")
            print("4. Exit")

            choice = input("Choose an option (1-4): ").strip()

            if choice == "4":
                print("👋 Goodbye!")
                break

            action = actions.get(choice)
            if action:
                action()
            else:
                print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    AIAssistant().start()
