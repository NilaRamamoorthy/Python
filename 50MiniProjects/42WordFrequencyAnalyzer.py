import os
import re
from collections import Counter
from typing import Generator, Tuple

class WordFrequencyAnalyzer:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.word_counts: Counter = Counter()

    def load_and_count(self) -> None:
        """Read the document, process text, and count word frequencies."""
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                text = file.read().lower()
        except Exception as e:
            raise IOError(f"Error reading file {self.filepath}: {e}")

        # Use regex to extract words, ignoring punctuation
        words = re.findall(r"\b\w+\b", text)
        self.word_counts = Counter(words)

    def top_words(self, n: int = 10) -> Generator[Tuple[str, int], None, None]:
        """
        Generator yielding top n words and their frequencies.
        """
        for word, count in self.word_counts.most_common(n):
            yield word, count

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    analyzer = WordFrequencyAnalyzer(path)
    try:
        analyzer.load_and_count()
    except Exception as e:
        print(f"[Error] {e}")
        exit(1)

    print(f"\nTop words in '{os.path.basename(path)}':")
    for word, freq in analyzer.top_words(10):
        print(f"{word}: {freq}")
