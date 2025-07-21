# book_data.py

from typing import List, Dict, Set, Tuple

books: List[Dict] = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genres": {"fiction", "philosophy"}},
    {"title": "1984", "author": "George Orwell", "genres": {"dystopia", "political", "fiction"}},
    {"title": "Becoming", "author": "Michelle Obama", "genres": {"biography", "inspirational"}},
    {"title": "Harry Potter", "author": "J.K. Rowling", "genres": {"fantasy", "fiction", "adventure"}},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "genres": {"history", "science", "non-fiction"}}
]

# Create genre → books dictionary
genre_to_books: Dict[str, Set[Tuple[str, str]]] = {}

for book in books:
    title_author = (book["title"], book["author"])
    for genre in book["genres"]:
        genre_to_books.setdefault(genre, set()).add(title_author)
