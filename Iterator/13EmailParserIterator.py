import re

class EmailParserIterator:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0
        self.pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.lines):
            candidate = self.lines[self.index].strip()
            self.index += 1
            if self.pattern.match(candidate):
                return candidate
        raise StopIteration

# Demo:
emails = ["valid@example.com", "bad@", "user@domain.org", "nope.com"]
print("13 valid emails:", list(EmailParserIterator(emails)))
# Output: ['valid@example.com', 'user@domain.org']
