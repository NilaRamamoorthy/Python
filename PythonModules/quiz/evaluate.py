def evaluate_answers(questions, answers):
    score = 0
    for q, user_ans in zip(questions, answers):
        if q['answer'].lower() == user_ans.lower():
            score += 1
    return score
