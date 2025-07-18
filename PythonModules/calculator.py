from calculator.interface import perform_operation

def show_menu():
    print("""
--- Calculator Menu ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Modulus
7. Floor Division
8. Exit
""")

def main():
    while True:
        show_menu()
        choice = int(input("Enter your choice (1-8): "))
        if choice == 8:
            print("Exiting calculator.")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = perform_operation(choice, a, b)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
