from expense_ops import add_expense, show_expenses, expenses, categories
from balance_ops import calculate_balances, show_balances

# Add sample expenses
add_expense(1200, "Alice", ["Alice", "Bob", "Charlie"], "Groceries")
add_expense(900, "Bob", ["Bob", "Charlie"], "Electricity")
add_expense(600, "Charlie", ["Alice", "Charlie"], "Internet")

print("All Expenses:")
show_expenses()

balances = calculate_balances(expenses)
show_balances(balances)

print("\nCategories Used:", categories)
