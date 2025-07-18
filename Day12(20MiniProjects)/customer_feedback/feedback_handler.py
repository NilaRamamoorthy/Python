# feedback_handler.py

# Dictionary to hold feedback with (customer_id,) as key
feedback_db = {}

# Function to add feedback
def add_feedback(customer_id, name, message):
    key = (customer_id,)
    if key in feedback_db:
        print(f"Feedback already received from customer ID {customer_id}.\n")
        return

    keywords = extract_keywords(message)
    feedback_db[key] = {
        "name": name,
        "message": message,
        "keywords": keywords
    }
    print(f"Feedback from '{name}' added successfully.\n")

# Function to extract keywords from feedback (very basic for now)
def extract_keywords(message):
    words = message.lower().split()
    stopwords = {"the", "is", "in", "and", "to", "a", "of", "it", "was", "for", "with"}
    return set(word.strip(".,!?") for word in words if word not in stopwords)

# View feedback summary
def view_all_feedback():
    print("\nCustomer Feedback Summary:")
    for customer_id, data in feedback_db.items():
        print(f"Customer ID: {customer_id}")
        print(f"Name: {data['name']}")
        print(f"Message: {data['message']}")
        print(f"Keywords: {', '.join(data['keywords'])}\n")
