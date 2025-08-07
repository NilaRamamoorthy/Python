import json
from datetime import datetime, timedelta
from functools import wraps

DATA_FILE = "library_data.json"

# Decorator to restrict certain actions to admin
def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = input("Enter user role (admin/user): ").strip().lower()
        if user != "admin":
            print("❌ Access denied. Admins only.")
            return
        return func(*args, **kwargs)
    return wrapper

# Book class
class Book:
    def __init__(self, title, author, available=True, due_date=None):
        self.title = title
        self.author = author
        self.available = available
        self.due_date = due_date  # None or ISO format date

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available,
            "due_date": self.due_date
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["available"], data["due_date"])

    def __str__(self):
        status = "Available" if self.available else f"Borrowed (Due: {self.due_date})"
        return f"📚 {self.title} by {self.author} - {status}"

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def save_books(self):
        with open(DATA_FILE, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def load_books(self):
        try:
            with open(DATA_FILE, "r") as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]
        except FileNotFoundError:
            self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        self.save_books()
        print(f"✅ Book '{title}' added.")

    @admin_only
    def delete_book(self, title):
        for i, book in enumerate(self.books):
            if book.title.lower() == title.lower():
                del self.books[i]
                self.save_books()
                print(f"🗑️ Book '{title}' deleted.")
                return
        print("❌ Book not found.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                book.due_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
                self.save_books()
                print(f"📕 Borrowed '{title}'. Return by {book.due_date}")
                return
        print("❌ Book not available or not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                book.due_date = None
                self.save_books()
                print(f"📗 Returned '{title}'.")
                return
        print("❌ Book not borrowed or not found.")

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
        print("🔍 Search complete.")

    def list_overdue_books(self):
        today = datetime.now().date()
        print("📅 Overdue Books:")
        for book in self.books:
            if book.due_date and datetime.strptime(book.due_date, "%Y-%m-%d").date() < today:
                print(f"{book.title} (Due: {book.due_date})")

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        while self._iter_index < len(self.books):
            book = self.books[self._iter_index]
            self._iter_index += 1
            if book.available:
                return book
        raise StopIteration

# Menu
def menu():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. List Available Books")
        print("7. List Overdue Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(title, author)
        elif choice == '2':
            title = input("Title to delete: ")
            lib.delete_book(title)
        elif choice == '3':
            title = input("Book to borrow: ")
            lib.borrow_book(title)
        elif choice == '4':
            title = input("Book to return: ")
            lib.return_book(title)
        elif choice == '5':
            title = input("Search title: ")
            lib.search_book(title)
        elif choice == '6':
            print("📘 Available Books:")
            for book in lib:
                print(book)
        elif choice == '7':
            lib.list_overdue_books()
        elif choice == '8':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice.")

menu()
