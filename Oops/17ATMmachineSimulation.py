# ATM Machine Simulation

class Account:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, *args):
        # Overloading behavior: single arg = amount, two args = pin + amount
        if len(args) == 1:
            amount = args[0]
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{amount} withdrawn.")
            else:
                print("Insufficient balance.")
        elif len(args) == 2:
            pin, amount = args
            if not self.verify_pin(pin):
                print("Invalid PIN.")
                return
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{amount} withdrawn after PIN verification.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdraw format.")

    def get_balance(self, pin):
        if self.verify_pin(pin):
            return self.__balance
        else:
            print("Invalid PIN.")
            return None


class ATM:
    @staticmethod
    def show_menu():
        print("\n1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Exit")


# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    acc = Account("Neha", "1234", 1000)

    ATM.show_menu()

    # Deposit money
    acc.deposit(500)  # Balance: 1500

    # Withdraw without PIN (single argument)
    acc.withdraw(200)  # Balance: 1300

    # Withdraw with PIN (two arguments)
    acc.withdraw("1234", 300)  # Balance: 1000

    # Check balance
    print("Balance:", acc.get_balance("1234"))  # Output: 1000

    # Wrong PIN
    acc.withdraw("0000", 100)  # Invalid PIN
    print("Balance:", acc.get_balance("0000"))  # Invalid PIN
