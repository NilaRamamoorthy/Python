import json

FILE = "library.json"

def load_books():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    genres = input("Genres (comma separated): ").split(",")
    book = {
        "info": (title, author, year),
        "genres": list(set([g.strip() for g in genres])),
        "available": True
    }
    data = load_books()
    data.append(book)
    save_books(data)
    print("Book added!")

def search_books():
    keyword = input("Enter title or author to search: ").lower()
    books = load_books()
    for book in books:
        title, author, _ = book["info"]
        if keyword in title.lower() or keyword in author.lower():
            print(f"\nTitle: {title}\nAuthor: {author}\nGenres: {book['genres']}\nAvailable: {book['available']}")
