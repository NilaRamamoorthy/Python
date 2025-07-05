# Student Gradebook

# Step 1: Ask for student's name and three subject scores
name = input("Enter the student's name: ")
score1 = float(input("Enter score for Subject 1: "))
score2 = float(input("Enter score for Subject 2: "))
score3 = float(input("Enter score for Subject 3: "))

# Step 2: Store data in a dictionary
student = {
    "Name": name,
    "Subject 1": score1,
    "Subject 2": score2,
    "Subject 3": score3
}

# Step 3: Calculate average score
average = (score1 + score2 + score3) / 3

# Step 4: Display results using f-strings
print(f"\n--- Gradebook for {student['Name']} ---")
print(f"Subject 1: {student['Subject 1']}")
print(f"Subject 2: {student['Subject 2']}")
print(f"Subject 3: {student['Subject 3']}")
print(f"Average Score: {average}")

# Step 5: Show type of the average
print(f"Type of average: {type(average)}")
