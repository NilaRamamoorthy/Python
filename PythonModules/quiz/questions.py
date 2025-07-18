import json

def load_questions(file_path='quiz/questions.json'):
    with open(file_path, 'r') as file:
        return json.load(file)
