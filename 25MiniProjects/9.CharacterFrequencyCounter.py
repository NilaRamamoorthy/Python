# Character Frequency Counter

# Function to count character frequency
def char_frequency(text):
    freq = {}
    for char in text:
        if char != " ":  
            freq[char] = freq.get(char, 0) + 1
    return freq

# Main logic
def main():
    sentence = input("Enter a sentence: ").strip()
    frequency = char_frequency(sentence)
    
    print("\nCharacter Frequency:")
    for char, count in frequency.items():
        print(f"'{char}': {count} time(s)")

# Run the app
main()
