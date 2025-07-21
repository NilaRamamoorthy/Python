from book_ops import load_books, save_books

def borrow_book():
    title = input("Enter the title to borrow: ").strip()
    books = load_books()
    for book in books:
        if book["info"][0].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                save_books(books)
                print(f"You borrowed '{title}'")
            else:
                print("Sorry, book is already borrowed.")
            return
    print("Book not found.")

def return_book():
    title = input("Enter the title to return: ").strip()
    books = load_books()
    for book in books:
        if book["info"][0].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                save_books(books)
                print(f"Thank you for returning '{title}'")
            else:
                print("Book was not borrowed.")
            return
    print("Book not found.")

def list_unique_genres():
    books = load_books()
    genre_set = set()
    for book in books:
        genre_set.update(book["genres"])
    print("\nUnique Genres:")
    for genre in genre_set:
        print(f"- {genre}")
