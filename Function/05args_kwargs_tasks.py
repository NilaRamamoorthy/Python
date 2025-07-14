# Task 26: Sum of all *args
def add_numbers(*args):
    return sum(args)
print(add_numbers(10, 20, 30, 40))
print("-"*40)

# Task 27: Print all positional arguments
def print_args(*args):
    print("Positional arguments received:")
    for i, arg in enumerate(args, 1):
        print(f"{i}. {arg}")
print_args("apple", "banana", "cherry")
print("-"*40)

# Task 28: Print student data using **kwargs
def student_info(**kwargs):
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
student_info(name="Anjali", age=20, grade="A")
print("-"*40)

# Task 29: Combine *args and **kwargs
def display_all(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)
display_all(1, 2, 3, name="Ravi", score=95)
print("-"*40)

# Task 30: Filter keyword arguments with integer values
def filter_integers(**kwargs):
    int_values = {k: v for k, v in kwargs.items() if isinstance(v, int)}
    return int_values
filtered = filter_integers(name="Raj", age=25, marks=88, grade="A")
print("Filtered Integers:", filtered)
print("-"*40)