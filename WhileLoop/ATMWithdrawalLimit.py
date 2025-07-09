#6. ATM Withdrawal Limit System
initial_balance=50000
balance=0
total_withdraw=0
while total_withdraw<=10000:
    withdraw=input("Enter Amount to withdraw ot (type 'stop' to cancel): ").lower()
    if withdraw=="stop":
        print("customer canceled the transaction")
        break
    else:
        withdraw=int(withdraw)
        total_withdraw+=withdraw
        if total_withdraw<=10000:
            balance=initial_balance-withdraw
            initial_balance=balance
            print(f"Amount withdrawn: {withdraw}")
            print(f"Balance: {balance}")

        
else:
    print("You have reached you daily limit!")