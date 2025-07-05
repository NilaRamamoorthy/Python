# Shopping Cart

# Step 1: Ask for item names and prices
item1 = input("Enter the name of item 1: ")
price1 = float(input(f"Enter the price of {item1}: "))

item2 = input("Enter the name of item 2: ")
price2 = float(input(f"Enter the price of {item2}: "))

item3 = input("Enter the name of item 3: ")
price3 = float(input(f"Enter the price of {item3}: "))

# Step 2: Store items and prices in a dictionary
cart = {
    item1: price1,
    item2: price2,
    item3: price3
}

# Step 3: Calculate total amount
total = price1 + price2 + price3

# Step 4: Print items, prices, and total
print("\n--- Shopping Cart ---")
for item, price in cart.items():
    print(f"{item}: ₹{price:.2f}")

print(f"\nTotal Amount: ₹{total:.2f}")
