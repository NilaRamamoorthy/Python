import logging
import re

# Setup logging
logging.basicConfig(filename="registration_errors.log", level=logging.ERROR, format='%(asctime)s - %(message)s')

# Custom Exception
class PasswordTooWeakError(Exception):
    pass

def validate_registration(name, email, age, password):
    try:
        # Assert pre-check: All fields must be non-empty
        assert all([name, email, age, password]), "All fields must be filled."

        # Type checks
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")

        # Age validation
        age = int(age)  # May raise ValueError
        if age < 13:
            raise ValueError("User must be at least 13 years old.")

        # Email format validation
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email):
            raise ValueError("Invalid email format.")

        # Password strength check
        if len(password) < 6 or password.isalpha() or password.isdigit():
            raise PasswordTooWeakError("Password must be at least 6 characters and contain letters and numbers.")

        print("✅ Registration successful!")

    except (AssertionError, TypeError, ValueError, PasswordTooWeakError) as e:
        logging.error(f"Registration error: {e}")
        print("❌ Registration failed:", e)

# Sample Usage
validate_registration("Alice", "alice@example.com", "22", "pass123")
# validate_registration("", "notanemail", "abc", "123")  # Uncomment to test failures
