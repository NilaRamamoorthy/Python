import os
from datetime import datetime

INVOICE_FOLDER = "invoices"

def generate_invoice(customer_name, items):
    if not os.path.exists(INVOICE_FOLDER):
        os.makedirs(INVOICE_FOLDER)

    invoice_id = len(os.listdir(INVOICE_FOLDER)) + 1
    filename = f"invoice_{invoice_id}.txt"
    filepath = os.path.join(INVOICE_FOLDER, filename)

    total = sum(price for item, price in items)

    with open(filepath, "w") as file:
        file.write(f"Invoice ID: {invoice_id}\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write("-" * 30 + "\n")
        for item, price in items:
            file.write(f"{item:20} ₹{price:.2f}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total: ₹{total:.2f}\n")

    print(f"Invoice generated: {filepath}")

def main():
    customer_name = input("Enter customer name: ")
    items = []
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item.lower() == "done":
            break
        try:
            price = float(input("Enter item price: "))
            items.append((item, price))
        except ValueError:
            print("Invalid price. Try again.")
    if items:
        generate_invoice(customer_name, items)
    else:
        print("No items entered. Invoice not generated.")

main()
