# main.py

from cart_ops import add_to_cart, remove_from_cart, checkout
from product_data import products

print("Available Products:")
for pid, (name, price, stock) in products.items():
    print(f"{pid} → {name} | ₹{price} | Stock: {stock}")

# Sample operations
add_to_cart(101, 1)
add_to_cart(102, 2)
remove_from_cart(102)
add_to_cart(103, 3)

checkout()
