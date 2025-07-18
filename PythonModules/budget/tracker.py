import json
from datetime import datetime

def add_expense(category, amount, note=""):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "amount": amount,
        "note": note
    }

    try:
        with open("budget/expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

    expenses.append(entry)

    with open("budget/expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

    print(f"Expense of ₹{amount} added under {category}.")
