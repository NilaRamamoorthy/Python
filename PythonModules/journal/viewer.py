# journal/viewer.py

import os
import fnmatch
import re

JOURNAL_DIR = "journal_entries"

def view_all():
    print("\n🗂 All Journal Entries:\n")
    for filename in sorted(os.listdir(JOURNAL_DIR)):
        print(f"\n📅 {filename}")
        with open(os.path.join(JOURNAL_DIR, filename), "r") as file:
            print(file.read())

def search_entries(keyword):
    print(f"\n🔍 Searching for keyword: '{keyword}'\n")
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    
    for filename in os.listdir(JOURNAL_DIR):
        path = os.path.join(JOURNAL_DIR, filename)
        with open(path, "r") as file:
            lines = file.readlines()
            matches = [line for line in lines if pattern.search(line)]
            if matches:
                print(f"\n📅 {filename}")
                for match in matches:
                    print("  " + match.strip())
