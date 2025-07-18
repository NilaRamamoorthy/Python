from decimal import Decimal, ROUND_HALF_UP
from expensesplitter.members import get_members

def split_expenses():
    members = get_members()
    total = sum(members.values())
    num_people = len(members)
    share = Decimal(total / num_people).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    balances = {}
    for name, spent in members.items():
        balances[name] = Decimal(spent).quantize(Decimal("0.01")) - share
    return balances
