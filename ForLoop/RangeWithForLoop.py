# Range() with For Loop (16–20)

# Task 16: Print all numbers between 1 and 50 that are divisible by 5
print("Task 16:")
for i in range(1, 51):
    if i % 5 == 0:
        print(i)
print()

# Task 17: Print even numbers between 2 and 20 using range()
print("Task 17:")
for i in range(2, 21, 2):
    print(i)
print()

# Task 18: Ask for a starting and ending number and print the range
print("Task 18:")
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for i in range(start, end + 1):
    print(i)
print()

# Task 19: Print powers of 2 up to 1024 using for loop
print("Task 19:")
for i in range(1, 11):  # 2^1 to 2^10 (2^10 = 1024)
    print(2 ** i)
print()

# Task 20: Print square of numbers from 1 to 10
print("Task 20:")
for i in range(1, 11):
    print(f"{i}^2 = {i*i}")
