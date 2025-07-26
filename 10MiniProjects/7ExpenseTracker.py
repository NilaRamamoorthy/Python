import csv
import datetime
import os
import matplotlib.pyplot as plt
from collections import defaultdict

DATA_FILE = 'expenses.csv'

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_data()
        self.budget = None

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            self.expenses = list(reader)

    def save_data(self):
        with open(DATA_FILE, 'w', newline='') as f:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)

    def add_expense(self):
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if not date:
            date = datetime.date.today().isoformat()
        category = input("Enter category (e.g. Food, Rent): ")
        amount = input("Enter amount: ")
        description = input("Enter description: ")

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount.")
            return

        self.expenses.append({
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        })
        self.save_data()
        print("Expense added.")

    def set_budget(self):
        budget = input("Enter monthly budget amount: ")
        try:
            self.budget = float(budget)
            print(f"Monthly budget set to {self.budget}")
        except ValueError:
            print("Invalid budget.")

    def monthly_report(self):
        month = input("Enter month to report (YYYY-MM) or leave blank for current month: ")
        if not month:
            month = datetime.date.today().strftime('%Y-%m')

        total = 0
        category_totals = defaultdict(float)
        for exp in self.expenses:
            if exp['date'].startswith(month):
                amount = float(exp['amount'])
                category_totals[exp['category']] += amount
                total += amount

        print(f"Report for {month}:")
        print(f"Total expenses: {total:.2f}")
        for cat, amt in category_totals.items():
            print(f"  {cat}: {amt:.2f}")

        if self.budget:
            diff = self.budget - total
            if diff >= 0:
                print(f"You are under budget by {diff:.2f}")
            else:
                print(f"You are over budget by {-diff:.2f}")

        # Plot chart
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        if categories:
            plt.figure(figsize=(6,6))
            plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.title(f'Expenses Breakdown for {month}')
            plt.show()
        else:
            print("No expenses for this month.")

    def export_to_csv(self):
        filename = input("Enter filename to export (e.g. export.csv): ")
        with open(filename, 'w', newline='') as f:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)
        print(f"Data exported to {filename}")

def main():
    tracker = ExpenseTracker()
    print("Expense Tracker")

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Set Monthly Budget")
        print("3. Monthly Report")
        print("4. Export Data to CSV")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.set_budget()
        elif choice == '3':
            tracker.monthly_report()
        elif choice == '4':
            tracker.export_to_csv()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
