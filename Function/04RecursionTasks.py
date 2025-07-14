# Recursion Tasks (21–25)

# Task 21: Write a recursive function to calculate factorial of a number.
def fact(num):
    if num==1:
        return 1
    return num*(fact(num-1))

number=int(input("Enter a number to find factorial: "))
result=fact(number)
print(f"Factorial of the {number} is: {result}")
print("-"*40)

# Task 22: Create a recursive function to calculate the nth Fibonacci number.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter n to find nth Fibonacci number: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
print("-"*40)
    
# Task 23: Use recursion to reverse a string.
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])
word = "python"
print(f"Original: {word}")
print(f"Reversed: {reverse_string(word)}")
print("-"*40)

# Task 24: Use recursion to sum all elements in a list.
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])
numbers = [10, 20, 30, 40]
print(f"List: {numbers}")
print(f"Sum: {sum_list(numbers)}")
print("-"*40)

# Task 25: Write a recursive function that counts down from a number to 1.

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

print("Countdown from 5:")
countdown(5)
print("-"*40)

