# Global list to store items
cart = []

# Add item using *args (name, price)
def add_item(*args):
    global cart
    for item in args:
        name, price = item
        cart.append((name, price))
        print(f"Added: {name} - ₹{price}")

# Calculate total price
def get_total():
    return sum(price for _, price in cart)

# Apply discount using lambda
def apply_discount(percent):
    total = get_total()
    discount = lambda total: total - (total * percent / 100)
    return discount(total)

add_item(("Milk", 50), ("Bread", 40), ("Eggs", 60))

print("\nCart Summary:")
for item, price in cart:
    print(f"- {item}: ₹{price}")

total = get_total()
print(f"\nTotal: ₹{total}")

final_total = apply_discount(10)
print(f"Total after 10% discount: ₹{final_total}")
