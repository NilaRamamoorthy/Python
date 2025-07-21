def calculate_balances(expenses):
    balances = {}
    for exp in expenses:
        split_amount = exp['amount'] / len(exp['participants'])
        for person in exp['participants']:
            balances[person] = balances.get(person, 0) - split_amount
        balances[exp['payer']] = balances.get(exp['payer'], 0) + exp['amount']
    return balances

def show_balances(balances):
    print("\n--- Final Balances ---")
    for person, amount in balances.items():
        print(f"{person}: ₹{amount:.2f}")
