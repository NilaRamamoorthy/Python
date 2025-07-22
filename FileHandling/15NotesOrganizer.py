import json
import os

FILENAME = "notes.json"

def load_notes():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}

def save_notes(notes):
    with open(FILENAME, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    category = input("Enter category: ").strip()
    note = input("Enter note: ").strip()
    
    notes = load_notes()
    if category not in notes:
        notes[category] = []
    notes[category].append(note)
    save_notes(notes)
    print("Note added.")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for category, items in notes.items():
        print(f"\n{category}:")
        for idx, note in enumerate(items, 1):
            print(f"  {idx}. {note}")

def delete_note():
    notes = load_notes()
    category = input("Enter category: ").strip()
    if category not in notes or not notes[category]:
        print("Category not found or empty.")
        return
    view_notes()
    index = int(input(f"Enter note number to delete from '{category}': "))
    if 0 < index <= len(notes[category]):
        removed = notes[category].pop(index - 1)
        if not notes[category]:  # remove empty category
            del notes[category]
        save_notes(notes)
        print(f"Deleted note: {removed}")
    else:
        print("Invalid note number.")

def main():
    while True:
        print("\n--- Notes Organizer ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
