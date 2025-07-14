# Online Order History Tracker

# Initial list of orders
orders = ["Shoes", "T-shirt", "Book", "Headphones", "Watch"]

# Add a new order
new_order = input("Enter a new order item to add: ").strip().title()
orders.append(new_order)

# Remove a canceled order
cancel_order = input("Enter an item to cancel from orders: ").strip().title()
if cancel_order in orders:
    orders.remove(cancel_order)
else:
    print("Item not found in order history.")

# Show last 5 orders
print("\nYour Last 5 Orders:")
for item in orders[-5:]:
    print("-", item)

# Show total number of orders
print(f"\nTotal Orders: {len(orders)}")
