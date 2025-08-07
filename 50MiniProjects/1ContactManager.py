import json
import re
from functools import wraps

# Decorator to log actions
def log_actions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Contact class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {'name': self.name, 'phone': self.phone, 'email': self.email}

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

# Contact Manager class
class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.contacts = {}
        self.filename = filename
        self.load_contacts()

    @log_actions
    def add_contact(self, name, phone, email):
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        self.contacts[name] = Contact(name, phone, email)
        self.save_contacts()

    @log_actions
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
        else:
            print("Contact not found.")

    @log_actions
    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            print("Contact not found.")
            return
        if phone:
            if not self.validate_phone(phone):
                raise ValueError("Invalid phone number format.")
            self.contacts[name].phone = phone
        if email:
            if not self.validate_email(email):
                raise ValueError("Invalid email format.")
            self.contacts[name].email = email
        self.save_contacts()

    @log_actions
    def search_contact(self, search_term):
        return (contact for name, contact in self.contacts.items() if search_term.lower() in name.lower())

    @log_actions
    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts.values():
            print("-" * 30)
            print(contact)

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump({name: contact.to_dict() for name, contact in self.contacts.items()}, f, indent=4)

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for name, info in data.items():
                    self.contacts[name] = Contact(info['name'], info['phone'], info['email'])
        except FileNotFoundError:
            pass

    @staticmethod
    def validate_phone(phone):
        return re.fullmatch(r'\+?\d{10,15}', phone) is not None

    @staticmethod
    def validate_email(email):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Menu-driven interface
def main():
    manager = ContactManager()

    menu = """
    ----- Contact Manager -----
    1. Add Contact
    2. Delete Contact
    3. Update Contact
    4. Search Contact
    5. Display All Contacts
    6. Exit
    """

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                manager.add_contact(name, phone, email)
                print("Contact added successfully.\n")
            elif choice == '2':
                name = input("Enter name to delete: ")
                manager.delete_contact(name)
                print("Contact deleted.\n")
            elif choice == '3':
                name = input("Enter name to update: ")
                phone = input("New phone (leave blank to keep unchanged): ")
                email = input("New email (leave blank to keep unchanged): ")
                manager.update_contact(name, phone or None, email or None)
                print("Contact updated.\n")
            elif choice == '4':
                search = input("Enter name to search: ")
                results = manager.search_contact(search)
                found = False
                for contact in results:
                    print("-" * 30)
                    print(contact)
                    found = True
                if not found:
                    print("No matching contacts found.")
            elif choice == '5':
                manager.display_all_contacts()
            elif choice == '6':
                print("Exiting Contact Manager. Goodbye!")
                break
            else:
                print("Invalid option. Try again.\n")
        except ValueError as ve:
            print(f"Error: {ve}\n")

if __name__ == "__main__":
    main()
