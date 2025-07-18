def apply_discount(total):
    if total > 500:
        print("Applying ₹50 discount.")
        return total - 50
    return total

def apply_tax(amount):
    tax = amount * 0.05
    return amount + tax
