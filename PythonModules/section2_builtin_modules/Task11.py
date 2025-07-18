import math

def calculator():
    print("Math Calculator")
    print("1. Square Root")
    print("2. Power")
    print("3. Factorial")

    choice = input("Choose operation (1/2/3): ")
    if choice == '1':
        num = float(input("Enter number: "))
        print("Square root:", math.sqrt(num))
    elif choice == '2':
        base = float(input("Enter base: "))
        exp = float(input("Enter exponent: "))
        print("Result:", math.pow(base, exp))
    elif choice == '3':
        num = int(input("Enter number: "))
        print("Factorial:", math.factorial(num))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    calculator()
