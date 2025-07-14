# Inventory System for a Shop

# Initial inventory list
inventory = ["Soap", "Shampoo", "Toothpaste", "Brush", "Oil"]

# Display current inventory
print("Current Inventory:")
for item in inventory:
    print("-", item)

# Add a new product
inventory.append("Lotion")
print("\nAfter adding 'Lotion':", inventory)

# Update quantity (for this example, simulate by appending duplicate)
inventory.append("Soap")  # Suppose more stock of Soap arrived
print("\nAfter restocking 'Soap':", inventory)

# Check if a product exists
item_to_check = "Oil"
if item_to_check in inventory:
    print(f"\n {item_to_check} is available in the inventory.")

# Remove a sold-out item
inventory.remove("Toothpaste")
print("\nAfter removing 'Toothpaste':", inventory)

# Display all items again
print("\n Updated Inventory:")
for item in inventory:
    print("-", item)
