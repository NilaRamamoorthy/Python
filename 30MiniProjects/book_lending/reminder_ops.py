from datetime import datetime

def check_overdue(books):
    today = datetime.today().date()
    print("\n--- Overdue Books ---")
    found = False
    for title, (borrower, due_date_str) in books.items():
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        if due_date < today:
            print(f"{title} is overdue! Borrower: {borrower}, Due: {due_date}")
            found = True
    if not found:
        print("No overdue books.")
