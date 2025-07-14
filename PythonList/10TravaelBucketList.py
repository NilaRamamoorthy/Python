# Travel Bucket List

# Initial list of places
bucket_list = ["Paris", "Tokyo", "New York"]

# Display current list
print("Travel Bucket List:")
for place in bucket_list:
    print(place)

# Add a new place
bucket_list.append("Sydney")
print("\nAfter adding Sydney:")
print(bucket_list)

# Remove a place
bucket_list.remove("Tokyo")
print("\nAfter removing Tokyo:")
print(bucket_list)

# Update a place (change 'Paris' to 'Rome')
for i in range(len(bucket_list)):
    if bucket_list[i] == "Paris":
        bucket_list[i] = "Rome"
print("\nAfter updating Paris to Rome:")
print(bucket_list)

# Check if a place is already in the list
check_place = "Rome"
if check_place in bucket_list:
    print(f"\nYes, {check_place} is already in your bucket list!")
else:
    print(f"\nNo, {check_place} is not in your list.")
