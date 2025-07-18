# poll_utils.py

# Set to track unique voters (using tuple IDs)
voted_voters = set()

# Dictionary to hold vote counts per option
poll_results = {
    "Option A": 0,
    "Option B": 0,
    "Option C": 0
}

def cast_vote(voter_id, choice):
    key = (voter_id,)
    if key in voted_voters:
        print(f"Voter ID {voter_id} has already voted.\n")
        return
    if choice not in poll_results:
        print(f"Invalid voting option: {choice}\n")
        return

    poll_results[choice] += 1
    voted_voters.add(key)
    print(f"Vote recorded for voter {voter_id} -> {choice}\n")

def show_results():
    print("📊 Poll Results:")
    for option, count in poll_results.items():
        print(f"{option}: {count} votes")
    print(f"\nTotal Voters: {len(voted_voters)}\n")
