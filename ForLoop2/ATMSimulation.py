balance = 5000
for i in range(3):
    choice = input("Choose operation (deposit/withdraw/balance): ").lower()
    if choice == "deposit":
        amt = float(input("Enter amount to deposit: "))
        balance += amt
    elif choice == "withdraw":
        amt = float(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance.")
    elif choice == "balance":
        print(f"Current balance: ₹{balance}")