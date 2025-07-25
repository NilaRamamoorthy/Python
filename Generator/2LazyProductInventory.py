def product_inventory(products, in_stock=True):
    """Generator filtering products conditionally."""
    return (prod for prod in products if prod.get("stock", 0) > 0) if in_stock else iter(products)

def paginate_generator(gen, page_size=5):
    """Yield pages (lists) from a generator."""
    while True:
        page = list(itertools.islice(gen, page_size))
        if not page:
            break
        yield page

# Mock data:
inventory = [
    {"id": i, "name": f"Product_{i}", "stock": (i % 7)*2}
    for i in range(1, 31)
]

filtered = product_inventory(inventory)
print("Inventory viewer (pages of 5, skipping out-of-stock):")
for page in paginate_generator(filtered, page_size=5):
    print(page)
