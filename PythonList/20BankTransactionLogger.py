# Bank Transaction Logger

transactions = []  # List to store all transaction amounts

# Add some sample transactions (positive for deposit, negative for withdrawal)
transactions.extend([+5000, -1200, +3000, -800])

# Add a new transaction
amount = float(input("Enter transaction amount (positive for deposit, negative for withdrawal): "))
transactions.append(amount)

# Remove incorrect transaction
remove_txn = float(input("Enter a transaction to remove (if entered wrongly): "))
if remove_txn in transactions:
    transactions.remove(remove_txn)
else:
    print("Transaction not found.")

# Show last 3 transactions
print("\nLast 3 Transactions:")
for txn in transactions[-3:]:
    print("Deposit" if txn > 0 else "Withdrawal", ":", abs(txn))

# Show current balance
balance = sum(transactions)
print(f"\nCurrent Balance: ₹{balance:.2f}")
