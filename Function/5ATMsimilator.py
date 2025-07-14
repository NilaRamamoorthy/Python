# ATM Simulator

balance = 10000  # Initial balance
pin = "1234"     # Default PIN

def atm():
    global balance, pin

    def validate_pin():
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == pin:
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts left: {attempts}")
        return False

    def deposit():
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            global balance
            balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{balance}")
        else:
            print("Invalid amount.")

    def withdraw():
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            global balance
            balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{balance}")
        else:
            print("Invalid or insufficient funds.")

    def check_balance():
        print(f"Current Balance: ₹{balance}")

    def change_pin():
        # Placeholder
        pass

    if validate_pin():
        while True:
            print("\n--- ATM Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                deposit()
            elif choice == "2":
                withdraw()
            elif choice == "3":
                check_balance()
            elif choice == "4":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice.")
    else:
        print("ATM access denied.")

# Run the ATM
atm()
