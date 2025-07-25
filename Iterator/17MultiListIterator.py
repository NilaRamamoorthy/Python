class MultiListIterator:
    def __init__(self, list1, list2):
        self.l1 = list1
        self.l2 = list2
        self.index = 0
        self.total = len(list1) + len(list2)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.l1):
            val = self.l1[self.index]
        elif self.index < self.total:
            val = self.l2[self.index - len(self.l1)]
        else:
            raise StopIteration
        self.index += 1
        return val

# Demo:
print("17. MultiList:", list(MultiListIterator([1,2,3], ['a','b'])))
# Output: [1, 2, 3, 'a', 'b']
