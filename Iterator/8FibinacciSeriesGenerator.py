class FibonacciIterator:
    def __init__(self, n_terms):
        self.n = n_terms
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

# Usage with for-loop
print("Fibonacci (for):", [x for x in FibonacciIterator(7)])
# Fibonacci (for): [0, 1, 1, 2, 3, 5, 8]

# Usage with manual next()
fib = FibonacciIterator(5)
print("Fibonacci (next):", end=" ")
try:
    while True:
        print(next(fib), end=" ")
except StopIteration:
    print("\nIteration complete.")
# Fibonacci (next): 0 1 1 2 3
