# Custom Exception
class InsufficientFundsError(Exception):
    pass

class ATM:
    def __init__(self, balance=10000):
        self.balance = balance

    def deposit(self, amount):
        try:
            assert amount > 0, "Deposit amount must be positive"
            self.balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
        except AssertionError as ae:
            print(f"❌ {ae}")

    def withdraw(self, amount):
        try:
            assert amount > 0, "Withdrawal amount must be positive"
            if amount > self.balance:
                raise InsufficientFundsError("❌ Not enough balance.")
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
        except AssertionError as ae:
            print(ae)
        except InsufficientFundsError as ie:
            print(ie)

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance:.2f}")

def run_atm():
    atm = ATM()
    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        try:
            choice = int(input("Select an option (1-4): "))
            if choice == 1:
                try:
                    amount = float(input("Enter deposit amount: "))
                    atm.deposit(amount)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == 2:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    atm.withdraw(amount)
                except ValueError:
                    print("❌ Please enter a valid number.")
            elif choice == 3:
                atm.check_balance()
            elif choice == 4:
                print("👋 Thank you for using the ATM!")
                break
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 4.")

# Run the ATM Simulator
run_atm()
