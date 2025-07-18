cart = {}

def add_to_cart(item, quantity):
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

def get_cart():
    return cart

def clear_cart():
    cart.clear()
