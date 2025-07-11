# 8. Sentence Analyzer

sentence=input("Enter a Sentence: ").strip()
print(f"First Character: {sentence[0]}")
print(f"Last Character: {sentence[-1]}")
print(f"First Space: {sentence.find(" ")}")
space_count=sentence.count(" ")
count=0
for key in sentence:
    if key in "aeiou":
        count+=1
print(f"Total vowels: {count}")
print(f"Total Spaces: {space_count}")


