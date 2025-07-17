# Initial survey response IDs
responses = {"R001", "R002", "R003", "R004"}

# New responses to be added
new_responses = {"R005", "R006", "R007", "R003"}  # "R003" is duplicate

# Add new responses using update()
responses.update(new_responses)
print("Updated Responses:", responses)

# Invalid responses to remove
invalid_responses = {"R002", "R006", "R100"}  # "R100" is not in set

# Keep track of removed responses
removed = set()

# Remove using remove() and discard()
for resp in invalid_responses:
    if resp in responses:
        responses.remove(resp)
        removed.add(resp)
    else:
        responses.discard(resp)  # Safe discard if not present

print("Responses after cleanup:", responses)
print("Removed Invalid Responses:", removed)

# Test pop() for random removal (simulating corrupted data removal)
popped_response = responses.pop()
print("Randomly removed response:", popped_response)
print("Final Responses:", responses)
