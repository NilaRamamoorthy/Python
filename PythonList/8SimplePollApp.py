# Simple Poll App

# List to store responses
responses = []

print("Welcome to the Poll: Do you like Python? (Yes/No)")

# Collect responses from multiple users
for i in range(5):
    response = input(f"User {i+1} response: ").strip().capitalize()
    if response in ["Yes", "No"]:
        responses.append(response)
    else:
        print(" Invalid input. Please answer with 'Yes' or 'No'.")

# Show poll results
print("\nPoll Results:")
print("Yes Votes:", responses.count("Yes"))
print("No Votes:", responses.count("No"))

# Remove any incorrect input (if any slipped through)
valid_responses = ["Yes", "No"]
cleaned_responses = [r for r in responses if r in valid_responses]

print("\n Cleaned Responses:", cleaned_responses)
