# List of valid candidates
candidates = ["Alice", "Bob", "Charlie"]

# Incoming vote list (some may be invalid)
votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "David", "Eve"]

# 1. Count votes
vote_count = {}
invalid_votes = 0

for name in votes:
    if name in candidates:
        vote_count[name] = vote_count.get(name, 0) + 1
    else:
        invalid_votes += 1

# 2. Display vote count
print("Vote Count:")
for name, count in vote_count.items():
    print(f"{name}: {count} vote(s)")

# 3. Find winner
if vote_count:
    winner = max(vote_count, key=vote_count.get)
    print(f"\nWinner: {winner} with {vote_count[winner]} votes")
else:
    print("\nNo valid votes were cast.")

# 4. Invalid vote count
print(f"\nInvalid votes: {invalid_votes}")
