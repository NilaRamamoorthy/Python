import re

class CapitalizedWordIterator:
    def __init__(self, text):
        # Accept multi-line input and process into words
        # Splitting on whitespace handles lines and spaces
        self.words = text.split()
        self.index = 0
        # Pattern: word starting with uppercase letter followed by lowercase or uppercase letters
        self.pattern = re.compile(r'^[A-Z][A-Za-z]*$')

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.words):
            w = self.words[self.index]
            self.index += 1
            if self.pattern.match(w):
                return w
        # No more valid words
        raise StopIteration

# Demo with inline output
paragraph = """Hello world
this is a Test of Capitalized Words
Python and GPT are Here"""

print("Capitalized words:")
for w in CapitalizedWordIterator(paragraph):
    print(w)
