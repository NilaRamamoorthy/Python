products = {"pen": 10, "notebook": 50, "eraser": 5, "bag": 200}
cart = [input("Enter item: ") for _ in range(3)]
total = sum(products.get(item.lower(), 0) for item in cart)
print(f"Total Bill: ₹{total}")