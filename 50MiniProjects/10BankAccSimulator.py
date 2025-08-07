import datetime
import pickle
from functools import wraps

# Decorator to audit operations
def audit(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        # log audit entry
        ts = datetime.datetime.now().isoformat()
        self.transactions.append({'type': func.__name__, 'amount': args[0], 'timestamp': ts})
        return result
    return wrapper

class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []  # list of dicts

    @audit
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self._apply_interest_if_needed()
        return self.balance

    @audit
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.balance:
            raise InsufficientFunds("Not enough balance")
        self.balance -= amount
        return self.balance

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
        # record transfer event manually:
        ts = datetime.datetime.now().isoformat()
        self.transactions.append({'type': 'transfer_out', 'amount': amount, 'timestamp': ts})
        other.transactions.append({'type': 'transfer_in', 'amount': amount, 'timestamp': ts})

    def _apply_interest_if_needed(self):
        # apply simple interest if balance > 1000
        if self.balance > 1000:
            interest = self.balance * 0.01  # 1%
            self.balance += interest
            ts = datetime.datetime.now().isoformat()
            self.transactions.append({'type': 'interest', 'amount': interest, 'timestamp': ts})

    def show_transactions(self):
        print(f"Transaction history for {self.owner}:")
        for t in self.transactions:
            print(f"{t['timestamp']}: {t['type']} → {t['amount']}")

    def gen_transactions(self, tx_type):
        # generator for filtering transactions
        for t in self.transactions:
            if t['type'] == tx_type:
                yield t

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Sample usage:
if __name__ == "__main__":
    acct1 = BankAccount("Alice", 500)
    acct2 = BankAccount("Bob", 1200)

    acct1.deposit(600)     # triggers interest since balance > 1000
    acct1.withdraw(50)
    acct1.transfer(acct2, 200)

    acct1.show_transactions()
    print("Only deposits:")
    for tx in acct1.gen_transactions('deposit'):
        print(tx)

    acct1.save("alice_acct.pkl")
    acct2.save("bob_acct.pkl")

    # reload
    a2 = BankAccount.load("alice_acct.pkl")
    print("Reloaded balance:", a2.balance)
