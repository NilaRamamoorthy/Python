import string
import secrets
import re
from functools import wraps

# Decorator to exclude similar characters
def exclude_similar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        password = func(*args, **kwargs)
        # Define characters to exclude
        exclude = {'l', '1', 'I', 'O', '0'}
        # Remove similar characters
        return ''.join(char for char in password if char not in exclude)
    return wrapper

# Password Generator Class
class RandomPasswordGenerator:
    def __init__(self):
        # Define pools of characters
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = string.punctuation
        self.all_chars = self.lowercase + self.uppercase + self.digits + self.special_chars

    @exclude_similar
    def generate(self, length=12):
        """Generates a random password of specified length."""
        if not isinstance(length, int) or length < 8:
            raise ValueError("Password length must be an integer greater than or equal to 8.")
        return ''.join(secrets.choice(self.all_chars) for _ in range(length))

    def password_generator(self):
        """Yields infinite random passwords."""
        while True:
            yield self.generate()

# Example usage
if __name__ == "__main__":
    generator = RandomPasswordGenerator()

    # Generate a single password
    try:
        password = generator.generate(12)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

    # Generate passwords indefinitely
    print("\nGenerating passwords indefinitely (press Ctrl+C to stop):")
    for password in generator.password_generator():
        print(password)
