# Task 36: Create a multiplication table for numbers 1 to 3 using nested loops
print("Task 36:")
for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
    
# Task 37: Print pattern: * * ** * ** * * *
print("Task 37:")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
print()

# Task 38: Print a number triangle:
# 1
# 1 2
# 1 2 3
print("Task 38:")
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

# Task 39: Print all pair combinations from two lists
print("Task 39:")
list1 = ["Red", "Blue"]
list2 = ["Circle", "Square"]
for color in list1:
    for shape in list2:
        print(f"{color} - {shape}")
print()

# Task 40: Multiplication chart from 1x1 to 5x5
print("Task 40:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()
print()

# Task 41: Right-angled triangle with alphabets
print("Task 41:")
ch = ord('A')
for i in range(1, 4):
    for j in range(i):
        print(chr(ch), end=" ")
    ch += 1
    print()
print()

# Task 42: Triangle pattern with name characters
print("Task 42:")
name = input("Enter your name: ")
for i in range(1, len(name)+1):
    for j in range(i):
        print(name[j], end=" ")
    print()
print()

# Task 43: Pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
print("Task 43:")
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()
print()

# Task 44: Print a 3x3 grid using nested loops
print("Task 44:")
for i in range(3):
    for j in range(3):
        print("#", end=" ")
    print()
print()

# Task 45: Star pattern with custom rows and columns
print("Task 45:")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
