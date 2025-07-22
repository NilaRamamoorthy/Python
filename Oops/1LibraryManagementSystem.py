from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

# Abstract Person class
class Person(ABC):
    def __init__(self, name, person_id):
        self.name = name
        self._id = person_id  # Encapsulated

    @abstractmethod
    def get_role(self):
        pass

# Member class
class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrowed_books = []

    def get_role(self):
        return "Member"

    def borrow_book(self, book, transaction_list):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            transaction_list.append(Transaction(self, book, "borrow"))
        else:
            print(f"'{book.title}' is currently unavailable.")

    def return_book(self, book, transaction_list):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            transaction_list.append(Transaction(self, book, "return"))

# Librarian class
class Librarian(Person):
    def __init__(self, name, librarian_id):
        super().__init__(name, librarian_id)

    def get_role(self):
        return "Librarian"

    def add_book(self, book, book_list):
        book_list.append(book)

    def remove_book(self, book, book_list):
        if book in book_list:
            book_list.remove(book)

    def search_book(self, title, book_list):
        return [book for book in book_list if title.lower() in book.title.lower()]

# Transaction class
class Transaction:
    def __init__(self, member, book, action):
        self.member = member
        self.book = book
        self.action = action
        self.date = datetime.now()
        self.due_date = self.date + timedelta(days=14) if action == "borrow" else None

    def __str__(self):
        return f"{self.member.name} {self.action}ed '{self.book.title}' on {self.date.strftime('%d-%m-%Y')}"

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.transactions = []

    def __len__(self):
        return len(self.books)

    def show_books(self):
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book} - {status}")

    def show_transactions(self):
        for t in self.transactions:
            print(t)
