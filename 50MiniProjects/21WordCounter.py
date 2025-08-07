
import os
import time
from collections import Counter
from functools import wraps

# Decorator to measure execution time
def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper

class WordCounter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.word_freq = Counter()
        self.line_count = 0
        self.char_count = 0

    def read_file(self):
        """Reads the file and processes its content."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                self.line_count += 1
                self.char_count += len(line)
                self.process_line(line)

    def process_line(self, line):
        """Processes each line to update word frequencies."""
        words = line.split()
        self.word_freq.update(words)

    def count_words(self):
        """Returns the total number of words."""
        return sum(self.word_freq.values())

    def most_common_word(self):
        """Returns the most common word and its frequency."""
        if not self.word_freq:
            return None, 0
        return self.word_freq.most_common(1)[0]

    def word_generator(self):
        """Yields words one by one."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                for word in line.split():
                    yield word

    def display_statistics(self):
        """Displays the statistics of the file."""
        print(f"Total Lines: {self.line_count}")
        print(f"Total Characters: {self.char_count}")
        print(f"Total Words: {self.count_words()}")
        most_common, freq = self.most_common_word()
        if most_common:
            print(f"Most Common Word: '{most_common}' with {freq} occurrences")
        else:
            print("No words found.")

# Example usage
if __name__ == "__main__":
    file_path = 'sample.txt'  # Replace with your file path
    word_counter = WordCounter(file_path)

    try:
        word_counter.read_file()
        word_counter.display_statistics()

        print("\nWords in the file:")
        for word in word_counter.word_generator():
            print(word)

    except FileNotFoundError as e:
        print(e)
