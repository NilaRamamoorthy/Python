# 9. Word Reverser
sentence=input("Enter a sentence: ").strip()
words=sentence.split(" ")

print(words)
updated=[]
for index in words:
    updated.append(index[::-1])

print(f"Reversed String: {" ".join(updated)}")
