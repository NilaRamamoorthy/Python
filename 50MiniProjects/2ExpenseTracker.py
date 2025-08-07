import csv
from datetime import datetime
from functools import wraps

# ================= Decorator =================
def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            amount = kwargs.get('amount')
            date_str = kwargs.get('date')
            category = kwargs.get('category')

            if amount is not None and (not isinstance(amount, (int, float)) or amount <= 0):
                raise ValueError("Amount must be a positive number.")

            if date_str is not None:
                datetime.strptime(date_str, "%Y-%m-%d")  # will raise ValueError if invalid

            if category is not None and not category.strip():
                raise ValueError("Category cannot be empty.")

        except ValueError as e:
            print(f"[Validation Error] {e}")
            return
        return func(*args, **kwargs)
    return wrapper

# ================= OOP: Expense Class =================
class Expense:
    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            'amount': f"{self.amount:.2f}",
            'category': self.category,
            'date': self.date
        }

    def __str__(self):
        return f"{self.date} | {self.category:<15} | ${self.amount:.2f}"

# ================= Expense Manager =================
class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.expenses = []
        self.filename = filename
        self.load_expenses()

    @validate_input
    def add_expense(self, amount, category, date):
        expense = Expense(amount, category, date)
        self.expenses.append(expense)
        self.save_expense(expense)
        print("[+] Expense added successfully.")

    def save_expense(self, expense):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['amount', 'category', 'date'])
            writer.writerow(expense.to_dict())

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.expenses.append(
                        Expense(float(row['amount']), row['category'], row['date'])
                    )
        except FileNotFoundError:
            with open(self.filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['amount', 'category', 'date'])
                writer.writeheader()

    def view_all_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nDate       | Category        | Amount")
        print("-" * 40)
        for exp in self.expenses:
            print(exp)

    def view_by_category(self, category):
        print(f"\nExpenses in category: {category}")
        for exp in self.expenses:
            if exp.category.lower() == category.lower():
                print(exp)

    def view_by_month(self, month_str):
        print(f"\nExpenses in month: {month_str}")
        for exp in self.expenses:
            if exp.date.startswith(month_str):  # format YYYY-MM
                print(exp)

    def filter_by_amount(self, threshold):
        print(f"\nExpenses > ${threshold}")
        for exp in self.expenses:
            if exp.amount > threshold:
                print(exp)

    def unique_categories(self):
        return {exp.category for exp in self.expenses}

    def expenses_in_date_range(self, start_date, end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return (
            exp for exp in self.expenses
            if start <= datetime.strptime(exp.date, "%Y-%m-%d") <= end
        )

# ================= Menu UI =================
def main():
    tracker = ExpenseTracker()

    menu = """
    -------- Expense Tracker --------
    1. Add Expense
    2. View All Expenses
    3. View by Category
    4. View by Month (YYYY-MM)
    5. Filter by Amount
    6. Show Unique Categories
    7. Show Expenses in Date Range
    8. Exit
    """

    while True:
        print(menu)
        choice = input("Enter choice: ")

        try:
            if choice == '1':
                amount = float(input("Amount: "))
                category = input("Category: ")
                date = input("Date (YYYY-MM-DD): ")
                tracker.add_expense(amount=amount, category=category, date=date)

            elif choice == '2':
                tracker.view_all_expenses()

            elif choice == '3':
                cat = input("Enter category: ")
                tracker.view_by_category(cat)

            elif choice == '4':
                month = input("Enter month (YYYY-MM): ")
                tracker.view_by_month(month)

            elif choice == '5':
                threshold = float(input("Show expenses > $: "))
                tracker.filter_by_amount(threshold)

            elif choice == '6':
                categories = tracker.unique_categories()
                print("\nUnique Categories:")
                for c in categories:
                    print("-", c)

            elif choice == '7':
                start = input("Start date (YYYY-MM-DD): ")
                end = input("End date (YYYY-MM-DD): ")
                print("\nExpenses in date range:")
                for exp in tracker.expenses_in_date_range(start, end):
                    print(exp)

            elif choice == '8':
                print("Exiting Expense Tracker. Goodbye!")
                break

            else:
                print("Invalid choice.\n")

        except Exception as e:
            print(f"[Error] {e}\n")

if __name__ == "__main__":
    main()
