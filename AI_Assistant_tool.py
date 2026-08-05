import os


class AIAssistant:
    def __init__(self):
        print("🤖 AI Assistant is Ready!")

    def calculator(self):
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")

    def read_file(self):
        filename = "note1.txt"

        if os.path.exists(filename):
            with open(filename, "r") as file:
                text = file.read()

            print("\n📄 File Content:\n")
            print(text)

        else:
            print("File not found.")

    def count_words(self):
        filename = "note1.txt"

        if os.path.exists(filename):
            with open(filename, "r") as file:
                text = file.read()

            words = text.split()

            print(f"\n📊 Total Words: {len(words)}")

        else:
            print("File not found.")

    def start(self):
        while True:
            print("\n========== AI Assistant ==========")
            print("1. Calculator")
            print("2. Read File")
            print("3. Count Words")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                self.calculator()

            elif choice == "2":
                self.read_file()

            elif choice == "3":
                self.count_words()

            elif choice == "4":
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid choice. Try again.")


assistant = AIAssistant()
assistant.start()