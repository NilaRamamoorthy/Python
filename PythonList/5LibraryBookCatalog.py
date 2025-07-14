# Library Book Catalog

# List of books: [Title, Author]
books = [
    ["Wings of Fire", "A.P.J. Abdul Kalam"],
    ["The Alchemist", "Paulo Coelho"],
    ["Rich Dad Poor Dad", "Robert Kiyosaki"]
]

# Display all books
print("Library Catalog:")
for book in books:
    print(f" {book[0]} by {book[1]}")

# Add a new book
books.append(["Ikigai", "Francesc Miralles"])
print("\nAfter adding 'Ikigai':")
for book in books:
    print(f"{book[0]} by {book[1]}")

# Update a book's author
for book in books:
    if book[0] == "The Alchemist":
        book[1] = "Paulo C."
print("\nAfter updating author of 'The Alchemist':")
print(books)

# Search for a book
search_title = "Rich Dad Poor Dad"
found = False
for book in books:
    if book[0] == search_title:
        print(f"\nFound '{search_title}' in the catalog.")
        found = True
        break
if not found:
    print(f"\n'{search_title}' not found in the catalog.")

# Show recent 2 additions using slicing
print("\nRecent Additions:")
for book in books[-2:]:
    print(f" {book[0]}")
