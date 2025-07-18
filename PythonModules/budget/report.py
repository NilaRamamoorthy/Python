import json
from collections import defaultdict

def generate_report(month):
    try:
        with open("budget/expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

    try:
        with open("budget/budget_data.json", "r") as f:
            budgets = json.load(f)
    except FileNotFoundError:
        budgets = []

    category_expense = defaultdict(float)
    for item in expenses:
        if item["date"].startswith(month):
            category_expense[item["category"]] += item["amount"]

    print(f"\nBudget Report for {month}:")
    for budget in budgets:
        if budget["date"] == month:
            cat = budget["category"]
            print(f"\nCategory: {cat}")
            print(f"  Budgeted: ₹{budget['budget']}")
            print(f"  Spent: ₹{category_expense[cat]}")
            balance = budget['budget'] - category_expense[cat]
            print(f"  Balance: ₹{balance}")
