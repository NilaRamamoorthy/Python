# Word Analyzer Tool

def analyze_words(*words):
    # Convert words to uppercase using lambda + map
    uppercase_words = list(map(lambda w: w.upper(), words))
    print("Uppercase Words:", uppercase_words)

    # Word lengths using map()
    lengths = list(map(len, words))
    print("Word Lengths:", lengths)

    # Most frequent character in each word
    print("Most Frequent Characters:")
    for word in words:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        most_frequent = max(freq, key=freq.get)
        print(f"'{word}' -> '{most_frequent}'")

# Example usage
analyze_words("hello", "banana", "programming", "python")
