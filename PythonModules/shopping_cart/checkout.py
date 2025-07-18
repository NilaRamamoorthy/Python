from .cart import view_cart

def total_price():
    return sum(item["price"] for item in view_cart())
