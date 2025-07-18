import os
from library.config import EBOOK_FOLDER

def list_ebooks():
    if not os.path.exists(EBOOK_FOLDER):
        print("Ebook folder does not exist.")
        return []
    return [f for f in os.listdir(EBOOK_FOLDER) if f.endswith(".txt")]

def show_catalog():
    ebooks = list_ebooks()
    print("\n--- eBook Catalog ---")
    for i, book in enumerate(ebooks, 1):
        print(f"{i}. {book}")
