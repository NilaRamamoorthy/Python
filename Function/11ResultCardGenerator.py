def result_card(**subject_marks):
    # Lambda function to convert marks to grades
    grade_mapper = lambda mark: (
        "A" if mark >= 90 else
        "B" if mark >= 75 else
        "C" if mark >= 60 else
        "D" if mark >= 35 else
        "F"
    )

    print("\n--- Result Card ---")
    total = sum(subject_marks.values())
    average = total / len(subject_marks)
    grades = list(map(grade_mapper, subject_marks.values()))
    
    for subject, grade in zip(subject_marks.keys(), grades):
        print(f"{subject}: {subject_marks[subject]} → Grade {grade}")

    status = "PASS" if all(mark >= 35 for mark in subject_marks.values()) else "FAIL"
    print(f"\nTotal Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Status: {status}")
    return total, average, status

# Example Usage
result_card(Math=92, Science=81, English=75, History=65, Tamil=58)
