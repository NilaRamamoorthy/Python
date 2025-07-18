from contact_book.add import add_contact
from contact_book.update import update_contact
from contact_book.delete import delete_contact
from contact_book.search import search_contact

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            name = input("Enter name to update: ")
            phone = input("New phone (or press Enter to skip): ")
            email = input("New email (or press Enter to skip): ")
            update_contact(name, phone or None, email or None)
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "4":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
