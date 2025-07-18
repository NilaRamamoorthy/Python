# cart_utils.py

cart = {}  # { (item_id,): {"name": str, "price": float, "category": str, "quantity": int} }
categories = set()

def add_to_cart(item_id, name, price, category, quantity):
    key = (item_id,)
    if key in cart:
        cart[key]["quantity"] += quantity
    else:
        cart[key] = {
            "name": name,
            "price": price,
            "category": category,
            "quantity": quantity
        }
        categories.add(category)

def remove_from_cart(item_id):
    key = (item_id,)
    if key in cart:
        del cart[key]

def update_quantity(item_id, quantity):
    key = (item_id,)
    if key in cart:
        cart[key]["quantity"] = quantity

def calculate_total():
    return sum(item["price"] * item["quantity"] for item in cart.values())

def display_cart():
    print("\n🛒 Your Shopping Cart:")
    for key, item in cart.items():
        print(f"ID: {key[0]}, Name: {item['name']}, Qty: {item['quantity']}, Price: ₹{item['price']}, Category: {item['category']}")
    print(f"Total: ₹{calculate_total()}")
    print(f"Available Categories: {categories}")
