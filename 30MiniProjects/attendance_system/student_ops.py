# student_ops.py

def load_students():
    """Returns a list of student tuples: (roll_no, name)"""
    return [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (4, "Diana"),
        (5, "Ethan")
    ]


def get_all_roll_numbers(students):
    """Returns a set of all roll numbers from student list"""
    return set(roll for roll, _ in students)


def display_students(students):
    print("Student List:")
    for roll, name in students:
        print(f"{roll}. {name}")
