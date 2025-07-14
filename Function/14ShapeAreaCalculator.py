import math

def area_calculator(shape, *args):
    shape = shape.lower()

    if shape == "circle" and len(args) == 1:
        area = lambda r: math.pi * r * r
        return f"Area of Circle: {area(args[0]):.2f}"

    elif shape == "rectangle" and len(args) == 2:
        area = lambda l, b: l * b
        return f"Area of Rectangle: {area(args[0], args[1])}"

    elif shape == "square" and len(args) == 1:
        area = lambda s: s * s
        return f"Area of Square: {area(args[0])}"

    else:
        return "Invalid shape or arguments provided."

# Examples
print(area_calculator("circle", 7))
print(area_calculator("rectangle", 5, 10))
print(area_calculator("square", 4))
print(area_calculator("triangle", 4, 5))  # Invalid input
