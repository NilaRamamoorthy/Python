from library.catalog import show_catalog
from library.reader import read_book
from library.search import search_by_keyword

while True:
    print("\n1. Show Catalog\n2. Search by Keyword\n3. Read a Book\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        show_catalog()
    elif choice == "2":
        keyword = input("Enter keyword to search: ")
        found = search_by_keyword(keyword)
        if found:
            print("Books containing keyword:")
            for book in found:
                print("-", book)
        else:
            print("No books found.")
    elif choice == "3":
        filename = input("Enter filename (e.g., book1.txt): ")
        read_book(filename)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
