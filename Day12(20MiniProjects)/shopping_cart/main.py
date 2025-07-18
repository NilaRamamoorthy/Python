# main.py

from cart_utils import add_to_cart, remove_from_cart, update_quantity, display_cart

add_to_cart(101, "Laptop", 55000, "Electronics", 1)
add_to_cart(102, "Shoes", 2000, "Footwear", 2)
add_to_cart(103, "Laptop Bag", 1500, "Accessories", 1)
add_to_cart(102, "Shoes", 2000, "Footwear", 1)  # Duplicate item ID, will increase quantity

update_quantity(103, 3)
remove_from_cart(101)

display_cart()
