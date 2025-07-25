class EvenIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            if val % 2 == 0:
                return val
        raise StopIteration

class OddIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            if val % 2 != 0:
                return val
        raise StopIteration

data = [1, 2, 3, 4, 5, 6]
print("Even:", list(EvenIterator(data)))
print("Odd: ", list(OddIterator(data)))
# Even: [2, 4, 6]
# Odd:  [1, 3, 5]
