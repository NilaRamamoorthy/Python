class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # Return a fresh iterator instance for reuse
        return MyRangeIterator(self.start, self.end)


class MyRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# Usage and outputs:
r = MyRange(1, 5)
print("MyRange first iteration:", list(r))   # [1, 2, 3, 4]
print("MyRange second iteration:", list(r))  # [1, 2, 3, 4] (reusable)
