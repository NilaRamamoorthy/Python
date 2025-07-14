# 18. College Course Manager
courses = [
    ('CS101', 'Python', (3, 'Dr. Smith')),
    ('CS102', 'Data Structures', (4, 'Dr. Smith')),
    ('CS103', 'Algorithms', (3, 'Dr. Lee'))
]
sorted_courses = sorted(courses, key=lambda x: x[2][0])
faculty_counts = {}
for cid, name, (credits, faculty) in courses:
    faculty_counts[faculty] = faculty_counts.get(faculty, 0) + 1
print("Courses sorted by credits:")
for c in sorted_courses:
    print(c)
print("Faculty course count:", faculty_counts)
