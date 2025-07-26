import random
import string
import os
import base64
from cryptography.fernet import Fernet

# Generate or load encryption key
KEY_FILE = 'key.key'

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
    return key

key = load_key()
cipher = Fernet(key)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character types selected!")

    return ''.join(random.choice(char_pool) for _ in range(length))

def password_strength(password):
    length = len(password)
    categories = 0
    categories += any(c.islower() for c in password)
    categories += any(c.isupper() for c in password)
    categories += any(c.isdigit() for c in password)
    categories += any(c in string.punctuation for c in password)

    score = length + categories * 5
    if score < 10:
        return "Weak"
    elif score < 20:
        return "Medium"
    else:
        return "Strong"

def save_passwords(passwords):
    data = '\n'.join(passwords).encode()
    encrypted = cipher.encrypt(data)
    with open('passwords.enc', 'wb') as f:
        f.write(encrypted)
    print("Passwords saved encrypted to passwords.enc")

def main():
    print("Password Generator")
    length = int(input("Password length: "))
    use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    count = int(input("How many passwords to generate? "))

    passwords = []
    for _ in range(count):
        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        strength = password_strength(pwd)
        print(f"{pwd}  (Strength: {strength})")
        passwords.append(pwd)

    save = input("Save passwords encrypted? (y/n): ").lower()
    if save == 'y':
        save_passwords(passwords)

if __name__ == "__main__":
    import os
    main()
