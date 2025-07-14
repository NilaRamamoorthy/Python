# 14. Exam Result Processing
results = [
    ('Alice', (85, 90, 78)),
    ('Bob', (75, 80, 88))
]
for name, scores in results:
    total = sum(scores)
    avg = total / len(scores)
    print(f"{name}: Total={total}, Average={avg:.2f}")
