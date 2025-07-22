# Online Exam Portal

from abc import ABC, abstractmethod

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class Student(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.__scores = {}

    def appear_exam(self, exam):
        print(f"\n{self.name} is taking the {exam.exam_name}")
        score = 0
        for question in exam.questions:
            print(question.text)
            for idx, opt in enumerate(question.options, 1):
                print(f"{idx}. {opt}")
            answer = int(input("Enter option number: "))
            if question.check_answer(answer):
                score += 1
        self.__scores[exam.exam_name] = score
        print(f"{self.name}'s score in {exam.exam_name}: {score}/{len(exam.questions)}")

    def show_result(self):
        print(f"\nResult for {self.name}:")
        for exam, score in self.__scores.items():
            print(f"{exam}: {score} marks")

class Admin(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)

    def create_exam(self, name):
        return Exam(name)

    def add_question(self, exam, question):
        exam.add_question(question)

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.__correct_option = correct_option  # private

    def check_answer(self, selected):
        return selected == self.__correct_option

class Exam:
    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)


# Sample usage
if __name__ == "__main__":
    # Admin creating an exam
    admin = Admin("Prof. Ravi", "ADM001")
    math_exam = admin.create_exam("Math Test")

    # Adding questions
    q1 = Question("What is 2 + 2?", ["3", "4", "5", "6"], 2)
    q2 = Question("What is 5 * 3?", ["15", "20", "10", "5"], 1)
    admin.add_question(math_exam, q1)
    admin.add_question(math_exam, q2)

    # Student appearing for exam
    student = Student("Ananya", "STU101")
    # Note: Requires manual input to answer questions
    student.appear_exam(math_exam)
    student.show_result()
