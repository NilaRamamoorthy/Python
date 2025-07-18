from calculator.basic import add, subtract, multiply, divide
from calculator.advanced import power, modulus, floor_division

def perform_operation(choice, a, b):
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: power,
        6: modulus,
        7: floor_division
    }

    operation = operations.get(choice)
    if operation:
        return operation(a, b)
    return "Invalid Choice"
