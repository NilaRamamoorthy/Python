# Typing Speed Test

import time

# Sentence to type
sentence = "Python programming is fun and powerful."

# Function to calculate typing speed and accuracy
def typing_test():
    print("Typing Speed Test")
    print("\nType the following sentence:")
    print(f"\n\"{sentence}\"\n")

    input("Press Enter when you're ready to start...")

    start_time = time.time()
    typed = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    time_taken = round(time_taken, 2)

    # Split words
    original_words = sentence.split()
    typed_words = typed.split()

    # Count errors
    errors = 0
    for o, t in zip(original_words, typed_words):
        if o != t:
            errors += 1

    # Calculate speed (words per minute)
    word_count = len(typed_words)
    wpm = (word_count / time_taken) * 60
    wpm = round(wpm, 2)

    print("\n Time Taken:", time_taken, "seconds")
    print(" Words Per Minute:", wpm)
    print(" Errors:", errors)

# Run the test
typing_test()
