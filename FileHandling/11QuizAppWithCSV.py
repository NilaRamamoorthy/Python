import csv
from datetime import datetime
import os

def load_questions(filename):
    questions = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    questions.append((row[0], row[1]))
    except FileNotFoundError:
        print("Question file not found.")
    return questions

def save_result(name, score, total, result_file):
    header_needed = not os.path.exists(result_file)
    with open(result_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if header_needed:
            writer.writerow(["Name", "Score", "Total", "Timestamp"])
        writer.writerow([name, score, total, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def conduct_quiz(questions):
    score = 0
    for q, a in questions:
        user_ans = input(f"{q} ").strip()
        if user_ans.lower() == a.lower():
            score += 1
    return score

def main():
    name = input("Enter your name: ")
    questions = load_questions('questions.csv')
    if not questions:
        return
    print(f"Starting quiz with {len(questions)} questions...\n")
    score = conduct_quiz(questions)
    print(f"\n{name}, your score is {score}/{len(questions)}")
    save_result(name, score, len(questions), 'quiz_results.csv')

main()
