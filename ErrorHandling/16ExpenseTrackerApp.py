# Custom exception
class InvalidCategoryError(Exception):
    pass

# Predefined valid categories
valid_categories = {"food", "transport", "entertainment", "utilities", "others"}

# Function to track expenses
def expense_tracker():
    print("💰 Expense Tracker")
    expenses = {}
    total = 0

    try:
        while True:
            category = input("Enter expense category (food, transport, entertainment, utilities, others or 'q' to quit): ").lower()
            if category == 'q':
                break

            if category not in valid_categories:
                raise InvalidCategoryError(f"'{category}' is not a valid category.")

            amount_input = input(f"Enter amount spent on {category}: ")
            if not amount_input.replace('.', '', 1).isdigit():
                raise ValueError("Amount must be a valid number.")

            amount = float(amount_input)
            expenses[category] = expenses.get(category, 0) + amount
            total += amount
            print(f"✅ Added ₹{amount:.2f} under '{category}'")

    except InvalidCategoryError as ice:
        print(f"⚠️ {ice}")
    except ValueError as ve:
        print(f"⚠️ Invalid input: {ve}")
    finally:
        print("\n📊 Final Expense Summary:")
        for cat, amt in expenses.items():
            print(f"- {cat.title()}: ₹{amt:.2f}")
        print(f"\n💼 Total Expenses: ₹{total:.2f}")
        print("📝 Expense tracking complete.\n")

# Run the tracker
expense_tracker()
