def deposit(account, amount):
    account["balance"] += amount
    return account

def withdraw(account, amount):
    if account["balance"] >= amount:
        account["balance"] -= amount
    return account
