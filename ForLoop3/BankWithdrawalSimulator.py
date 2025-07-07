# 6. Bank Withdrawal Simulator
balance = float(input("Enter current balance: "))
withdraw = float(input("Enter amount to withdraw: "))
if withdraw <= balance:
    balance -= withdraw
    print(f"Withdrawal successful. Remaining balance: ₹{balance:.2f}")
else:
    print("Insufficient funds")