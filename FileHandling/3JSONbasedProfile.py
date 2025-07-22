import json
import os

FILENAME = "profiles.json"

def load_profiles():
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_profiles(profiles):
    with open(FILENAME, "w") as f:
        json.dump(profiles, f, indent=4)

def add_profile(name, email, age, phone):
    profiles = load_profiles()
    profiles[name] = {
        "email": email,
        "age": age,
        "phone": phone
    }
    save_profiles(profiles)
    print("Profile added successfully.")

def view_profiles():
    profiles = load_profiles()
    if not profiles:
        print("No profiles found.")
    for name, data in profiles.items():
        print(f"\nName: {name}")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")

def update_profile(name):
    profiles = load_profiles()
    if name in profiles:
        email = input("New Email: ")
        age = input("New Age: ")
        phone = input("New Phone: ")
        profiles[name] = {
            "email": email,
            "age": age,
            "phone": phone
        }
        save_profiles(profiles)
        print("Profile updated.")
    else:
        print("Profile not found.")

def delete_profile(name):
    profiles = load_profiles()
    try:
        del profiles[name]
        save_profiles(profiles)
        print("Profile deleted.")
    except KeyError:
        print("Profile not found.")

# Demo usage
add_profile("Alice", "alice@mail.com", 25, "9999999999")
add_profile("Bob", "bob@mail.com", 30, "8888888888")
view_profiles()
update_profile("Alice")
delete_profile("Bob")
view_profiles()
