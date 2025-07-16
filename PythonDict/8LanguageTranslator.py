# Initial dictionary
dictionary = {
    "apple": "ஆப்பிள்",
    "banana": "வாழைப்பழம்",
    "water": "தண்ணீர்"
}

# 1. Add a new word
dictionary["milk"] = "பால்"

# 2. Update existing translation
dictionary["apple"] = "ஆப்பிள் பழம்"

# 3. Delete a word
dictionary.pop("banana", None)

# 4. Translate English → Tamil
word = "milk"
meaning = dictionary.get(word, "Translation not found")
print(f"{word} in Tamil is: {meaning}")

# 5. Reverse translation (Tamil → English)
reversed_dict = {v: k for k, v in dictionary.items()}
tamil_word = "தண்ணீர்"
english_word = reversed_dict.get(tamil_word, "English word not found")
print(f"{tamil_word} in English is: {english_word}")

# 6. Check if word exists
check_word = "water"
if check_word in dictionary:
    print(f"{check_word} is available in dictionary.")
else:
    print(f"{check_word} not found.")
