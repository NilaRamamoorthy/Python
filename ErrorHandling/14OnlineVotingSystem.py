# Custom exception
class AlreadyVotedError(Exception):
    pass

def voting_system():
    has_voted = False

    try:
        print("Welcome to the Voting System")
        choice = input("Do you want to vote? (yes/no): ").strip().lower()

        if choice == 'yes':
            if has_voted:
                raise AlreadyVotedError("You have already voted!")
            print("Candidates: A, B, C")
            vote = input("Enter your vote (A/B/C): ").strip().upper()

            if vote not in ['A', 'B', 'C']:
                raise ValueError("Invalid candidate choice!")

            has_voted = True
            print(f"✅ Your vote for {vote} has been recorded.")

        elif choice == 'no':
            print("You chose not to vote.")

        else:
            raise ValueError("Input must be 'yes' or 'no'.")

    except AlreadyVotedError as ave:
        print(f"⛔ {ave}")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")
    finally:
        print("🙏 Thank you for participating in the voting process.")

# Run the voting system
voting_system()
