group_members = {}

def add_member(name):
    if name not in group_members:
        group_members[name] = 0.0

def get_members():
    return group_members

def update_expense(name, amount):
    if name in group_members:
        group_members[name] += amount
