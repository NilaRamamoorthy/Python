# Global list to store expenses
expenses = []

# Function to add expenses using *args
def add_expenses(*args):
    global expenses
    for amount in args:
        expenses.append(amount)
    return expenses

# Function to apply GST using map
def apply_gst(expense_list, gst_percent=18):
    gst_multiplier = 1 + (gst_percent / 100)
    return list(map(lambda x: round(x * gst_multiplier, 2), expense_list))

# Function to calculate total
def get_total():
    return sum(expenses)

# Example Usage
add_expenses(100, 250, 400)
print("Original Expenses:", expenses)

gst_applied = apply_gst(expenses)
print("Expenses after 18% GST:", gst_applied)

print("Total Original Amount:", get_total())
print("Total with GST:", sum(gst_applied))
