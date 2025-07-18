# main.py

from feedback_handler import add_feedback, view_all_feedback

# Add feedbacks
add_feedback(501, "Alice", "The service was excellent and the staff was helpful.")
add_feedback(502, "Bob", "I had a bad experience with the delivery.")
add_feedback(501, "Alice", "Trying to send feedback again.")  # Duplicate

# View all feedback
view_all_feedback()
