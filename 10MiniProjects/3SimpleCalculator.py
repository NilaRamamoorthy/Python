import math

class SimpleCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    def calculate(self, expression):
        try:
            # Evaluate expression with support for parentheses
            result = eval(expression, {"__builtins__": None}, {})
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            return f"Error: {e}"

    def store_memory(self, value):
        self.memory = value
        print(f"Stored {value} in memory.")

    def recall_memory(self):
        print(f"Recalled {self.memory} from memory.")
        return self.memory

    def show_history(self):
        if not self.history:
            print("No calculations yet.")
        else:
            print("Calculation History:")
            for h in self.history:
                print(h)

    def convert_units(self):
        print("\nUnit Conversion:")
        print("1. Length (meters to feet)")
        print("2. Weight (kilograms to pounds)")
        choice = input("Choose conversion: ")

        if choice == '1':
            meters = float(input("Enter meters: "))
            feet = meters * 3.28084
            print(f"{meters} meters = {feet:.2f} feet")
        elif choice == '2':
            kg = float(input("Enter kilograms: "))
            pounds = kg * 2.20462
            print(f"{kg} kg = {pounds:.2f} pounds")
        else:
            print("Invalid choice")

def main():
    calc = SimpleCalculator()
    print("Simple Calculator")
    while True:
        print("\nMenu:")
        print("1. Calculate Expression")
        print("2. Store Value to Memory")
        print("3. Recall Memory")
        print("4. Show Calculation History")
        print("5. Unit Conversion")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            expr = input("Enter expression (e.g. 2+3*(4-1)): ")
            result = calc.calculate(expr)
            print(f"Result: {result}")

        elif choice == '2':
            val = input("Enter value to store: ")
            try:
                val = float(val)
                calc.store_memory(val)
            except ValueError:
                print("Invalid value.")

        elif choice == '3':
            mem = calc.recall_memory()
            print(f"Memory: {mem}")

        elif choice == '4':
            calc.show_history()

        elif choice == '5':
            calc.convert_units()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
