import os
from library.config import EBOOK_FOLDER

def search_by_keyword(keyword):
    results = []
    for filename in os.listdir(EBOOK_FOLDER):
        if filename.endswith(".txt"):
            with open(os.path.join(EBOOK_FOLDER, filename), "r", encoding="utf-8") as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    results.append(filename)
    return results
