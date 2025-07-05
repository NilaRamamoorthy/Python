# Task 1: Print all elements in the list ["Pen", "Pencil", "Eraser"]
print("Task 1:")
items = ["Pen", "Pencil", "Eraser"]
for item in items:
    print(item)
print()

# Task 2: Print each character in the string "Vetri" one by one
print("Task 2:")
name = "Vetri"
for char in name:
    print(char)
print()

# Task 3: Use range() to print numbers from 1 to 10
print("Task 3:")
for i in range(1, 11):
    print(i)
print()

# Task 4: Print all odd numbers from 1 to 20 using range() with step
print("Task 4:")
for i in range(1, 21, 2):
    print(i)
print()

# Task 5: Create a list of 5 colors and print them using a for loop
print("Task 5:")
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
for color in colors:
    print(color)
print()

# Task 6: Use range() to print numbers from 10 to 1 (reverse order)
print("Task 6:")
for i in range(10, 0, -1):
    print(i)
print()

# Task 7: Ask user to enter a number n, and print numbers from 1 to n
print("Task 7:")
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)
print()

# Task 8: Create a list of fruits, use a loop to print “I like <fruit>” for each fruit
print("Task 8:")
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
for fruit in fruits:
    print(f"I like {fruit}")
print()

# Task 9: Print the multiplication table of 5 using a loop
print("Task 9:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print()

# Task 10: Calculate the sum of numbers from 1 to 50 using a for loop
print("Task 10:")
total = 0
for i in range(1, 51):
    total += i
print("Sum from 1 to 50 is:", total)
