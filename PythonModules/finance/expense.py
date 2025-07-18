import json
from datetime import datetime

expense_file = "expense.json"

def add_expense(amount, category):
    entry = {
        "amount": amount,
        "category": category,
        "date": datetime.now().isoformat()
    }
    try:
        with open(expense_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    data.append(entry)

    with open(expense_file, "w") as f:
        json.dump(data, f, indent=2)

def get_total_expense():
    try:
        with open(expense_file, "r") as f:
            data = json.load(f)
        return sum(item["amount"] for item in data)
    except FileNotFoundError:
        return 0
