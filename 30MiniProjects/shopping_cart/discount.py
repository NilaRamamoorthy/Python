# discount.py

def apply_discount(total: float) -> float:
    if total > 50000:
        return total * 0.9  # 10% discount
    elif total > 20000:
        return total * 0.95  # 5% discount
    return total
