from journal.entry import add_entry
from journal.viewer import view_entry, search_entries
from journal.exporter import export_all_entries

def main():
    while True:
        print("\n1. Add Entry\n2. View Entry\n3. Search Entries\n4. Export All\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            note = input("Write your journal note: ")
            add_entry(note)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            view_entry(date)
        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            search_entries(keyword)
        elif choice == "4":
            export_all_entries()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
