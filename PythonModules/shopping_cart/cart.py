cart = []

def add_to_cart(item):
    cart.append(item)

def remove_from_cart(item):
    cart.remove(item)

def view_cart():
    return cart
