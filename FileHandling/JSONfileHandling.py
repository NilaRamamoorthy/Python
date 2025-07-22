import json
import os

# 36. Save user profile data (name, age, skills) into a .json file
def save_profile(profile, filename="profiles.json"):
    with open(filename, "w") as file:
        json.dump(profile, file, indent=4)

# Demo
user_profile = {"name": "Alice", "age": 25, "skills": ["Python", "HTML"]}
save_profile(user_profile)

# 37. Read a .json file and display all user profiles
def read_profiles(filename="profiles.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("User Profiles:")
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("File not found.")

# Demo
read_profiles()

# 38. Add a new entry into the existing .json data and save it back
def add_profile(new_profile, filename="profiles.json"):
    data = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    data = [data]
            except json.JSONDecodeError:
                pass
    data.append(new_profile)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Demo
new_user = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
add_profile(new_user)

# 39. Build a mini phonebook app using .json as the database
def save_phonebook(phonebook, filename="phonebook.json"):
    with open(filename, "w") as file:
        json.dump(phonebook, file, indent=4)

def add_contact(name, number, filename="phonebook.json"):
    phonebook = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                phonebook = json.load(file)
            except json.JSONDecodeError:
                pass
    phonebook[name] = number
    save_phonebook(phonebook, filename)

def view_phonebook(filename="phonebook.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("Phonebook Entries:")
            for name, number in data.items():
                print(f"{name}: {number}")
    except FileNotFoundError:
        print("Phonebook not found.")

# Demo
add_contact("Charlie", "9876543210")
view_phonebook()

# 40. Validate if a .json file contains required keys and handle errors
def validate_json(filename="profiles.json", required_keys=["name", "age", "skills"]):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                data = [data]
            for profile in data:
                for key in required_keys:
                    if key not in profile:
                        raise KeyError(f"Missing key: {key}")
            print("All profiles are valid.")
    except Exception as e:
        print(f"Validation error: {e}")

# Demo
validate_json()
