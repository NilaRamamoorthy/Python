from quiz.user.play import start_quiz
from quiz.admin.manage import add_question

def main():
    print("Welcome to the Quiz System")
    role = input("Are you an (A)dmin or (U)ser? ").strip().lower()

    if role == 'a':
        add_question()
    elif role == 'u':
        start_quiz()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
