from book_ops import add_book, search_books
from user_ops import borrow_book, return_book, list_unique_genres

def main():
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book\n2. Search Book\n3. Borrow Book\n4. Return Book\n5. Show Genres\n6. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            search_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            list_unique_genres()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
