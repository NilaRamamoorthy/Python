# Initial cart
cart = {
    "apple": {"quantity": 2, "price": 30},
    "milk": {"quantity": 1, "price": 50}
}

# 1. Add new item
cart["bread"] = {"quantity": 3, "price": 25}

# 2. Update quantity and price
cart["apple"]["quantity"] = 4
cart["milk"]["price"] = 55

# 3. Remove item
cart.pop("bread", None)

# 4. Calculate total bill
total = sum(item["quantity"] * item["price"] for item in cart.values())
print(f"\n Total Bill: ₹{total}")

# 5. Remove out-of-stock items
for item in list(cart.keys()):
    if cart[item]["quantity"] == 0:
        cart.pop(item)

# 6. Show highest value item
highest = max(cart.items(), key=lambda x: x[1]["quantity"] * x[1]["price"])
print(f"\n Highest Value Item: {highest[0]} (₹{highest[1]['quantity'] * highest[1]['price']})")

# 7. Bill Summary
print("\n Cart Summary:")
for item, info in cart.items():
    item_total = info["quantity"] * info["price"]
    print(f"{item.title()}: {info['quantity']} x ₹{info['price']} = ₹{item_total}")

# 8. Check if item exists
print("\nIs 'milk' in cart?", "milk" in cart)
print("Is 'bread' in cart?", "bread" in cart)
