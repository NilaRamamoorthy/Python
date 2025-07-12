# Dynamic Polling App

poll_question = ""
options = []
votes = []

# Set up poll
def setup_poll():
    global poll_question, options, votes
    poll_question = input("Enter your poll question: ").strip()
    num_options = int(input("How many options? (e.g., 2, 3, 4): "))
    for i in range(num_options):
        opt = input(f"Enter option {i+1}: ").strip()
        options.append(opt)
        votes.append(0)

# Vote
def vote():
    print(f"\n{poll_question}")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    try:
        choice = int(input("Enter option number to vote: "))
        if 1 <= choice <= len(votes):
            votes[choice - 1] += 1
            print(" Vote recorded.")
        else:
            print(" Invalid option.")
    except ValueError:
        print(" Please enter a number.")

# Show poll result
def show_results():
    print("\n Poll Results:")
    for i, option in enumerate(options):
        print(f"{option}: {votes[i]} vote(s)")

# Run poll app
def polling_app():
    setup_poll()
    while True:
        vote()
        again = input("Next voter? (yes/no): ").strip().lower()
        if again != "yes":
            break
    show_results()

# Start polling
polling_app()
