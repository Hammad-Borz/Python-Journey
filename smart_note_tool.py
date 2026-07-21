while True:
    greeting = ("Welcome to our project")
    print("\n" + "=" * 40)
    print(greeting)
    print("1. Add Note")
    print("2. View Note")
    print("3. Search Note")
    print("4. Delete Note")
    print("5. Exit")
    print("=" * 40)
    choice = input("Choose an option: ")
    print(f"You Selected: {choice}")
    if choice == "1":
       print("You choose Add Note")
       note  = input("Write your note: ")
       print(note)
       with open("note.txt", "a") as file:
          file.write(note + "\n")
       print("Note saved succcesfully")
       input("\nPress Enter to continue...")
    elif choice == "2":
       print("You choose View Note")
       with open("note.txt", "r") as file:
         notes = file.read()
         print(notes)
         input("\nPress Enter to continue...")
    elif choice == "3":
        print("You choose Search Note")
        search = input("Enter a word to search: ")
        Found = False
        with open("note.txt", "r") as file:
           for line in file:
               if search.lower() in line.lower():
                print(f"Found: {line.strip()}")
                Found = True
        if not Found:
            print("No matching note found.")
        input("\nPress Enter to continue...")
    elif choice == "4":
        print("You choose Delete Note")
        delete_note = input("Enter the exact note to delete: ")
        with open("note.txt", "r") as file:
            notes = file.readlines()
        with open("note.txt", "w") as file:
            found = False 
            for line in notes:
               if line.strip().lower() != delete_note.lower():
                    file.write(line)
               else:
                found = True
        if found:
             print("Note deleted successfully.")
        else:
            print("Note not found.")
        input("\nPress Enter to continue...")
    elif choice == "5":
        print("Thank You For Using Smart Note Tool")
        break
    else:
        print("Please choose 1-5")