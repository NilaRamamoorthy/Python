class DigitIterator:
    def __init__(self, s):
        self.s = s
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.s):
            ch = self.s[self.index]
            self.index += 1
            if ch.isdigit():
                return ch
        # When none left:
        raise StopIteration

# Usage:
mixed = "abc123def456"
print("Digits:", ", ".join(DigitIterator(mixed)))
# Digits: 1, 2, 3, 4, 5, 6
