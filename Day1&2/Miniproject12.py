# Simple Quiz

# Step 1: Ask the user three questions
answer1 = input("What is the capital of India? ")
answer2 = int(input("What is 5 + 3? "))
answer3 = input("What is the color of the sky? ")

# Step 2: Store answers in a list
answers = [answer1, answer2, answer3]

# Step 3: Print each answer and its type
print("\nYour Answers:")
print(f"1. {answers[0]} (Type: {type(answers[0])})")
print(f"2. {answers[1]} (Type: {type(answers[1])})")
print(f"3. {answers[2]} (Type: {type(answers[2])})")
