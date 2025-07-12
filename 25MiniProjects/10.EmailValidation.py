# Email Validation Program

# Function to check email validity
def is_valid_email(email):
    if "@" in email and "." in email:
        at_pos = email.find("@")
        dot_pos = email.rfind(".")
        username = email[:at_pos]
        domain = email[at_pos+1:]

        # Conditions: valid position of @ and ., username > 5, domain includes "gmail.com"
        if len(username) > 5 and at_pos < dot_pos and domain.endswith("gmail.com"):
            return True
    return False

# Main loop
def email_validator():
    while True:
        email = input("Enter your email (or type 'exit' to stop): ").strip().lower()
        if email == "exit":
            print("Exiting Email Validator.")
            break
        if is_valid_email(email):
            print("Email is valid!")
        else:
            print("Invalid email. Make sure it contains '@', '.', has username > 5, and domain is 'gmail.com'.")

# Run the validator
email_validator()
