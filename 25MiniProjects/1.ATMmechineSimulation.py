# ATM Machine Simulation

balance = 5000
pin = "1234"
transaction_history = []

# Function to check PIN
def login():
    attempts = 3
    while attempts > 0:
        user_pin = input("Enter your 4-digit PIN: ")
        if user_pin == pin:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
    print("Account locked due to too many failed attempts.")
    return False

# Function to show menu
def show_menu():
    print("\n--- ATM MENU ---")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

# Function to deposit money
def deposit():
    global balance
    amount = input("Enter amount to deposit: ₹")
    if amount.isdigit():
        amount = int(amount)
        balance += amount
        transaction_history.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited successfully.")
    else:
        print("Invalid amount.")

# Function to withdraw money
def withdraw():
    global balance
    amount = input("Enter amount to withdraw: ₹")
    if amount.isdigit():
        amount = int(amount)
        if amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdrew ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid amount.")

# Main program
if login():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            print(f"Current Balance: ₹{balance}")
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("\nTransaction History:")
            for t in transaction_history:
                print("-", t)
            if not transaction_history:
                print("No transactions yet.")
        elif choice == "5":
            print("Thank you for using ZAHIRX ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
