from expensesplitter.split import split_expenses

def display_report():
    balances = split_expenses()
    print("\n--- Expense Split Report ---")
    for name, balance in balances.items():
        if balance > 0:
            print(f"{name} should receive ₹{balance}")
        elif balance < 0:
            print(f"{name} should pay ₹{-balance}")
        else:
            print(f"{name} is settled up.")
