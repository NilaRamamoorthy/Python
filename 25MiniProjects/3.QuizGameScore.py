# Quiz Game with Score Tracking

questions = [
    {"question": "1. What is the capital of India?", "answer": "delhi"},
    {"question": "2. What language is used for web development?", "answer": "html"},
    {"question": "3. Who wrote the Harry Potter series?", "answer": "jk rowling"},
    {"question": "4. What is 5 + 7?", "answer": "12"},
    {"question": "5. What color is a banana?", "answer": "yellow"}
]

score = 0

# Function to ask each question
def ask_question(q, correct_answer):
    global score
    user_answer = input(q + "\nYour answer: ").strip().lower()
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")

# Function to calculate and show results
def show_result():
    percentage = (score / len(questions)) * 100
    print(f"\n You scored {score} out of {len(questions)}")
    print(f"Percentage: {percentage:.2f}%")

# Main quiz function
def start_quiz():
    print("Welcome to the Quiz Game!")
    print("----------------------------")
    for q in questions:
        ask_question(q["question"], q["answer"])
    show_result()

# Start the game
start_quiz()
