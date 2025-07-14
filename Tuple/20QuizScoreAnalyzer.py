# 20. Quiz Score Analyzer
quiz_scores = [
    (1, (8, 9, 7)),
    (2, (10, 6, 8))
]
for uid, scores in quiz_scores:
    print(f"User {uid} - Best: {max(scores)}, Worst: {min(scores)}")
    print("Last two attempts:", scores[-2:])
