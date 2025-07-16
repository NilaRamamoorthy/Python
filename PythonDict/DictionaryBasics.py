
import operator

#  Dictionary Basics

# 1. Create a dictionary with five employee names and their ID numbers.
employees = {"Alice": 1001, "Bob": 1002, "Charlie": 1003, "David": 1004, "Eva": 1005}

# 2. Access and print the phone number from a contact dictionary.
contact = {"John": "555-1234", "Jane": "555-5678"}
print(contact["Jane"])

# 3. Use the get() method to retrieve a value that may not exist in the dictionary.
print(contact.get("Jake", "Not Found"))

# 4. Add a new key-value pair to a student marks dictionary.
marks = {"Tom": 85, "Jerry": 90}
marks["Spike"] = 88

# 5. Update an existing student's score in the marks dictionary.
marks["Tom"] = 95

# 6. Delete a key from a dictionary using del.
del marks["Jerry"]

# 7. Use pop() to remove a key and display the returned value.
removed_score = marks.pop("Spike")
print(removed_score)

# 8. Use popitem() and explain how it works.
# Removes and returns the last inserted key-value pair.
last_item = employees.popitem()
print(last_item)

# 9. Clear all entries in a dictionary using clear() and show the result.
employees.clear()
print(employees)  # {}

# 10. Check if a key exists in the dictionary using the in keyword.
print("Tom" in marks)

# Dictionary Iteration
data = {"a": 10, "b": 95, "c": 88, "d": 100}

# 11. Loop through a dictionary and print all keys.
for key in data:
    print(key)

# 12. Loop through a dictionary and print all values.
for value in data.values():
    print(value)

# 13. Loop through both keys and values using .items().
for k, v in data.items():
    print(f"{k}: {v}")

# 14. Count how many values in a dictionary are above a certain threshold (e.g., 90).
count = sum(1 for v in data.values() if v > 90)
print(count)

# 15. Create a function that returns all keys that have a specific value.
def keys_with_value(d, target):
    return [k for k, v in d.items() if v == target]


#  Dictionary Methods
# 16. Use update() to merge two dictionaries.
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
a.update(b)

# 17. Use setdefault() to add a key only if it doesn't exist.
a.setdefault("w", 5)

# 18. Use copy() to duplicate a dictionary, then prove they are separate.
copy_dict = a.copy()
copy_dict["x"] = 999
print(a["x"] != copy_dict["x"])

# 19. Create a dictionary using dict() constructor from a list of tuples.
tuple_list = [("apple", 3), ("banana", 5)]
fruit_dict = dict(tuple_list)

# 20. Get a list of all keys using .keys() and all values using .values().
print(list(fruit_dict.keys()))
print(list(fruit_dict.values()))



# Practical Use Cases
# 21. Shopping cart: item name as key, quantity as value.
cart = {"apple": 2, "banana": 4, "milk": 1}

# 22. Grade book with student names and grades.
grades = {"Liam": "A", "Noah": "B", "Emma": "A+"}

# 23. Phonebook dictionary and search.
phonebook = {"Alice": "1234", "Bob": "5678"}
print(phonebook.get("Bob", "Not Found"))

# 24. Product inventory system.
inventory = {
    "P001": {"name": "Laptop", "stock": 5},
    "P002": {"name": "Mouse", "stock": 12}
}

# 25. Attendance tracker: date → list of students
attendance = {
    "2025-07-15": ["Alice", "Bob"],
    "2025-07-16": ["Charlie"]
}


#  Nested Dictionaries
# 26. Nested dictionary for employees
employees = {
    101: {"name": "Alice", "salary": 50000},
    102: {"name": "Bob", "salary": 60000}
}

# 27. Access a nested value
print(employees[101]["salary"])

# 28. Add a new employee
employees[103] = {"name": "Charlie", "salary": 55000}

# 29. Update salary of specific employee
employees[102]["salary"] = 65000

# 30. Loop through and print name and salary
for emp in employees.values():
    print(emp["name"], emp["salary"])


# Dictionary Comprehension
# 31. Squares: {n: n**2 for n in range(1, 6)}
squares = {n: n**2 for n in range(1, 6)}

# 32. Even/Odd dictionary
nums = [1, 2, 3, 4]
evenodd = {n: "even" if n % 2 == 0 else "odd" for n in nums}

# 33. Words → lengths
words = ["apple", "banana"]
word_lengths = {word: len(word) for word in words}

# 34. Swap keys and values
original = {"a": 1, "b": 2}
swapped = {v: k for k, v in original.items()}

# 35. Filter values > 90
filtered = {k: v for k, v in data.items() if v > 90}


# Data Processing
# 36. Frequency of characters
s = "hello world"
char_freq = {}
for c in s:
    if c != " ":
        char_freq[c] = char_freq.get(c, 0) + 1

# 37. Word count from paragraph
para = "This is a test. This test is simple."
words = para.lower().replace(".", "").split()
word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1

# 38. Fruit prices → most expensive
prices = {"apple": 2.5, "banana": 1.2, "mango": 3.0}
most_exp = max(prices, key=prices.get)

# 39. Total value of inventory
price = {"item1": 10, "item2": 5}
qty = {"item1": 2, "item2": 3}
total = sum(price[i] * qty.get(i, 0) for i in price)

# 40. Group students by grade
students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A")]
by_grade = {}
for name, grade in students:
    by_grade.setdefault(grade, []).append(name)


# Advanced Applications
# 41. Caching system
cache = {}
def square(n):
    if n not in cache:
        cache[n] = n ** 2
    return cache[n]

# 42. URL shortener
url_map = {}
def shorten(url):
    code = f"u{len(url_map)+1}"
    url_map[code] = url
    return code

# 43. English → Tamil translator
translator = {"apple": "ஆப்பிள்", "banana": "வாழைப்பழம்"}

# 44. Login system
users = {"admin": "pass123"}
def login(user, pw):
    return users.get(user) == pw

# 45. Movie collection manager
movies = {
    "Inception": {"year": 2010, "genre": "Sci-Fi"},
    "Titanic": {"year": 1997, "genre": "Romance"}
}


# Utility Tools

# 46. Calculator using functions
calc = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
print(calc["+"](4, 3))

# 47. Travel expense tracker
expenses = {"Paris": 1200, "Tokyo": 1500, "Delhi": 800}

# 48. File extension counter
files = ["doc1.txt", "image.png", "data.csv", "notes.txt"]
ext_count = {}
for f in files:
    ext = f.split(".")[-1]
    ext_count[ext] = ext_count.get(ext, 0) + 1

# 49. Countries to capitals
capitals = {"India": "New Delhi", "France": "Paris"}
print(capitals.get("France", "Not found"))

# 50. Quiz app
quiz = {"Capital of France?": "Paris", "5 + 3 = ?": "8"}
answers = {"Capital of France?": "Paris", "5 + 3 = ?": "9"}
score = sum(1 for q in quiz if quiz[q] == answers.get(q))
print("Score:", score)

