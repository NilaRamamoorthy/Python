from .stock import update_stock  # Relative import

def sell_item(item, quantity):
    print(f"Selling {quantity} units of {item}.")
    update_stock(item, -quantity)
