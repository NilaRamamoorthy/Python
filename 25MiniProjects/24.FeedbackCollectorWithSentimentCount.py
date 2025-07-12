# Feedback Collector with Sentiment Count

# Function to collect and analyze feedback
def collect_feedback():
    print("Feedback Collector with Sentiment Count")
    print("Type 'done' to finish collecting feedback.\n")

    feedback_list = []

    while True:
        feedback = input("Enter feedback: ").strip()
        if feedback.lower() == "done":
            break
        feedback_list.append(feedback)

    # Initialize sentiment counts
    good_count = 0
    bad_count = 0
    average_count = 0

    for fb in feedback_list:
        fb_lower = fb.lower()
        if "good" in fb_lower:
            good_count += 1
        elif "bad" in fb_lower:
            bad_count += 1
        elif "average" in fb_lower:
            average_count += 1

    # Show results
    print("\n Sentiment Summary:")
    print(f"Total Feedbacks: {len(feedback_list)}")
    print(f" Good: {good_count}")
    print(f" Bad: {bad_count}")
    print(f" Average: {average_count}")

# Run the tool
collect_feedback()
