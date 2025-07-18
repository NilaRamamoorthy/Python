# main.py

from poll_utils import cast_vote, show_results

# Voters cast their votes
cast_vote(1001, "Option A")
cast_vote(1002, "Option B")
cast_vote(1003, "Option A")
cast_vote(1001, "Option C")  # Duplicate vote
cast_vote(1004, "Option Z")  # Invalid option

# Show results
show_results()
