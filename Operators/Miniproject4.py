# Simple ATM Simulation
# Input: initial balance
balance = float(input("Enter your initial balance: ₹"))

# Ask user what they want to do
action = input("Do you want to 'deposit' or 'withdraw'?: ").strip().lower()

# Perform the selected action
if action == "deposit":
    amount = float(input("Enter deposit amount: ₹"))
    balance += amount
    print(f"₹{amount} deposited successfully.")
    print(f"Updated Balance: ₹{balance:.2f}")

elif action == "withdraw":
    amount = float(input("Enter withdrawal amount: ₹"))
    if amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{balance:.2f}")
    else:
        print("Insufficient balance. Transaction failed.")
        print(f"Available Balance: ₹{balance:.2f}")

else:
    print("Invalid action. Please choose 'deposit' or 'withdraw'.")

print("=== Thank You for Using Simple ATM ===")
