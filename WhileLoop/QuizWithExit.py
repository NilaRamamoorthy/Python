#19. Quiz with Exit Option
questions = [
    "What is the capital of India?",
    "What is 5 + 3?",
    "Which planet is known as the Red Planet?",
    "What is the square root of 16?",
    "Who wrote 'Ramayana'?"
]
key=0
while key<=len(questions):
    answer=input(f"{key+1}. {questions[key]} (type 'quit' to exit): ").strip().lower()
    key+=1
    if answer=="quit":
        print("You exited the quiz")
        break
else:
    print("Quiz complete")
print("Quiz complete")
