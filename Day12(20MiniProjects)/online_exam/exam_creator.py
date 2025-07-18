# exam_creator.py

exam_questions = {}  # { (question_id): {"question": str, "options": list, "answer": str, "topics": set([...]) } }

def add_question(qid, question, options, answer, topics):
    if qid in exam_questions:
        return "⚠️ Question ID already exists."
    exam_questions[qid] = {
        "question": question,
        "options": options,
        "answer": answer,
        "topics": set(topics)
    }
    return f"✅ Question {qid} added."

def display_question(qid):
    if qid in exam_questions:
        q = exam_questions[qid]
        opts = '\n'.join([f"{i+1}. {opt}" for i, opt in enumerate(q["options"])])
        return f"📝 Q: {q['question']}\n{opts}\nAnswer: {q['answer']}"
    return "❌ Question not found."

def list_topics():
    all_topics = set()
    for q in exam_questions.values():
        all_topics.update(q["topics"])
    return f"📚 Topics Covered: {', '.join(all_topics)}"

def display_all_questions():
    for qid in exam_questions:
        print(display_question(qid))
        print()
