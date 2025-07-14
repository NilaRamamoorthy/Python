total = 0
items = []

def add_item(*args):
    global total
    for item in args:
        items.append(item)
        total += item[1]

def get_total():
    return total

def apply_discount(percent):
    discount = lambda t, p: t - (t * p / 100)
    return discount(total, percent)

# Example
add_item(("Pen", 10), ("Book", 50), ("Pencil", 5))
print("Items:", items)
print("Total:", get_total())
print("After 10% Discount:", apply_discount(10))
