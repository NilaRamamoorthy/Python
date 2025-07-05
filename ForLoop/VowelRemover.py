text = input("Enter a sentence: ")
result = ""
for char in text:
    if char.lower() in "aeiou":
        continue
    result += char
print("Without vowels:", result)
