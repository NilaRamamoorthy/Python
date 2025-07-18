from restaurant.menu import MENU
from restaurant.offers import apply_discount, apply_tax

def generate_bill(order_id, order):
    print(f"\nOrder ID: {order_id}")
    print("--- Bill Summary ---")
    total = 0
    for item, qty in order.items():
        price = MENU[item] * qty
        total += price
        print(f"{item} x {qty} = ₹{price}")
    
    print(f"Subtotal: ₹{total}")
    total = apply_discount(total)
    total = apply_tax(total)
    print(f"Total with tax: ₹{round(total, 2)}")
