import json
import csv
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    category = input("Category (family/work/other): ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'category': category
    })
    print("Contact added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} - {c['phone']} - {c['email']} [{c['category']}]")

def search_contacts(contacts):
    query = input("Enter name or phone: ").lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        for c in results:
            print(f"{c['name']} - {c['phone']} - {c['email']} [{c['category']}]")
    else:
        print("No matching contacts.")

def edit_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter contact number to edit: ")) - 1
    if 0 <= idx < len(contacts):
        contacts[idx]['name'] = input("New Name: ") or contacts[idx]['name']
        contacts[idx]['phone'] = input("New Phone: ") or contacts[idx]['phone']
        contacts[idx]['email'] = input("New Email: ") or contacts[idx]['email']
        contacts[idx]['category'] = input("New Category: ") or contacts[idx]['category']
        print("Contact updated.")
    else:
        print("Invalid contact number.")

def delete_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter contact number to delete: ")) - 1
    if 0 <= idx < len(contacts):
        removed = contacts.pop(idx)
        print(f"Deleted {removed['name']}")
    else:
        print("Invalid contact number.")

def export_to_csv(contacts):
    with open('contacts_export.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'phone', 'email', 'category'])
        writer.writeheader()
        writer.writerows(contacts)
    print("Contacts exported to contacts_export.csv")

def group_by_category(contacts):
    categories = {}
    for contact in contacts:
        cat = contact['category']
        categories.setdefault(cat, []).append(contact)

    for cat, items in categories.items():
        print(f"\nCategory: {cat}")
        for c in items:
            print(f"- {c['name']} ({c['phone']})")

def contact_book_app():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Export to CSV")
        print("7. Group by Category")
        print("8. Exit")
        choice = input("Choose: ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            export_to_csv(contacts)
        elif choice == '7':
            group_by_category(contacts)
        elif choice == '8':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run the app
contact_book_app()
