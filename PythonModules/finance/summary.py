from income import add_income, get_total_income
from expense import add_expense, get_total_expense

def show_summary():
    income = get_total_income()
    expense = get_total_expense()
    savings = income - expense

    print("\n--- Finance Summary ---")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Total Savings: ₹{savings}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. Show Summary\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amt = float(input("Enter income amount: ₹"))
            src = input("Enter income source: ")
            add_income(amt, src)
        elif choice == "2":
            amt = float(input("Enter expense amount: ₹"))
            cat = input("Enter expense category: ")
            add_expense(amt, cat)
        elif choice == "3":
            show_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
