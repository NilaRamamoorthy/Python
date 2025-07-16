# Initial book catalog
library = {
    101: {"title": "Python Basics", "author": "John Smith", "copies": 3},
    102: {"title": "Data Science 101", "author": "Jane Doe", "copies": 2}
}

# 1. Add new book
library[103] = {"title": "Machine Learning", "author": "Andrew Ng", "copies": 1}

# 2. Borrow a book
book_id = 101
if library.get(book_id):
    if library[book_id]["copies"] > 0:
        library[book_id]["copies"] -= 1
    else:
        print(f"{library[book_id]['title']} is not available")
else:
    print("Book ID not found")

# 3. Return a book
library[101]["copies"] += 1

# 4. Delete book if copies = 0
for book_id in list(library.keys()):
    if library[book_id]["copies"] == 0:
        library.pop(book_id)

# 5. Use .get() for safe access
book_info = library.get(104, "Book not found")
print("\nBook 104 info:", book_info)

# 6. Display available books
print("\nAvailable Books:")
for book_id, info in library.items():
    print(f"{book_id} - {info['title']} by {info['author']} ({info['copies']} copies)")
