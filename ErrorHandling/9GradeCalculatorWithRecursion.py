# Custom Exception not required here, standard ValueError is used

valid_grades = []

def get_grade_input():
    try:
        grade = input("Enter student grade (0-100): ")
        grade = float(grade)
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        valid_grades.append(grade)
        print(f"✅ Grade accepted: {grade}")
    except ValueError as ve:
        print(f"❌ Invalid input: {ve}. Please try again.")
        get_grade_input()  # Recursive call until valid
    finally:
        print(f"📊 Total valid entries so far: {len(valid_grades)}")

# Main Execution
num_entries = 5
print(f"🎯 Enter {num_entries} grades:")

for _ in range(num_entries):
    get_grade_input()

# Final Output
print("\n📋 Final Grades:", valid_grades)
average = sum(valid_grades) / len(valid_grades)
print(f"🎯 Average Grade: {average:.2f}")
