from lending_ops import add_book, return_book, books
from reminder_ops import check_overdue

add_book("Python Basics", "John", "2025-07-10")
add_book("AI Revolution", "Sara", "2025-07-25")
add_book("Python Basics", "Mike", "2025-07-22")  # Already borrowed

return_book("Python Basics")
add_book("Python Basics", "Mike", "2025-07-22")

check_overdue(books)
