import json
import os

FILENAME = "resumes.json"

def load_resumes():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}

def save_resumes(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def add_resume():
    name = input("Enter full name: ").strip()
    email = input("Enter email: ")
    skills = input("Enter skills (comma-separated): ").split(",")
    experience = input("Enter years of experience: ")
    education = input("Enter education details: ")

    resumes = load_resumes()
    resumes[name] = {
        "email": email,
        "skills": [s.strip() for s in skills],
        "experience": experience,
        "education": education
    }
    save_resumes(resumes)
    print(f"Resume for {name} added.")

def view_resume():
    name = input("Enter candidate name to view: ").strip()
    resumes = load_resumes()
    if name in resumes:
        print(json.dumps(resumes[name], indent=4))
    else:
        print("Resume not found.")

def update_resume():
    name = input("Enter candidate name to update: ").strip()
    resumes = load_resumes()
    if name in resumes:
        print("Leave field blank to keep existing value.")
        email = input(f"Email [{resumes[name]['email']}]: ") or resumes[name]['email']
        skills = input(f"Skills (comma-separated) [{', '.join(resumes[name]['skills'])}]: ")
        experience = input(f"Experience [{resumes[name]['experience']}]: ") or resumes[name]['experience']
        education = input(f"Education [{resumes[name]['education']}]: ") or resumes[name]['education']

        resumes[name] = {
            "email": email,
            "skills": [s.strip() for s in skills.split(",")] if skills else resumes[name]['skills'],
            "experience": experience,
            "education": education
        }
        save_resumes(resumes)
        print("Resume updated.")
    else:
        print("Resume not found.")

def main():
    while True:
        print("\n--- Resume Collector ---")
        print("1. Add Resume")
        print("2. View Resume")
        print("3. Update Resume")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_resume()
        elif choice == "2":
            view_resume()
        elif choice == "3":
            update_resume()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
