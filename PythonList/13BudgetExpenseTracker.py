# Budget Expense Tracker

# Initial expenses list
expenses = [1500, 2200, 800, 1200]

# Add a new expense
new_expense = float(input("Enter a new expense: "))
expenses.append(new_expense)

# Update an existing expense
index_to_update = int(input("Enter the index of the expense to update (0-based): "))
if 0 <= index_to_update < len(expenses):
    updated_value = float(input("Enter the new value: "))
    expenses[index_to_update] = updated_value
else:
    print("Invalid index.")

# Show last 3 expenses using slicing
print("\nLast 3 Expenses:", expenses[-3:])

# Remove a wrong entry
wrong_value = float(input("Enter an expense value to remove (if wrong): "))
if wrong_value in expenses:
    expenses.remove(wrong_value)
else:
    print("Expense value not found.")

# Final expense report
print("\nFinal Expenses List:", expenses)
print("Total Spent:", sum(expenses))
