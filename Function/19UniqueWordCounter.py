def analyze_text(paragraph):
    words = paragraph.lower().split()
    total_words = len(words)
    unique_words = len(set(words))
    longest_word = max(words, key=len)
    
    return total_words, unique_words, longest_word

# Example Usage
text = input("Enter a paragraph: ")

total, unique, longest = analyze_text(text)

print(f"\nTotal Words: {total}")
print(f"Unique Words: {unique}")
print(f"Longest Word: {longest}")
