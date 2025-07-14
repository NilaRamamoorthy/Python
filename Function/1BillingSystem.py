# Billing System

cart = []
total_bill = 0  # Global variable to maintain total

def add_items(*args):
    global total_bill
    for item in args:
        name, price = item
        cart.append((name, price))
        total_bill += price
    return cart

def apply_discount(percent):
    global total_bill
    discount = total_bill * (percent / 100)
    total_bill -= discount
    return total_bill

# Example usage
add_items(("Milk", 50), ("Bread", 30), ("Eggs", 60))
print("Cart Items:", cart)
print("Total before discount:", total_bill)

final_total = apply_discount(10)  # Apply 10% discount
print("Total after discount:", final_total)
