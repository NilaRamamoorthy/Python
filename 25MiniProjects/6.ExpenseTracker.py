# Expense Tracker with Categories

expenses = []

# Function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))
        category = input("Enter category (e.g., food, travel, bills): ").strip().lower()
        expenses.append({"amount": amount, "category": category})
        print(f"₹{amount:.2f} added under '{category}' category.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

# Function to show all expenses
def show_expenses():
    if not expenses:
        print("📭 No expenses recorded yet.")
        return
    print("\n Expense List:")
    for idx, item in enumerate(expenses, start=1):
        print(f"{idx}. ₹{item['amount']:.2f} - {item['category'].title()}")

# Function to show total expenses
def total_expenses():
    total = sum(item['amount'] for item in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")

# Function to show category-wise totals
def category_totals():
    category_map = {}
    for item in expenses:
        cat = item['category']
        category_map[cat] = category_map.get(cat, 0) + item['amount']
    
    print("\nCategory-wise Totals:")
    for cat, amt in category_map.items():
        print(f"{cat.title()}: ₹{amt:.2f}")

# Main menu loop
def main():
    while True:
        print("\n--- EXPENSE TRACKER MENU ---")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Total Expenses")
        print("4. Category-wise Totals")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_totals()
        elif choice == "5":
            print("Exiting Expense Tracker. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
main()
