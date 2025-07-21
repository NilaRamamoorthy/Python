# poll_ops.py

from typing import Dict, List, Set

# Structure: question → {"options": [...], "votes": {option: count}, "voted_users": set()}
polls: Dict[str, Dict] = {}

def create_poll(question: str, options: List[str]):
    if question in polls:
        print("Poll already exists.")
        return
    polls[question] = {
        "options": options,
        "votes": {opt: 0 for opt in options},
        "voted_users": set()
    }
    print("Poll created.")

def vote(question: str, option: str, username: str):
    if question not in polls:
        print("Poll not found.")
        return
    poll = polls[question]
    if username in poll["voted_users"]:
        print("User has already voted.")
        return
    if option not in poll["options"]:
        print("Invalid option.")
        return
    poll["votes"][option] += 1
    poll["voted_users"].add(username)
    print(f"{username} voted for '{option}'.")

def show_results(question: str):
    if question not in polls:
        print("Poll not found.")
        return
    print(f"Results for: {question}")
    for option, count in polls[question]["votes"].items():
        print(f"{option}: {count} votes")
