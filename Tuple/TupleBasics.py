# 1. Tuple Basics
#Task 1: Create an empty tuple and print its type.
tup=[]
print(type(tup))

#Task 2: Create a tuple with integers, strings, and a float and print each item.
tup1=[1,"apple",0.3]
for tup in range(len(tup1)):
    print(tup1[tup])

#Task 3: Create a tuple with only one element and print its type.
tup2=["orange"]
print(type(tup2[0]))

#Task 4: Convert a list of numbers [1, 2, 3, 4, 5] to a tuple.
list=[1,2,3,4,5]
tup3=tuple(list)
print(tup3)

#Task 5: Convert the string "Python" into a tuple of characters.
str="Python"
tup4=tuple(str)
print(tup4)

# 2. Tuple Indexing and Slicing

#Task 6: Access the first and last elements of a tuple.
fruits=['apple','orange','grapes','banana']
print(f"First element of fruits Tuple: {fruits[0]}")
print(f"Last element of fruits Tuple: {fruits[-1]}")

#Task 7: Slice a tuple to get the middle 3 elements.
elements=(1,2,3,4,5,6,7,8)
length=len(elements)
half=int(length/2)

print(elements[half-1:half+2:])
# Task 8: Reverse a tuple using slicing.
print(fruits[::-1])

#Task 9: Access every second element from a tuple using slicing.
print(fruits[::2])

#Task 10: Get a sub-tuple using negative indexing and slicing.

sub_fruits=fruits[:-2:]
print(sub_fruits)

# 3. Tuple Immutability

# Task 11: Attempt to change a tuple element and handle the resulting error.
numbers=(1,2,3,45,5)
numbers[3]=4
print(numbers) #Raises Type Error

#Task 12: Show how to replace a value in a tuple by converting it to a list and back.
list_numbers=list(numbers)
print("Original List: ",list_numbers)
list_numbers[3]=4
list_numbers=tuple(list_numbers)
print("Updated List: ",list_numbers)

#Task 13: Add a new value to a tuple (simulate by tuple concatenation).
numbers=numbers+(6,7,8)
print(numbers)

#Task 14: Remove an item from a tuple (simulate by list conversion).
my_tuple=(11,22,33,44,55)
new_list=list(my_tuple)
print(new_list)

#Task 15: Demonstrate that tuples cannot be deleted partially (e.g., del tuple[0]).

del numbers[3] #Raises Type Error (tuple does not support item deletion)
print(numbers)

# 4. Tuple Operations
#Task 16: Concatenate two tuples.
tupp1=(1,2,3,4,5)
tupp2=(6,7,8,9,0)

#Task 17: Repeat a tuple 3 times using the * operator.
print((1,2,3,4)*3)

#Task 18: Check if an item exists in a tuple using in.
fruits = ('apple', 'banana', 'cherry', 'mango')

if 'banana' in fruits:
    print("Yes, 'banana' is in the tuple.")
else:
    print("No, 'banana' is not in the tuple.")


#Task 19: Find the length of a tuple using len().
tupp_length=len(tupp1)
print(f"Length of the Tuple: {tupp_length}")

#Task 20: Count the number of times an element occurs in a tuple.
tupp3=(1,2,3,3,5,6,3,4,5)
count=tupp3.count("3")
print(f"Count of 3 in tupp3: {count}")

# 5. Tuple Functions and Methods

#Task 21: Use the count() method to count element occurrences.
colors = ('red', 'blue', 'green', 'red', 'yellow', 'red')
print("Count of 'red':", colors.count('red'))

#Task 22: Use the index() method to find the position of an item.
print("Index of 'green':", colors.index('green'))

#Task 23: Use max() and min() on a tuple of numbers.
numbers = (10, 20, 5, 8, 100)
print("Max value:", max(numbers))
print("Min value:", min(numbers))

#Task 24: Use sum() to find the total of tuple items.
print("Sum of all numbers:", sum(numbers))

#Task 25: Sort a tuple using sorted() (returns a list).
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)


# 6. Iteration and Looping with Tuples

#Task 26: Iterate over a tuple using a for loop and print all elements.
for fruit in ('apple', 'banana', 'cherry'):
    print("Fruit:", fruit)

