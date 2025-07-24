import re
import logging

# Setup logging
logging.basicConfig(filename="invalid_emails.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Custom Exception
class InvalidEmailFormatError(Exception):
    def __init__(self, email):
        super().__init__(f"Invalid email format: {email}")
        self.email = email

# Email validation function
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailFormatError(email)

# Main function to validate multiple emails
def validate_email_list():
    emails = input("Enter comma-separated emails to validate: ").split(',')

    print("\nValid Emails:")
    for email in emails:
        email = email.strip()
        try:
            validate_email(email)
            print(f"✅ {email}")
        except InvalidEmailFormatError as e:
            print(f"❌ {e}")
            logging.info(f"{e}")

# Run
validate_email_list()
