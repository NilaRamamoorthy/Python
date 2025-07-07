# 18. Palindrome Checker
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
if word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")