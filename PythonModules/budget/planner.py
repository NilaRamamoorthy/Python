import json
from datetime import datetime

def set_budget(amount, category):
    data = {
        "date": datetime.now().strftime("%Y-%m"),
        "category": category,
        "budget": amount
    }

    try:
        with open("budget/budget_data.json", "r") as f:
            budgets = json.load(f)
    except FileNotFoundError:
        budgets = []

    budgets.append(data)

    with open("budget/budget_data.json", "w") as f:
        json.dump(budgets, f, indent=4)

    print(f"Budget of ₹{amount} set for {category}.")
