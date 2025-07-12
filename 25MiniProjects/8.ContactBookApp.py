# Contact Book App

contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip().lower()
    contacts.append([name, phone, email])
    print(f"✅ Contact '{name}' added successfully.")

# Function to show all contacts
def show_contacts():
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📒 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

# Function to search contact
def search_contact():
    keyword = input("Enter name/phone/email to search: ").strip().lower()
    found = False
    for contact in contacts:
        if keyword in contact[0].lower() or keyword in contact[1] or keyword in contact[2]:
            print(f"🔍 Found: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            found = True
    if not found:
        print("❌ Contact not found.")

# Function to delete a contact
def delete_contact():
    show_contacts()
    if not contacts:
        return
    try:
        num = int(input("Enter contact number to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            print(f"🗑️ Contact '{removed[0]}' deleted.")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main loop
def contact_book():
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the contact book
contact_book()
