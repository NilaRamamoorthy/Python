# 3. Word Frequency Counter

paragraph=input("Enter a paragraph: ").lower()
words=paragraph.split(" ")
length=len(words)
word_set=set(words)
for word in word_set:
    print(f"{word}: {words.count(word)}")
print(f"Total number of words: {length}")