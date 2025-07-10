#1. Billing System
total_bill = 0

# Function to add items with name and price using *args
def add_items(*item_details):
    global total_bill
    print("\nItems Added:")
    for item in item_details:
        name, price = item  # tuple unpacking
        print(f"- {name}: ₹{price}")
        total_bill += price
    return total_bill

# Function to calculate total
def calculate_total():
    global total_bill
    return total_bill

# Function to apply discount
def apply_discount(discount_percent):
    global total_bill
    discount_amount = total_bill * (discount_percent / 100)
    final_amount = total_bill - discount_amount
    return final_amount

# Sample usage
add_items(("Milk", 45), ("Bread", 30), ("Eggs", 60))       # Item name + price
print(f"\nTotal before discount: ₹{calculate_total()}")

final_price = apply_discount(5)                            # Apply 5% discount
print(f"Final Price after 5% Discount: ₹{final_price}")
