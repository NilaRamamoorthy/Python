from budget.planner import set_budget
from budget.tracker import add_expense
from budget.report import generate_report

def main():
    print("Budget Planning App")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. Generate Monthly Report")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter budget amount: "))
        set_budget(amount, category)
    elif choice == "2":
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))
        note = input("Add a note (optional): ")
        add_expense(category, amount, note)
    elif choice == "3":
        month = input("Enter month (YYYY-MM): ")
        generate_report(month)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
