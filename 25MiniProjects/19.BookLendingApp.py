# Book Lending App

books = ["Python Basics", "Data Science 101", "Machine Learning", "AI for Beginners", "Deep Learning"]
borrowed_books = []

# Function to display available books
def show_books():
    print("\n Available Books:")
    if books:
        for book in books:
            print(f"- {book}")
    else:
        print(" No books available.")

# Function to borrow a book
def borrow_book():
    show_books()
    book_name = input("\nEnter the name of the book to borrow: ").strip().title()
    if book_name in books:
        books.remove(book_name)
        borrowed_books.append(book_name)
        print(f" You borrowed: {book_name}")
    else:
        print(" Book not available.")

# Function to return a book
def return_book():
    book_name = input("Enter the name of the book to return: ").strip().title()
    if book_name in borrowed_books:
        borrowed_books.remove(book_name)
        books.append(book_name)
        print(f" You returned: {book_name}")
    else:
        print(" Book not in borrowed list.")

# Main menu loop
def lending_app():
    print(" Book Lending App")
    while True:
        print("\nChoose an option:")
        print("1. Show Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ").strip()
        if choice == "1":
            show_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            print("Thank you for using the Book Lending App.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
lending_app()
