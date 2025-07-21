def display_results(votes):
    print("\n--- Voting Results ---")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
    
    max_votes = max(votes.values())
    winners = [c for c, v in votes.items() if v == max_votes]
    
    if len(winners) > 1:
        print("It's a tie between:", ", ".join(winners))
    else:
        print(f"Winner: {winners[0]}")
