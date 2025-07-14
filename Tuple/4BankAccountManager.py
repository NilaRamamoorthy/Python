
# 4. Bank Account Manager
accounts = [
    (101, 'Alice', (5000.0, 'active')),
    (102, 'Bob', (3000.0, 'inactive'))
]
for acc_no, name, (balance, status) in accounts:
    print(f"Account: {acc_no}, Name: {name}, Balance: {balance}, Status: {status}")

