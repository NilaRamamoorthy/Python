from contact_book.storage import load_contacts, save_contacts

def delete_contact(name):
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(contacts) == len(updated_contacts):
        print("Contact not found.")
    else:
        save_contacts(updated_contacts)
        print("Contact deleted.")
