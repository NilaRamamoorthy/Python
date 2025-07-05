# Task 31: Use enumerate() to print index and value for "Python"
print("Task 31:")
for index, value in enumerate("Python"):
    print(index, value)
print()

# Task 32: Use enumerate() with a fruit list to print like: 1. Apple 2. Banana ...
print("Task 32:")
fruits = ["Apple", "Banana", "Cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
print()

# Task 33: Use enumerate() to display character positions in "Hello World"
print("Task 33:")
for pos, char in enumerate("Hello World"):
    print(f"Position {pos}: {char}")
print()

# Task 34: Create a list of students and print roll number using enumerate(start=101)
print("Task 34:")
students = ["John", "Sara", "Meena"]
for roll, student in enumerate(students, start=101):
    print(f"Roll No: {roll} - {student}")
print()

# Task 35: Use enumerate() inside a function that labels each item in a menu list
print("Task 35:")
def show_menu(menu):
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")

menu_items = ["Pizza", "Burger", "Pasta"]
show_menu(menu_items)
print()

