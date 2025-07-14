# List Creation & Basic Operations (Tasks 1–10)

#1 Create a list of 5 student names and print it.
students_list=["priya","maya","meera","lia"]
print(students_list)

#2 Create a list with mixed data types (int, float, string, bool) and display each element.
mix_list=["Apple",11,18.89,True]
print(mix_list)

#3 Write a program to accept 5 numbers from the user and store them in a list.
numbers=[input("Enter a number: ") for i in range(5)]
print(numbers)

#4 Create an empty list and dynamically append 3 user inputs.
new_list=[]
new_list.append("apple")
new_list.append("orange")
new_list.append("grapes")
print(new_list)

#5 Write a program to create a list of 10 even numbers using a for loop.
numbers=[]
for num in range(19):
    if num%2==0:
        numbers.append(num)
print(numbers)
        
#6 Create two lists, one with integers and one with strings, then print them together.
number_list=[2,3,4,5,6]
string_list=["Apple","Orange","Grapes","Banana"]
print(number_list+string_list)

#7 Create a list of fruits and print only the first and last items using indexing.
fruits=["Apple","Orange","Grapes","Banana","Pineapple"]
print(f"First item in the list: {fruits[0]}")
print(f"Last item in the list: {fruits[-1]}")

#8 Use negative indexing to print the second-last item in a list.
print(f"Second last item in the list: {fruits[-2]}")

#9 Write a program to count the total number of elements in a list using len().
print(f"Number of items in the list is: {len(fruits)}")

#10 Check and print the data type of a created list.
print(f"Data Type of the list: {type(fruits)}")

# -------------------------------------------------------------------------------------------#
# Accessing & Indexing Tasks (11–15)


#11 Access and print each element of a list using a for loop with indexing.
fruits=["Apple","Orange","Banana","Grapes","Pineapple"]
for num in range(len(fruits)):
    print(fruits[num])

#12 Print every alternate item from a list using slicing.
print("Alternate items:", fruits[::2])


#13 Create a list of cities and print the third character of the second city.
cities = ["Delhi", "Chennai", "Mumbai"]
print("Third character of second city:", cities[1][2])  

#14 Write a program to reverse a list using slicing.
numbers = [10, 20, 30, 40, 50]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

#15 Access the last element of a list using both positive and negative indexing.
animals = ["Dog", "Cat", "Elephant", "Tiger", "Zebra"]
print("Last element (positive index):", animals[len(animals) - 1])
print("Last element (negative index):", animals[-1])

# Adding Elements to Lists (Tasks 16–20)
#16: Start with an empty list and use append() to add 5 elements
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)
print("Task 16 - List after appending 5 elements:", numbers)


#17: Insert an element at the 3rd position in a list
items = ["pen", "book", "eraser", "scale"]
items.insert(2, "pencil")  # index 2 is the 3rd position
print("Task 17 - List after insert:", items)


#18: Use extend() to add multiple elements to an existing list
colors = ["red", "blue"]
colors.extend(["green", "yellow", "pink"])
print("Task 18 - List after extend():", colors)


#19: Take user input for a name and add it to an existing list of students
students = ["John", "Amy", "Kate"]
new_student = input("Task 19 - Enter a new student name: ").strip()
students.append(new_student)
print("Task 19 - Updated students list:", students)


#20: Add all elements from one list into another using += and extend()
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Method 1: Using +=
list1 += list2
print("Task 20 - After += :", list1)

# Method 2: Using extend()
list3 = [10, 20]
list4 = [30, 40]
list3.extend(list4)
print("Task 20 - After extend():", list3)


# Updating List Items (Tasks 21–25)

# 21. Change the first element of a list to uppercase
names = ["john", "amy", "kate"]
names[0] = names[0].upper()
print("Updated names:", names)

# 22. Modify price in list (index 2 = 999)
prices = [120, 450, 300, 650]
prices[2] = 999
print("Updated prices:", prices)

# 23. Multiply all odd numbers by 2
nums = [1, 2, 3, 4, 5, 6]
nums = [x*2 if x % 2 != 0 else x for x in nums]
print("Doubled odd numbers:", nums)

# 24. Replace fruit in a list
fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print("Replaced fruit:", fruits)

# 25. Update nested list item
nested = [[1, 2, 3], [4, 5, 6]]
nested[1][2] = 'done'
print("Updated nested list:", nested)

# Removing Elements (Tasks 26–30)
# 26. Use remove() to delete a value
items = ["pen", "pencil", "eraser"]
items.remove("pencil")
print("After remove():", items)

# 27. Use pop() without index
nums = [10, 20, 30, 40]
nums.pop()
print("After pop():", nums)

# 28. Use pop(index)
colors = ["red", "blue", "green", "yellow"]
colors.pop(1)
print("After pop(1):", colors)

# 29. Use del
marks = [88, 76, 92, 85, 67]
del marks[3]
print("After del index 3:", marks)

# 30. Use clear()
cart = ["item1", "item2", "item3"]
cart.clear()
print("After clear():", cart)


# Looping Through Lists (Tasks 31–35)
# 31. Print all in uppercase
languages = ["python", "java", "html"]
for lang in languages:
    print(lang.upper())

# 32. Find all odd numbers
nums = [1, 4, 7, 10, 13]
for n in nums:
    if n % 2 != 0:
        print("Odd:", n)

# 33. Print square of each
for n in [2, 3, 4, 5]:
    print("Square:", n**2)

# 34. Use enumerate()
for index, value in enumerate(["A", "B", "C"]):
    print(f"Index {index} → {value}")

# 35. Count "apple"
basket = ["apple", "banana", "apple", "orange", "apple"]
count = 0
for fruit in basket:
    if fruit == "apple":
        count += 1
print("Apple count:", count)


# Nested Lists (Tasks 36–40)
# 36. Create nested list
students = [["John", 85], ["Amy", 90]]

# 37. Access second student's name
print("Second student:", students[1][0])

# 38. Update marks of first student
students[0][1] = 95
print("Updated marks:", students)

# 39. Iterate and print
for s in students:
    print(f"Name: {s[0]}, Marks: {s[1]}")

# 40. Add new student
students.append(["Mike", 88])
print("After adding student:", students)


#  Concatenation, Repetition, Slicing (Tasks 41–45)
# 41. Concatenate lists
a = [1, 2, 3]
b = [4, 5, 6]
print("Concatenated:", a + b)

# 42. Repeat list
print("Repeated:", ["Hello"] * 3)

# 43. Slice first 3
data = [10, 20, 30, 40, 50]
print("First 3:", data[:3])

# 44. Slice excluding first & last
print("Middle items:", data[1:-1])

# 45. Merge numbers and strings
merged = [1, 2, 3] + ["a", "b", "c"]
print("Merged list:", merged)


# Membership & Conditional Checks (Tasks 46–50)
# 46. Check if fruit exists
fruits = ["apple", "banana", "kiwi"]
check = input("Enter a fruit: ")
if check in fruits:
    print(f"{check} is in the list.")

# 47. Remove item only if it exists
item = "mango"
if item in fruits:
    fruits.remove(item)
print("Updated fruits:", fruits)

# 48. Count specific element
names = ["john", "amy", "john", "kate"]
print("Count of 'john':", names.count("john"))

# 49. Check number in list
marks = [78, 85, 90, 67]
num = int(input("Enter a number to check: "))
if num in marks:
    print(f"{num} found in the list.")
else:
    print(f"{num} not found.")

# 50. Item presence message
item = input("Enter an item: ")
inventory = ["pen", "book", "scale"]
print(f"{item} is {'present' if item in inventory else 'not present'} in the list.")



