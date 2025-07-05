# Assignment Operators Tasks (21–26)

# Task 21
num = 10
print("Initial value:", num)

num += 5
print("After += 5:", num)

num -= 3
print("After -= 3:", num)

num *= 2
print("After *= 2:", num)

num /= 4
print("After /= 4:", num)

num //= 2
print("After //= 2:", num)

num %= 3
print("After %= 3:", num)
print("-" * 40)

# Task 22
num = int(input("Enter a number: "))
num += 5
print("Updated number:", num)
print("-" * 40)

# Task 23
side = int(input("Enter side of square: "))
area = side * side
print("Original area:", area)
area *= 2
print("Doubled area:", area)
print("-" * 40)

# Task 24
salary = float(input("Enter your salary: "))
tax = float(input("Enter tax amount to deduct: "))
salary -= tax
print("Salary after tax:", salary)
print("-" * 40)

# Task 25
val = int(input("Enter a starting number: "))
print("Initial value:", val)

val += 10
print("After += 10:", val)

val -= 5
print("After -= 5:", val)

val *= 2
print("After *= 2:", val)

val /= 3
print("After /= 3:", val)

val //= 2
print("After //= 2:", val)

val %= 4
print("After %= 4:", val)
print("-" * 40)

# Task 26
balance=400000
choice = input("Would you like to 'deposit' or 'withdraw' first? ").strip().lower()

if choice == "deposit":
    deposit = float(input("Enter amount to deposit: "))
    balance += deposit
    print("Balance after deposit:", balance)

elif choice == "withdraw":
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw<balance:
        balance -= withdraw
        print("Balance after withdrawal:", balance)
    else:
        print("Insufficient Balance")    
else:
    print("Invalid choice.")
   

