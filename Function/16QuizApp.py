def quiz_app():
    score = 0

    def ask_question(question, options, correct):
        print("\n" + question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        answer = input("Enter your choice (1-4): ")
        return int(answer) == correct

    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "Kolkata", "Delhi", "Chennai"],
            "answer": 3
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["Python", "Java", "HTML", "All of the above"],
            "answer": 4
        },
        {
            "question": "How many continents are there?",
            "options": ["5", "6", "7", "8"],
            "answer": 3
        }
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"\nFinal Score: {score}/{len(questions)}")
    return score

# Run the Quiz
quiz_app()
