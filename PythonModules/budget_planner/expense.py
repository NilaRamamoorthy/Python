from budget_planner.data import load_data, save_data

def add_expense(category, amount):
    data = load_data()
    data["expenses"].append({"category": category, "amount": amount})
    save_data(data)
    print(f"Expense on '{category}' added.")
