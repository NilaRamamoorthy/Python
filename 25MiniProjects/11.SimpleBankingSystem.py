# Simple Banking System

balance = 0
transactions = []

# Function to deposit amount
def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited ₹{amount}")
    print(f"₹{amount} deposited. New balance: ₹{balance}")

# Function to withdraw amount
def withdraw(amount):
    global balance
    if amount > balance:
        print(" Insufficient balance.")
    else:
        balance -= amount
        transactions.append(f"Withdrew ₹{amount}")
        print(f"₹{amount} withdrawn. New balance: ₹{balance}")

# Function to check balance
def check_balance():
    print(f"Current Balance: ₹{balance}")

# Function to print transaction history
def show_history():
    if not transactions:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for t in transactions:
            print("-", t)

# Main menu loop
def banking_system():
    while True:
        print("\n--- BANK MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: ₹"))
                deposit(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: ₹"))
                withdraw(amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            check_balance()
        elif choice == "4":
            show_history()
        elif choice == "5":
            print("👋 Exiting Banking System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the banking app
banking_system()
