# main.py

from book_manager.books import add_book, list_books, issue_book
from user_manager.users import issue_to_user

# Add sample books
add_book(("978-0-123456-47-2",), "The Science of Everything", "John Smith", "Science")
add_book(("978-1-234567-89-7",), "Historical Tales", "Mary Gold", "History")
add_book(("978-0-123456-47-2",), "Duplicate ISBN", "Duplicate", "Fiction")  # Duplicate test
add_book(("978-9-876543-21-0",), "Unknown Genre Book", "Ghost Writer", "Fantasy")  # Invalid genre

# List all books
list_books()

# Issue book to user
issue_book(("978-0-123456-47-2",))
issue_to_user((101,), "Alice", ("978-0-123456-47-2",))

# Issue again to check status
issue_book(("978-0-123456-47-2",))
