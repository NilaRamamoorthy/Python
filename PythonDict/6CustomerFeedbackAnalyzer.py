# Initial feedback data
feedbacks = {
    1: {"feedback": "positive", "rating": 5},
    2: {"feedback": "negative", "rating": 2},
    3: {"feedback": "positive", "rating": 4},
    4: {"feedback": "neutral", "rating": 3},
    5: {"feedback": "positive", "rating": 5}
}

# 1. Compute average rating
ratings = [info["rating"] for info in feedbacks.values()]
avg_rating = sum(ratings) / len(ratings)
print(f"Average Rating: {avg_rating:.2f}")

# 2. Count feedback types
summary = {}
for info in feedbacks.values():
    f_type = info["feedback"]
    summary[f_type] = summary.get(f_type, 0) + 1

print("\nFeedback Type Count:")
for f_type, count in summary.items():
    print(f"{f_type}: {count}")

# 3. Customers with rating > 4
high_rated = {cid: info for cid, info in feedbacks.items() if info["rating"] > 4}

print("\nHigh-Rated Customers:")
for cid, info in high_rated.items():
    print(f"Customer {cid}: Rating {info['rating']}")
