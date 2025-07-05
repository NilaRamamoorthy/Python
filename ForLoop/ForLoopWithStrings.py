# Task 11: Print all vowels in "Technology" using a for loop
print("Task 11:")
text = "Technology"
for char in text:
    if char.lower() in "aeiou":
        print(char)
print()

# Task 12: Count and display the number of vowels in a given string
print("Task 12:")
user_input = input("Enter a string: ")
vowel_count = 0
for char in user_input:
    if char.lower() in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)
print()

# Task 13: Count the number of lowercase letters in "Python Loop Practice"
print("Task 13:")
sample_text = "Python Loop Practice"
lower_count = 0
for char in sample_text:
    if char.islower():
        lower_count += 1
print("Number of lowercase letters:", lower_count)
print()

# Task 14: Print each word in the string "Learn Python Fast"
print("Task 14:")
sentence = "Learn Python Fast"
words = sentence.split()
for word in words:
    print(word)
print()

# Task 15: Reverse a string using a for loop (without using slicing)
print("Task 15:")
original = "Technology"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)
print()

