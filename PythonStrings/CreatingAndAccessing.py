# SECTION 1: Creating and Accessing Strings (1–10)

# Task 1: Create a string using single, double, and triple quotes
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''Python is powerful'''
print("Task 1:", single_quote, double_quote, triple_quote)

print("-" * 40)

# Task 2: Create a multiline quote using triple quotes and print it
multi_line = """Success is not final,
Failure is not fatal,
It is the courage to continue that counts."""
print("Task 2:\n" + multi_line)

print("-" * 40)

# Task 3: Access first and last characters using positive and negative indexing
text = "Programming"
print("Task 3: First =", text[0], ", Last =", text[-1])

print("-" * 40)

# Task 4: Print every character in a string using a for loop
print("Task 4:")
for char in text:
    print(char, end=" ")
print()

print("-" * 40)

# Task 5: Slice to extract middle 3 characters
mid = len(text) // 2
middle_three = text[mid - 1:mid + 2]
print("Task 5: Middle 3 characters =", middle_three)

print("-" * 40)

#  Task 6: Access and print every second character
print("Task 6: Every second character =", text[::2])

print("-" * 40)

#  Task 7: Print all vowels using indexing and conditions
print("Task 7: Vowels in the string:")
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        print(char, end=" ")
print()

print("-" * 40)

#  Task 8: Extract domain from an email
email = "user@gmail.com"
domain = email[email.find("@") + 1:]
print("Task 8: Domain =", domain)

print("-" * 40)

#  Task 9: Check if first and last characters are the same
sample = "radar"
result = "Yes" if sample[0] == sample[-1] else "No"
print(f"Task 9: First and last same? {result}")

print("-" * 40)

#  Task 10: Reverse a string using slicing
reversed_text = text[::-1]
print("Task 10: Reversed string =", reversed_text)
