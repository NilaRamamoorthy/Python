# journal/entry.py

import os
from datetime import datetime
import textwrap

JOURNAL_DIR = "journal_entries"

def add_entry():
    os.makedirs(JOURNAL_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(JOURNAL_DIR, f"{today}.txt")
    
    print(f"\n--- Journal Entry for {today} ---")
    entry = input("Write your journal entry:\n> ")

    with open(filename, "a") as file:
        wrapped = textwrap.fill(entry, width=80)
        file.write(f"{datetime.now().strftime('%H:%M')} - {wrapped}\n")

    print(f"✅ Entry saved to {filename}")
