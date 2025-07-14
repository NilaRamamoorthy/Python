# Grocery Cart System

# Start with an empty cart
cart = []

# Add items using append and extend
cart.append("Milk")
cart.append("Bread")
cart.extend(["Eggs", "Butter", "Juice"])

# Display all items
print("🛒 Your Cart Items:")
for item in cart:
    print("-", item)

# Remove an item
cart.remove("Eggs")  # Removes first occurrence of "Eggs"
print("\nAfter removing 'Eggs':", cart)

# Pop last item
cart.pop()
print("\nAfter popping last item:", cart)

# Show total count
print("\nTotal items in cart:", len(cart))

# Check for duplicates
cart.append("Milk")
if cart.count("Milk") > 1:
    print("Note: 'Milk' is added more than once.")

# Show first 3 items using slicing
print("\nFirst 3 items in cart:", cart[:3])
