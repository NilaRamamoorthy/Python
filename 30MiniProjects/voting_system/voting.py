candidates = {"Alice", "Bob", "Charlie"}
voters = set()
votes = {candidate: 0 for candidate in candidates}

def cast_vote(voter_id, candidate):
    if voter_id in voters:
        print("You have already voted.")
        return
    if candidate not in candidates:
        print("Invalid candidate.")
        return
    voters.add(voter_id)
    votes[candidate] += 1
    print(f"Vote cast for {candidate} by voter {voter_id}.")
