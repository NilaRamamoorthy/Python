from budget_planner.data import load_data, save_data

def add_income(source, amount):
    data = load_data()
    data["income"].append({"source": source, "amount": amount})
    save_data(data)
    print(f"Income from '{source}' added.")
