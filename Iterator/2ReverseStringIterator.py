class ReverseStringIterator:
    def __init__(self, s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        if len(s) == 0:
            raise ValueError("Cannot iterate empty string in reverse")
        self.s = s
        self.index = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        ch = self.s[self.index]
        self.index -= 1
        return ch

# Usage:
rev = ReverseStringIterator("hello")
print("ReverseStringIterator:", "".join(rev))  # 'olleh'

# Empty string example:
try:
    rev_empty = ReverseStringIterator("")
except ValueError as e:
    print("Error:", e)
# Error: Cannot iterate empty string in reverse
