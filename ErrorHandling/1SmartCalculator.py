import logging

# Setup logging
logging.basicConfig(filename="calculator_errors.log", level=logging.ERROR, format='%(asctime)s - %(message)s')

# Custom exception
class InvalidOperationError(Exception):
    pass

def smart_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /, %): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            raise InvalidOperationError(f"Invalid operator: {operator}")
    
    except ZeroDivisionError:
        logging.error("Attempted division by zero.")
        print("Error: Cannot divide by zero.")
    
    except ValueError:
        logging.error("Non-numeric input entered.")
        print("Error: Please enter valid numbers.")
    
    except InvalidOperationError as e:
        logging.error(str(e))
        print("Error:", e)
    
    else:
        print("Result:", result)
    
    finally:
        print("Calculation complete.")

# Run the calculator
smart_calculator()
