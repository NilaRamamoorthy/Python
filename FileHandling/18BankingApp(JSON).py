import json
import os

BANK_FILE = "bank_data.json"

def load_accounts():
    if os.path.exists(BANK_FILE):
        with open(BANK_FILE, "r") as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    with open(BANK_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter account holder's name: ")
    balance = float(input("Enter opening balance: "))
    
    accounts = load_accounts()
    if acc_no in accounts:
        print("Account already exists.")
        return

    accounts[acc_no] = {"name": name, "balance": balance}
    save_accounts(accounts)
    print("Account created successfully.")

def deposit():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))

    accounts = load_accounts()
    if acc_no in accounts:
        accounts[acc_no]["balance"] += amount
        save_accounts(accounts)
        print(f"Deposited {amount}. New balance: {accounts[acc_no]['balance']}")
    else:
        print("Account not found.")

def withdraw():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))

    accounts = load_accounts()
    if acc_no in accounts:
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            save_accounts(accounts)
            print(f"Withdrawn {amount}. Remaining balance: {accounts[acc_no]['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def check_balance():
    acc_no = input("Enter account number: ")

    accounts = load_accounts()
    if acc_no in accounts:
        print(f"Account Holder: {accounts[acc_no]['name']}")
        print(f"Balance: {accounts[acc_no]['balance']}")
    else:
        print("Account not found.")

def main():
    while True:
        print("\n--- Banking App ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

main()
