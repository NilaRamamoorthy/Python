class CartIterator:
    def __init__(self, cart_items):
        self._items = cart_items
        self._it = iter(self._items)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._it)
        except StopIteration:
            raise StopIteration("Cart is empty or all items have been fetched")

# Usage:
cart = ["apple", "banana", "cherry"]
it = CartIterator(cart)
print("Cart items:", end=" ")
try:
    while True:
        print(next(it), end=" ")
except StopIteration as e:
    print(f"\n{e}")
# Cart items: apple banana cherry 
# Cart is empty or all items have been fetched
