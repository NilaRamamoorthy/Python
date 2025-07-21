def show_stats(stats):
    total = stats['correct'] + stats['incorrect']
    print("\n--- Quiz Stats ---")
    print(f"Correct: {stats['correct']}")
    print(f"Incorrect: {stats['incorrect']}")
    print(f"Total Questions: {total}")
