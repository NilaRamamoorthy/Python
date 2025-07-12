# Mini Email Formatter

# Function to generate formatted email
def email_formatter():
    print(" Mini Email Formatter")
    
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    domain = input("Enter email domain (e.g., gmail.com): ").strip().lower()

    # Create email
    email = f"{first_name}.{last_name}@{domain}"
    
    print("\nFormatted Email Address:")
    print(email)

# Run the app
email_formatter()
