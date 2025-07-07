# 19. Word Frequency Counter
word = input("Enter a word: ")
count = {}
for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)