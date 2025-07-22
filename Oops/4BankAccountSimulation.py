from datetime import datetime

# Base Account class
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Account: {self.account_number}, Holder: {self.holder_name}, Balance: ₹{self.__balance:.2f}"

# SavingsAccount with limit
class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)

    def withdraw(self, amount):
        if amount > 25000:
            print("SavingsAccount limit: Cannot withdraw more than ₹25,000.")
            return False
        return super().withdraw(amount)

# CurrentAccount with different rule
class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)

    def withdraw(self, amount):
        if amount > 100000:
            print("CurrentAccount limit: Cannot withdraw more than ₹1,00,000.")
            return False
        return super().withdraw(amount)

# Transaction record class
class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_acc = from_account.account_number
        self.to_acc = to_account.account_number
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y %H:%M:%S')}: ₹{self.amount} transferred from {self.from_acc} to {self.to_acc}"
# Create accounts
acc1 = SavingsAccount("S001", "Nila", 50000)
acc2 = CurrentAccount("C001", "Ravi", 200000)

# Deposit and Withdraw
acc1.deposit(5000)
acc1.withdraw(20000)        # OK
acc1.withdraw(30000)        # Limit check

# Transfer
transactions = []
if acc2.transfer(acc1, 25000):
    transactions.append(Transaction(acc2, acc1, 25000))

# Show details
print(acc1)
print(acc2)

# Show transaction history
print("\nTransaction History:")
for t in transactions:
    print(t)
