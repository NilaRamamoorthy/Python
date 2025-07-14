
# 5. Product Inventory System
products = [
    (1, 'Pen', 10.0, True),
    (2, 'Notebook', 50.0, True),
    (3, 'Pencil', 5.0, False)
]
total_value = sum(price for _, _, price, _ in products)
print("Total Inventory Value:", total_value)
in_stock = [p for p in products if p[3]]
sorted_products = sorted(products, key=lambda x: x[2])
for pid, name, price, stock in sorted_products:
    print(f"{name} - Rs.{price}")

