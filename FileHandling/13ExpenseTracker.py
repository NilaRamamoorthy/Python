import csv
import os
from datetime import datetime

def get_filename():
    month = datetime.now().strftime("%Y-%m")
    return f"expenses_{month}.csv"

def add_expense(category, amount):
    filename = get_filename()
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount])
    print("Expense recorded.")

def view_summary():
    filename = get_filename()
    if not os.path.exists(filename):
        print("No expense file found for this month.")
        return
    total = 0
    print(f"\nSummary for {filename}:")
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Date']} - {row['Category']} - ₹{row['Amount']}")
            total += float(row['Amount'])
    print(f"Total Spent: ₹{total}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            category = input("Enter category (e.g., Food, Travel): ")
            try:
                amount = float(input("Enter amount: ₹"))
                add_expense(category, amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()
