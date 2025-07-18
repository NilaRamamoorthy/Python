import json

BUDGET_FILE = "budget_planner/data.json"

def load_data():
    try:
        with open(BUDGET_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": [], "expenses": []}

def save_data(data):
    with open(BUDGET_FILE, "w") as file:
        json.dump(data, file, indent=4)
