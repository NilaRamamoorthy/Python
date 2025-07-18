from contact_book.storage import load_contacts, save_contacts

def add_contact(name, phone, email):
    contacts = load_contacts()
    new_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully.")
