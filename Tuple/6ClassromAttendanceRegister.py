
# 6. Classroom Attendance Register
attendance = [
    ('2025-07-01', ('Alice', 'Bob')),
    ('2025-07-02', ('Alice', 'Charlie')),
    ('2025-07-03', ('Bob', 'Charlie'))
]
for date, students in attendance:
    print(f"{date}: {', '.join(students)}")
days_present = sum('Alice' in students for _, students in attendance)
print("Alice was present for", days_present, "days")
