class SkipAlternateIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 2
        return val

# Demo:
print("12 skip even-indexed items:", list(SkipAlternateIterator([10,20,30,40,50,60])))
# Output: [10, 30, 50]
