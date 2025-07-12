# Word Counter Tool

# Function to count words and frequency
def word_counter():
    print("Word Counter Tool")
    paragraph = input("Enter a paragraph:\n").strip().lower()

    words = paragraph.split()
    total_words = len(words)

    # Frequency count using dictionary
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    print(f"\n Total words: {total_words}")
    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(f"{word} → {count}")

# Run the tool
word_counter()
