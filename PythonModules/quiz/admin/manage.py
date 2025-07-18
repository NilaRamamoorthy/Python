import json

def add_question():
    question = input("Enter question: ")
    options = [input(f"Option {i+1}: ") for i in range(4)]
    answer = input("Enter correct option text: ")

    q = {
        "question": question,
        "options": options,
        "answer": answer
    }

    try:
        with open("quiz/questions.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(q)

    with open("quiz/questions.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Question added successfully.")
