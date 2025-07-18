# main.py

from exam_creator import add_question, display_question, list_topics, display_all_questions

# Adding questions
print(add_question((1,), "What is the capital of France?", ["Paris", "Berlin", "Rome"], "Paris", ["Geography"]))
print(add_question((2,), "What is 2 + 2?", ["3", "4", "5"], "4", ["Math"]))
print(add_question((3,), "Which gas do plants absorb?", ["Oxygen", "Carbon Dioxide", "Nitrogen"], "Carbon Dioxide", ["Biology"]))

# Display individual question
print("\n" + display_question((2,)))

# List all topics
print("\n" + list_topics())

# Show all questions
print("\nAll Questions:")
display_all_questions()
