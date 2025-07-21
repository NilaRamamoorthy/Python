expenses = []  # List of dicts: amount, payer, participants (set), category
categories = set()

def add_expense(amount, payer, participants, category):
    expenses.append({
        "amount": amount,
        "payer": payer,
        "participants": set(participants),
        "category": category
    })
    categories.add(category)

def show_expenses():
    for e in expenses:
        print(f"{e['payer']} paid ₹{e['amount']} for {e['category']} shared by {', '.join(e['participants'])}")
