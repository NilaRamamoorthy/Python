class CountdownIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Demo with manual next():
cd = CountdownIterator(5)
print("18. Countdown:", end=" ")
while True:
    try:
        print(next(cd), end="...")
    except StopIteration:
        print("Done.")
        break
# Output: 5...4...3...2...1...Done.
