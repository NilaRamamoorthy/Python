from auth import authenticate
from banking_ops import deposit, withdraw, view_balance, view_statement, show_transaction_types

def main():
    print("🏦 Welcome to Simple Bank App")
    username = input("Username: ")
    password = input("Password: ")

    if not authenticate(username, password):
        print("❌ Invalid credentials.")
        return

    while True:
        print(f"\n🧾 Hello {username}, choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. View Statement")
        print("5. View Transaction Types")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            deposit(username, amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            withdraw(username, amt)
        elif choice == '3':
            view_balance(username)
        elif choice == '4':
            view_statement(username)
        elif choice == '5':
            show_transaction_types(username)
        elif choice == '6':
            print("👋 Exiting. Thank you for using Simple Bank App.")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
