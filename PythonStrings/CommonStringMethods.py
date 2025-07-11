# SECTION 4: Common String Methods (21–35)

# 21 Use len() to count the characters in a string.
str="Impossible"
print(f"Lenth of impossible is: {len(str)}")

# 22 Convert a string to lowercase using .lower().
print(f"string in lower case: {str.lower()}")

# 23 Convert a string to uppercase using .upper().
print(f"string in lower case: {str.upper()}")

# 24 Remove leading and trailing whitespaces using .strip().
print(f"string in lower case: {str.strip()}")

# 25 Use .replace() to change "bad" to "good" in a sentence.
str1="Cucumber is a bad food"
updated=str.replace("bad","good")
print(f"Original String: {str1}")
print(f"Updated String: {updated}")

# 26 Split a comma-separated string into a list using .split(',').
str2="apple,banana,orange,mango"
str_list=str2.split(",")
print(f"String before Split{str2}")
print("After Split: ")
print(str_list)

# 27 Join a list of words with - using .join().
words = ["code", "with", "nila"]
joined = "-".join(words)
print("Task 27:", joined)

# 28 Count how many times "a" appears in "banana" using .count().
word = "banana"
count_a = word.count("a")
print("Task 28: 'a' appears", count_a, "times")

# 29 Use .find() to get the first index of the letter 'o' in "Google".
text = "Google"
index_o = text.find("o")
print("Task 29: First 'o' is at index", index_o)

# 30 Create a program to convert 'Python is FUN' to 'python-is-fun'.
text = "Python is FUN"
formatted = text.lower().replace(" ", "-")
print("Task 30:", formatted)

# 31 Write a function that counts vowels and consonants in a string.
def count_vowels_consonants(s):
    vowels = "aeiou"
    v_count = c_count = 0
    for char in s.lower():
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

v, c = count_vowels_consonants("Python is Awesome")
print(f"Task 31: Vowels = {v}, Consonants = {c}")

# 32 Use .replace() to remove all spaces from a string.
text = "Remove all spaces here"
no_space = text.replace(" ", "")
print("Task 32:", no_space)

# 33 Use .split() and a for loop to print each word on a new line.
text = "Print each word separately"
for word in text.split():
    print("Task 33:", word)


# 34 Print the middle character of a string (if odd length).
text = "middle"
if len(text) % 2 == 1:
    middle = text[len(text)//2]
    print("Task 34: Middle character:", middle)
else:
    print("Task 34: String has even length, no single middle character")


# 35 Write a function that returns the first and last characters combined.
def first_last_chars(s):
    if len(s) >= 2:
        return s[0] + s[-1]
    return s  # If only one character

result = first_last_chars("banana")
print("Task 35:", result)
