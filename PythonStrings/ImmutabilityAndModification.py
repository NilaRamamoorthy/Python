# SECTION 2: Immutability and Modification (11–15)

# Task 11: Try to modify a single character in a string (this will cause an error)
try:
    text = "hello"
    text[0] = "H"  # Strings are immutable in Python, this will raise TypeError
except TypeError:
    print("Task 11: Strings are immutable – you cannot modify a character directly.")

print("-" * 40)

# Task 12: Change the first character using slicing and concatenation
text = "hello"
modified = "H" + text[1:]
print("Task 12:", modified)

print("-" * 40)

# Task 13: Replace a character in the middle by reconstructing the string
text = "python"
mid_index = len(text) // 2
reconstructed = text[:mid_index] + "X" + text[mid_index + 1:]
print("Task 13:", reconstructed)

print("-" * 40)

# Task 14: Function to replace all vowels with '*'
def mask_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        result += "*" if ch in vowels else ch
    return result

print("Task 14:", mask_vowels("Education is Power"))

print("-" * 40)

# Task 15: Function to replace all occurrences of 'a' with '@'
def replace_a_with_at(s):
    return s.replace('a', '@')

print("Task 15:", replace_a_with_at("banana is amazing"))
