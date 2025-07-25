import re

def word_speaker(filepath):
    """Generator yielding one clean word at a time from a file."""
    word_pattern = re.compile(r'\b\w+\b')
    with open(filepath, 'r') as f:
        for line in f:  # file object is its own iterator :contentReference[oaicite:4]{index=4}
            for match in word_pattern.finditer(line):
                yield match.group()

# Usage:
# Assuming 'paragraph.txt' exists with some text
for word in word_speaker('paragraph.txt'):
    print(word)
