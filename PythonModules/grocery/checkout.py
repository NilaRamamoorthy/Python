import json
from datetime import datetime
from grocery.cart import get_cart
from grocery.items import get_price
import random

def generate_bill():
    cart = get_cart()
    total = 0
    bill_id = f"BILL{random.randint(1000,9999)}"
    print(f"\nBill ID: {bill_id}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("------ Grocery Bill ------")
    for item, qty in cart.items():
        price = get_price(item)
        if price is not None:
            subtotal = price * qty
            print(f"{item.capitalize()} x {qty} = ₹{subtotal}")
            total += subtotal
    print(f"Total: ₹{total}")

    bill_data = {
        "bill_id": bill_id,
        "timestamp": datetime.now().isoformat(),
        "total": total,
        "items": cart
    }

    with open(f"{bill_id}.json", "w") as f:
        json.dump(bill_data, f, indent=2)

    print("Bill saved as JSON.\n")
