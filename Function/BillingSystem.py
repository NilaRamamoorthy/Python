#1. Billing System
# Global total bill
total_bill = 0

# Function to add item prices
def add_items(*prices):
    global total_bill
    for price in prices:
        total_bill += price
    return total_bill

# Function to apply discount
def apply_discount(percent):
    global total_bill
    discount_amount = total_bill * (percent / 100)
    final_total = total_bill - discount_amount
    return final_total

# --- Example Usage ---
print("Adding items to the bill...")
add_items(100, 250, 150)  
print("Total before discount: ₹", total_bill)

final_amount = apply_discount(10)  
print("Total after 10% discount: ₹", final_amount)
