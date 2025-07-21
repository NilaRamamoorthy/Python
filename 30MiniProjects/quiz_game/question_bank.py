import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris",
        "topic": "Geography"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Chaucer", "Wordsworth", "Dickens"],
        "answer": "Shakespeare",
        "topic": "Literature"
    },
    {
        "question": "What is 7 x 6?",
        "options": ["42", "36", "48", "56"],
        "answer": "42",
        "topic": "Math"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Earth", "Jupiter"],
        "answer": "Mars",
        "topic": "Science"
    }
]

def get_random_question():
    return random.choice(questions)

def get_all_topics():
    return {q["topic"] for q in questions}
