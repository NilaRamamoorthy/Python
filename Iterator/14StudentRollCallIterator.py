class RollCallIterator:
    def __init__(self, roll_dict):
        self.items = list(roll_dict.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        pair = self.items[self.index]
        self.index += 1
        return pair

# Demo:
students = {101: "Alice", 102: "Bob", 103: "Charlie"}
print("14 roll call:")
for roll, name in RollCallIterator(students):
    print(f" Roll: {roll} → Name: {name}")
# Output:
#  Roll: 101 → Name: Alice
#  Roll: 102 → Name: Bob
#  Roll: 103 → Name: Charlie
