# Infinite While Loop Tasks (11–15)

#Task 11
# while True:
#     print("Welcome")
print("-"*40)
#Task 12
while True:
    password=input("Enter password: ")
    if password== "1234":
        print("You are LoggedIn")
        break
print("-"*40)
# Task 13: Menu-Based Application

while True:
    print("\n--- Main Menu ---")
    print("1. Greet")
    print("2. Show Info")
    print("3. Help")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Hello! Welcome to our app.")
    elif choice == "2":
        print("This is a simple menu-based Python application.")
    elif choice == "3":
        print("Choose 1 to greet, 2 for info, 4 to exit.")
    elif choice == "4":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

print("-"*40)
#Task 14
while True:
    number=int(input("Enter a number"))
    if number<0:
        print("You entered a negative number")
        break
print("-"*40)
# Task 15: Simple ATM System
balance = 10000  # Initial balance

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is ₹{balance}")
    
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"₹{amount} deposited successfully.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
