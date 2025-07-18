import json

CONTACT_FILE = "contact_book/contacts.json"

def load_contacts():
    try:
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)
