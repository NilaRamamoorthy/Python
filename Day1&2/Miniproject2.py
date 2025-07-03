name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

contact = {
    "Name": name,
    "Phone": phone,
    "Email": email
}
print("\n--- Contact Information ---")
print("Name :", contact["Name"], " (Type:", type(contact["Name"]), ")")
print("Phone:", contact["Phone"], " (Type:", type(contact["Phone"]), ")")
print("Email:", contact["Email"], " (Type:", type(contact["Email"]), ")")

