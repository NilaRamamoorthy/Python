from budget_planner.data import load_data

def show_summary():
    data = load_data()
    total_income = sum(item["amount"] for item in data["income"])
    total_expense = sum(item["amount"] for item in data["expenses"])
    balance = total_income - total_expense

    print("\n--- Budget Summary ---")
    print(f"Total Income: ₹{total_income}")
    print(f"Total Expense: ₹{total_expense}")
    print(f"Balance: ₹{balance}")
