from budget_planner.income import add_income
from budget_planner.expense import add_expense
from budget_planner.summary import show_summary

def main():
    while True:
        print("\nBudget Planner")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            source = input("Enter income source: ")
            amount = float(input("Enter amount: "))
            add_income(source, amount)
        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            add_expense(category, amount)
        elif choice == "3":
            show_summary()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
