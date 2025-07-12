# Library Due Date Calculator

from datetime import datetime, timedelta

# Function to calculate due date
def calculate_due_date():
    print(" Library Due Date Calculator")

    book_name = input("Enter the book name: ").strip().title()
    borrow_date_input = input("Enter the borrow date (YYYY-MM-DD): ").strip()

    try:
        borrow_date = datetime.strptime(borrow_date_input, "%Y-%m-%d")
        due_date = borrow_date + timedelta(days=7)

        print("\n Book Summary:")
        print(f"Book Name     : {book_name}")
        print(f"Borrowed On   : {borrow_date.strftime('%d %b %Y')}")
        print(f"Due Date      : {due_date.strftime('%d %b %Y')}")
    except ValueError:
        print(" Invalid date format. Please use YYYY-MM-DD.")

# Run the app
calculate_due_date()
