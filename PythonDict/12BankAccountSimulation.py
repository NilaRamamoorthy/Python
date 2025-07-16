# Initial account data
accounts = {
    1001: {"name": "Alice", "balance": 5000},
    1002: {"name": "Bob", "balance": 3000},
    1003: {"name": "Charlie", "balance": 800}
}

# 1. Deposit
def deposit(account_number, amount):
    account = accounts.get(account_number)
    if account:
        account["balance"] += amount
        print(f"Deposited ₹{amount} to {account['name']}'s account.")
    else:
        print("Account not found.")

# 2. Withdraw
def withdraw(account_number, amount):
    account = accounts.get(account_number)
    if account:
        if account["balance"] >= amount:
            account["balance"] -= amount
            print(f"Withdrew ₹{amount} from {account['name']}'s account.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

# Perform operations
deposit(1001, 1000)
withdraw(1002, 500)
withdraw(1003, 1000)  # should fail

# 3. Low balance alert
low_balance_accounts = {acc: data for acc, data in accounts.items() if data["balance"] < 1000}

print("\nAccounts with low balance (< ₹1000):")
for acc_no, data in low_balance_accounts.items():
    print(f"{acc_no} - {data['name']} (₹{data['balance']})")
