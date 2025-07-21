from datetime import datetime

books = {}  # title → (borrower, due_date)
borrowers = set()

def add_book(title, borrower, due_date):
    if title in books:
        print(f"{title} is already borrowed.")
    else:
        books[title] = (borrower, due_date)
        borrowers.add(borrower)
        print(f"Book '{title}' borrowed by {borrower} until {due_date}.")

def return_book(title):
    if title in books:
        borrower = books[title][0]
        del books[title]
        print(f"Book '{title}' returned by {borrower}.")
    else:
        print(f"Book '{title}' is not in the system.")
