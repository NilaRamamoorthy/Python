from accounts import users

def deposit(username, amount):
    users[username]["balance"] += amount
    users[username]["transactions"].append(("deposit", amount))
    print(f"✅ Deposited ₹{amount:.2f} to {username}")

def withdraw(username, amount):
    if users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        users[username]["transactions"].append(("withdraw", amount))
        print(f"✅ Withdrawn ₹{amount:.2f} from {username}")
    else:
        print("❌ Insufficient funds.")

def view_balance(username):
    print(f"💰 Current Balance: ₹{users[username]['balance']:.2f}")

def view_statement(username):
    print(f"\n📄 Transaction History for {username}:")
    for t_type, amt in users[username]["transactions"]:
        print(f"- {t_type.capitalize()}: ₹{amt:.2f}")

def show_transaction_types(username):
    tx_types = {t[0] for t in users[username]["transactions"]}
    print("🔁 Unique Transaction Types:", tx_types)
