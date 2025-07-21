import json
from validator import validate_phone, validate_email

CONTACT_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone (10 digits): ")
    email = input("Enter email: ")
    tags = set(input("Enter tags (comma-separated): ").split(','))

    if not validate_phone(phone) or not validate_email(email):
        print("Invalid phone or email!")
        return

    contact = {"name": name, "phone": phone, "email": email, "tags": list(tags)}
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added!")

def search_contact(name):
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(c)
            return
    print("Contact not found!")

def delete_contact(name):
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    save_contacts(new_contacts)
    print("Contact deleted!" if len(contacts) != len(new_contacts) else "Contact not found.")

def list_contacts():
    contacts = sorted(load_contacts(), key=lambda x: x["name"])
    for c in contacts:
        print(f"{c['name']} - {c['phone']} - {c['email']} - Tags: {', '.join(c['tags'])}")

def main():
    while True:
        print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. List Contacts\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact(input("Enter name to search: "))
        elif choice == "3":
            delete_contact(input("Enter name to delete: "))
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
