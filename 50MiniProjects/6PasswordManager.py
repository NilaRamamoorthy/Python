from cryptography.fernet import Fernet
import os
import json
import random
import string
from functools import wraps

# File paths
KEY_FILE = "secret.key"
DATA_FILE = "passwords.json"

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

fernet = Fernet(load_key())

# Decorator for simulated login
def logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("🔐 User authenticated.")
        return func(*args, **kwargs)
    return wrapper

# Password entry class
class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "website": self.website,
            "username": self.username,
            "password": fernet.encrypt(self.password.encode()).decode()
        }

# Password manager logic
class PasswordManager:
    def __init__(self):
        self.entries = self.load_passwords()
        self.compromised = set()

    def load_passwords(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    def save_passwords(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.entries, file, indent=4)

    @logged_in
    def add_entry(self, website, username, password):
        entry = PasswordEntry(website, username, password)
        self.entries.append(entry.to_dict())
        self.save_passwords()
        print("✅ Password added.")

    @logged_in
    def retrieve_entry(self, website):
        for entry in self.entries:
            if entry["website"] == website:
                decrypted_pw = fernet.decrypt(entry["password"].encode()).decode()
                print(f"🔍 Username: {entry['username']}, Password: {decrypted_pw}")
                return
        print("❌ Website not found.")

    @logged_in
    def delete_entry(self, website):
        for i, entry in enumerate(self.entries):
            if entry["website"] == website:
                self.entries.pop(i)
                self.save_passwords()
                print("🗑️ Entry deleted.")
                return
        print("❌ Website not found.")

    def generate_strong_password(self, length=12):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    def weak_passwords(self):
        for entry in self.entries:
            decrypted_pw = fernet.decrypt(entry["password"].encode()).decode()
            if len(decrypted_pw) < 6 or decrypted_pw.isalpha():
                yield (entry["website"], decrypted_pw)

# Menu interface
def menu():
    manager = PasswordManager()
    while True:
        print("\n--- Password Manager ---")
        print("1. Add password")
        print("2. Retrieve password")
        print("3. Delete password")
        print("4. Generate strong password")
        print("5. List weak passwords")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            w = input("Website: ")
            u = input("Username: ")
            p = input("Password: ")
            manager.add_entry(w, u, p)

        elif choice == '2':
            w = input("Website: ")
            manager.retrieve_entry(w)

        elif choice == '3':
            w = input("Website: ")
            manager.delete_entry(w)

        elif choice == '4':
            print("🔐 Generated Password:", manager.generate_strong_password())

        elif choice == '5':
            print("⚠️ Weak Passwords:")
            for site, pw in manager.weak_passwords():
                print(f"{site}: {pw}")

        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option.")

menu()
