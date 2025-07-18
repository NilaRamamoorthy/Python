from contact_book.storage import load_contacts, save_contacts

def update_contact(name, phone=None, email=None):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("Contact not found.")
