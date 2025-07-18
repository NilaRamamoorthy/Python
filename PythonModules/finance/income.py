import json
from datetime import datetime

income_file = "income.json"

def add_income(amount, source):
    entry = {
        "amount": amount,
        "source": source,
        "date": datetime.now().isoformat()
    }
    try:
        with open(income_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    data.append(entry)

    with open(income_file, "w") as f:
        json.dump(data, f, indent=2)

def get_total_income():
    try:
        with open(income_file, "r") as f:
            data = json.load(f)
        return sum(item["amount"] for item in data)
    except FileNotFoundError:
        return 0
