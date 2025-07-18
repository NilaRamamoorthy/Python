import os
from library.config import EBOOK_FOLDER

def read_book(filename):
    path = os.path.join(EBOOK_FOLDER, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            print("\n--- Begin Book ---")
            print(f.read(1000))  # Print first 1000 characters
            print("--- End Preview ---\n")
    else:
        print("Book not found.")
