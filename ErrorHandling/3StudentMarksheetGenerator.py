import logging

# Setup logging
logging.basicConfig(filename="marksheet_errors.log", level=logging.ERROR, format='%(asctime)s - %(message)s')

# Custom Exception
class InvalidMarkError(Exception):
    pass

def calculate_grade(marks):
    average = sum(marks.values()) / len(marks)
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def process_student(name, marks):
    try:
        # Check all marks are within valid range
        for subject, mark in marks.items():
            if mark < 0:
                raise ValueError(f"Negative mark found in {subject}.")
            if mark > 100:
                raise InvalidMarkError(f"Mark greater than 100 in {subject}.")

    except (ValueError, InvalidMarkError) as e:
        logging.error(f"Student: {name} - {e}")
        print(f"❌ Error processing {name}: {e}")
    
    else:
        grade = calculate_grade(marks)
        print(f"✅ {name}'s Grade: {grade}")
    
    finally:
        print(f"Finished processing {name}.\n")

# Sample student data
students = [
    ("Alice", {"Math": 85, "Science": 90, "English": 78}),
    ("Bob", {"Math": 105, "Science": 88, "English": 76}),     # Invalid mark
    ("Charlie", {"Math": 70, "Science": -10, "English": 65}), # Negative mark
    ("Diana", {"Math": 92, "Science": 95, "English": 89}),
]

# Process each student
for name, marks in students:
    process_student(name, marks)
