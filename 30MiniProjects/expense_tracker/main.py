from tracker import add_expense, view_summary, view_unique_categories, monthly_total

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense\n2. View Summary\n3. View Categories\n4. Monthly Total\n5. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            view_unique_categories()
        elif choice == "4":
            monthly_total()
        elif choice == "5":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
