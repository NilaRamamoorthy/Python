class ProductFilterIterator:
    def __init__(self, products, threshold=1000):
        # Accepts a dictionary {product_name: price}
        self.items = list(products.items())
        self.threshold = threshold
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.items):
            name, price = self.items[self.index]
            self.index += 1
            if price > self.threshold:
                return name
        raise StopIteration
products = {
    'ItemA': 950,
    'ItemB': 1200,
    'ItemC': 2000,
    'ItemD': 500
}

print("Products above ₹1000:")
for prod in ProductFilterIterator(products, threshold=1000):
    print(prod)

# Output
# Products above ₹1000:
# ItemB
# ItemC