#Task 27: Iterate with enumerate() to print index and value.
for index, value in enumerate(('dog', 'cat', 'parrot')):
    print(f"Index {index}: {value}")

#Task 28: Use a while loop to iterate through a tuple.
animals = ('lion', 'tiger', 'bear')
i = 0
while i < len(animals):
    print("Animal:", animals[i])
    i += 1

#Task 29: Print all even numbers from a tuple.
nums = (1, 2, 3, 4, 5, 6, 7, 8)
for num in nums:
    if num % 2 == 0:
        print("Even number:", num)

#Task 30: Count how many strings start with “A” in a tuple of names.
names = ('Alice', 'Bob', 'Andrew', 'Angela', 'Steve')
count = sum(1 for name in names if name.startswith('A'))
print("Names starting with 'A':", count)


# 7. Nested Tuples

#Task 31: Create a tuple of tuples and access inner elements.
nested = ((1, 2), (3, 4), (5, 6))
print("Element [1][1]:", nested[1][1])

#Task 32: Print all sub-tuples from a nested tuple.
for sub in nested:
    print("Sub-tuple:", sub)

#Task 33: Sum all numbers from a tuple of tuples like ((1,2), (3,4)).
total = sum(sum(sub) for sub in nested)
print("Total sum:", total)

#Task 34: Flatten a nested tuple of integers using a loop.
flat = []
for sub in nested:
    for item in sub:
        flat.append(item)
print("Flattened:", tuple(flat))

#Task 35: Access the second element of the third sub-tuple.
print("Second element of third sub-tuple:", nested[2][1])


# 8. Tuple Packing and Unpacking

#Task 36: Pack multiple values into a tuple and print.
person = ('John', 30, 'Engineer')
print("Packed tuple:", person)

#Task 37: Unpack a tuple into individual variables.
name, age, job = person
print("Name:", name, "| Age:", age, "| Job:", job)

#Task 38: Use unpacking to swap two variables.
a, b = 10, 20
a, b = b, a
print("Swapped values:", a, b)

#Task 39: Use * to unpack remaining values from a tuple.
a, *b = (1, 2, 3, 4, 5)
print("a:", a, "| b:", b)

#Task 40: Unpack nested tuples into individual values.
nested_tuple = ('X', (1, 2))
char, (num1, num2) = nested_tuple
print("Char:", char, "| Num1:", num1, "| Num2:", num2)


# 9. Tuple Use in Functions

#Task 41: Write a function that returns multiple values as a tuple.
def get_student():
    return ('Alice', 90)

student = get_student()
print("Returned tuple:", student)

#Task 42: Pass a tuple as an argument to a function and print elements.
def print_items(items):
    for item in items:
        print("Item:", item)

print_items(('pen', 'pencil', 'eraser'))

#Task 43: Write a function to calculate average of numbers using tuple input.
def average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average((10, 20, 30)))

#Task 44: Return both min and max from a tuple using a function.
def min_max(tup):
    return (min(tup), max(tup))

print("Min and Max:", min_max((7, 2, 9, 4)))

#Task 45: Write a function to merge two tuples.
def merge_tuples(t1, t2):
    return t1 + t2

print("Merged Tuple:", merge_tuples((1, 2), (3, 4)))


# 10. Real-Life Tuple Applications

#Task 46: Store coordinates (latitude, longitude) as tuples and display them.
location = (13.0827, 80.2707)
print("Coordinates:", location)

#Task 47: Create a phone book with names and numbers stored as tuples in a list.
phone_book = [('Alice', '9876543210'), ('Bob', '9123456789')]
for name, number in phone_book:
    print(f"{name}'s number is {number}")

#Task 48: Represent RGB values of an image pixel using a tuple.
pixel = (255, 0, 128)
print("Pixel RGB:", pixel)

#Task 49: Store exam results (student_name, score) as tuples and print top scorer.
results = [('Alice', 88), ('Bob', 95), ('Charlie', 79)]
topper = max(results, key=lambda x: x[1])
print("Top Scorer:", topper)

#Task 50: Use a tuple to represent an immutable configuration (host, port, debug_mode)
config = ('localhost', 8080, True)
print("Configuration:", config)
