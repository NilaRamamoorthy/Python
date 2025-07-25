class LazySquareIterator:
    def __init__(self, numbers):
        if numbers is None or not hasattr(numbers, '__iter__'):
            self._it = iter([])
        else:
            self._it = iter(numbers)

    def __iter__(self):
        return self

    def __next__(self):
        num = next(self._it)  # may raise StopIteration
        return num * num

# Valid input
nums = [2, 3, 5]
sq_iter = LazySquareIterator(nums)
print("Squares (valid):", list(sq_iter))
# Squares (valid): [4, 9, 25]

# Empty input should not error
empty_iter = LazySquareIterator([])
print("Squares (empty):", list(empty_iter))
# Squares (empty): []
