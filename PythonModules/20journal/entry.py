import os
from datetime import datetime

def add_entry(note):
    today = datetime.now().strftime("%Y-%m-%d")
    folder = "journal_entries"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{today}.txt")
    
    with open(filepath, "a") as file:
        timestamp = datetime.now().strftime("%H:%M")
        file.write(f"[{timestamp}] {note}\n")
    
    print(f"Note added to {filepath}")
