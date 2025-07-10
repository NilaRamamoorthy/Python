# Task 31: Lambda to add two numbers
add = lambda a, b: a + b
print("Add →", add(10, 5))
print("-"*40)

# Task 32: Lambda to return square of a number
square = lambda x: x * x
print("Square →", square(6))
print("-"*40)

# Task 33: Use lambda with sorted() to sort list of tuples by second value
data = [("apple", 3), ("banana", 1), ("cherry", 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted by second value →", sorted_data)
print("-"*40)

# Task 34: Replace normal function with lambda
# Normal: def double(x): return x * 2
double = lambda x: x * 2
print("Double using lambda →", double(7))
print("-"*40)

# Task 35: Function returning a lambda (closure)
def make_multiplier(n):
    return lambda x: x * n

triple = make_multiplier(3)
print("Multiplier lambda (3×5) →", triple(5))
print("-"*40)