from voting import cast_vote, votes
from tally import display_results

# Simulate voting
cast_vote("V001", "Alice")
cast_vote("V002", "Bob")
cast_vote("V003", "Alice")
cast_vote("V001", "Charlie")  # Already voted
cast_vote("V004", "Charlie")

# Show results
display_results(votes)
