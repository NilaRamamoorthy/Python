import math

def radians_to_degrees(func):
    """Decorator to convert radians to degrees for trigonometric functions."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return math.degrees(result)
    return wrapper

class ScientificCalculator:
    def __init__(self):
        self.operations = {
            'sin': self.sin,
            'cos': self.cos,
            'tan': self.tan,
            'log': self.log,
            'sqrt': self.sqrt,
            'exp': self.exp,
            'factorial': self.factorial,
            'exit': self.exit_calculator
        }

    @radians_to_degrees
    def sin(self, x):
        return math.sin(x)

    @radians_to_degrees
    def cos(self, x):
        return math.cos(x)

    @radians_to_degrees
    def tan(self, x):
        return math.tan(x)

    def log(self, x):
        return math.log(x)

    def sqrt(self, x):
        return math.sqrt(x)

    def exp(self, x):
        return math.exp(x)

    def factorial(self, x):
        try:
            return math.factorial(x)
        except ValueError:
            return "Factorial is not defined for negative numbers."

    def exit_calculator(self, x=None):
        print("Exiting calculator.")
        exit()

    def get_input(self):
        while True:
            try:
                expression = input("Enter operation and number(s), or 'exit' to quit: ").split()
                op = expression[0].lower()
                if op not in self.operations:
                    print("Invalid operation. Try again.")
                    continue
                if op == 'exit':
                    self.operations[op]()
                elif len(expression) == 2:
                    num = float(expression[1])
                    print(f"Result: {self.operations[op](num)}")
                elif len(expression) == 3:
                    num1, num2 = float(expression[1]), float(expression[2])
                    print(f"Result: {self.operations[op](num1, num2)}")
                else:
                    print("Invalid input format. Try again.")
            except ValueError:
                print("Invalid number format. Please enter valid numbers.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.get_input()
