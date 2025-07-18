# books.py

# Set of available genres
genres = {"Fiction", "Science", "History", "Biography"}

# Dictionary to store books with ISBN tuple as key
library_books = {}

def add_book(isbn, title, author, genre):
    if genre not in genres:
        print(f"Genre '{genre}' is not recognized.")
        return
    if isbn in library_books:
        print("Book with this ISBN already exists.")
        return
    library_books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "available": True
    }
    print(f"Book '{title}' added successfully.")

def list_books():
    if not library_books:
        print("No books in the library.")
        return
    print("\nLibrary Books:")
    for isbn, details in library_books.items():
        status = "Available" if details["available"] else "Issued"
        print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Genre: {details['genre']}, Status: {status}")
    print()

def issue_book(isbn):
    if isbn in library_books and library_books[isbn]["available"]:
        library_books[isbn]["available"] = False
        print(f"Book '{library_books[isbn]['title']}' has been issued.")
    else:
        print("Book is either not found or already issued.")
