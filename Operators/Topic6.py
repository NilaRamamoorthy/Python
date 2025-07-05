# Membership Operators Tasks (31–35)

# Task 31
word = "elephant"
letter = input("Enter a letter to check: ")
if letter in word:
    print(f"'{letter}' is in '{word}'")
else:
    print(f"'{letter}' is not in '{word}'")
print("-" * 40)

# Task 32
fruits = ["apple", "banana", "orange", "grape", "mango"]
user_fruit = input("Enter a fruit name: ").lower()
if user_fruit in fruits:
    print(f"{user_fruit} is in the fruit list.")
else:
    print(f"{user_fruit} is not in the fruit list.")
print("-" * 40)

# Task 33
numbers = [2, 4, 6, 8, 10]
num = int(input("Enter a number: "))
if num not in numbers:
    print(f"{num} is not in the list.")
else:
    print(f"{num} is in the list.")
print("-" * 40)

# Task 34
sentence = "Python is a powerful and versatile language."
search_word = input("Enter a word to search: ").lower()
if search_word in sentence.lower():
    print(f"'{search_word}' is found in the sentence.")
else:
    print(f"'{search_word}' is not found in the sentence.")
print("-" * 40)

# Task 35
student = {"name": "Rahul", "age": 20, "grade": "A"}
key = input("Enter a key to check (name, age, grade): ")
if key in student:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does not exist in the dictionary.")
print("-" * 40)
