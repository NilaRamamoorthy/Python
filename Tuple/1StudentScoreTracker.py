# 1. Student Score Tracker
students = [
    ('Alice', (85, 90, 78)),
    ('Bob', (70, 88, 82)),
    ('Charlie', (92, 75, 80))
]
for name, scores in students:
    avg = sum(scores) / len(scores)
    print(f"{name}: Math={scores[0]}, Physics={scores[1]}, Chemistry={scores[2]}, Average={avg:.2f}")
