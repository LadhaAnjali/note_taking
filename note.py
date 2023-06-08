notes = []

while True:
    print("Note Taking App")
    print("1. Add a note")
    print("2. View notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")
        notes.append(note)
        print("Note added successfully!\n")
    elif choice == "2":
        print("Your notes:")
        if len(notes) == 0:
            print("No notes found.\n")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")
            print()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
