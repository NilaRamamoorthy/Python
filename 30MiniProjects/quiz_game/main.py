from quiz import ask_question, show_result

def main():
    print("🎮 Welcome to the Quiz Game!")
    for _ in range(3):  # You can increase the number of questions
        ask_question()
    show_result()

if __name__ == "__main__":
    main()
