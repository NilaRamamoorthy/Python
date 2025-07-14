# Book Reading Progress Tracker

# Each book: [title, pages read, total pages]
books = [
    ["The Alchemist", 100, 200],
    ["Python Basics", 50, 150]
]

# Add a new book
title = input("Enter book title: ").strip().title()
pages_read = int(input("Enter pages read: "))
total_pages = int(input("Enter total pages: "))
books.append([title, pages_read, total_pages])

# Update page count for a book
update_title = input("\nEnter book title to update progress: ").strip().title()
new_read = int(input("Enter new pages read: "))
for book in books:
    if book[0] == update_title:
        book[1] = new_read
        break
else:
    print("Book not found.")

# Check reading status
print("\nReading Progress:")
for book in books:
    status = "Finished" if book[1] >= book[2] else "In Progress"
    print(f"{book[0]}: {book[1]}/{book[2]} pages - {status}")
