import json
from collections import defaultdict
from validator import validate_date, validate_amount

FILE = "expenses.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format!")
        return
    category = input("Category: ")
    amount = input("Amount: ")
    if not validate_amount(amount):
        print("Invalid amount!")
        return
    record = [date, category, float(amount)]
    data = load_data()
    data.append(record)
    save_data(data)
    print("Expense added!")

def view_summary():
    data = load_data()
    summary = defaultdict(float)
    for entry in data:
        summary[entry[1]] += entry[2]
    print("\nCategory-wise Summary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

def view_unique_categories():
    data = load_data()
    categories = {entry[1] for entry in data}
    print("\nUnique Categories:")
    for cat in categories:
        print(f"- {cat}")

def monthly_total():
    month = input("Enter month (YYYY-MM): ")
    total = 0
    data = load_data()
    for entry in data:
        if entry[0].startswith(month):
            total += entry[2]
    print(f"\nTotal expenses in {month}: ₹{total:.2f}")
