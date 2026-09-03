tasks = []
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("Your tasks:", tasks)
    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Removed!")
        else:
            print("Task not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")