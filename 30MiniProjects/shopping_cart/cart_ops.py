# cart_ops.py

from typing import List, Tuple
from product_data import products
from discount import apply_discount

# Cart is a list of (product_id, quantity)
cart: List[Tuple[int, int]] = []

def add_to_cart(product_id: int, quantity: int):
    if product_id not in products:
        print("Invalid product ID.")
        return
    name, price, stock = products[product_id]
    if quantity > stock:
        print(f"Only {stock} items in stock.")
        return
    cart.append((product_id, quantity))
    products[product_id] = (name, price, stock - quantity)
    print(f"{quantity} x {name} added to cart.")

def remove_from_cart(product_id: int):
    global cart
    for item in cart:
        if item[0] == product_id:
            cart.remove(item)
            name, price, stock = products[product_id]
            products[product_id] = (name, price, stock + item[1])
            print(f"Removed {item[1]} x {name} from cart.")
            return
    print("Item not found in cart.")

def checkout():
    print("\n--- Bill ---")
    total = 0
    unique_items = set()
    for pid, qty in cart:
        name, price, _ = products[pid]
        line_total = price * qty
        total += line_total
        unique_items.add(pid)
        print(f"{name} x {qty} = ₹{line_total}")
    discounted_total = apply_discount(total)
    print(f"\nSubtotal: ₹{total}")
    print(f"Discounted Total: ₹{discounted_total:.2f}")
    print(f"Unique Items Bought: {len(unique_items)}")
    cart.clear()
