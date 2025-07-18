# Task 8 - split math operations and import selectively

# addition.py
def add(a, b):
    return a + b

# subtraction.py
def subtract(a, b):
    return a - b

# main.py (example usage)
from task_08_addition import add
from task_08_subtraction import subtract

print("Add:", add(3, 2))
print("Subtract:", subtract(5, 2))
