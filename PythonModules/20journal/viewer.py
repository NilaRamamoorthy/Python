import os
import fnmatch

def view_entry(date_str):
    filepath = os.path.join("journal_entries", f"{date_str}.txt")
    if os.path.exists(filepath):
        with open(filepath) as file:
            print(file.read())
    else:
        print("No entry found for that date.")

def search_entries(keyword):
    folder = "journal_entries"
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)
            with open(path) as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    print(f"Match found in {file}:\n")
                    print(content)
                    print("-" * 40)
