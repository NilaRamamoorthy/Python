def print_item(item):
    status = "✓" if item["bought"] else "✗"
    print(f"{item['item']} ({item['category']}) - Bought: {status}")

def print_grouped_items(items):
    grouped = {}
    for item in items:
        grouped.setdefault(item["category"], []).append(item)
    for category, items in grouped.items():
        print(f"\nCategory: {category}")
        for item in items:
            print_item(item)
