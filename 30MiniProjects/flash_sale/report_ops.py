def generate_sales_report(sales, products):
    print("\n--- Sales Report ---")
    summary = {}
    for code, buyer, qty, _ in sales:
        summary[code] = summary.get(code, 0) + qty
    for code, qty in summary.items():
        print(f"{products[code]['name']}: {qty} units sold")
