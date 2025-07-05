items = input("Enter grocery items separated by commas: ").split(",")
for i, item in enumerate(items, start=1):
    print(f"{i}. {item.strip()}")
