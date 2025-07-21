sales = []  # List of tuples: (product, buyer, qty, time)
products = {
    "P001": {"name": "Keyboard", "price": 1000, "stock": 50},
    "P002": {"name": "Mouse", "price": 500, "stock": 80},
    "P003": {"name": "Monitor", "price": 7000, "stock": 30}
}
buyers = set()

def apply_discount(price, qty):
    if qty >= 5:
        return price * 0.9  # 10% discount
    return price

def sell_product(code, buyer, qty, time):
    if code in products and products[code]["stock"] >= qty:
        price = products[code]["price"]
        total = apply_discount(price, qty) * qty
        products[code]["stock"] -= qty
        sales.append((code, buyer, qty, time))
        buyers.add(buyer)
        print(f"Sold {qty} x {products[code]['name']} to {buyer} at ₹{total:.2f}")
    else:
        print("Product not available or insufficient stock.")
