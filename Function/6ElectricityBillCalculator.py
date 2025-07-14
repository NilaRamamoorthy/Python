# Electricity Bill Calculator

def calculate_bill(*units):
    total_units = sum(units)
    
    if total_units <= 100:
        bill = total_units * 1.5
    elif total_units <= 300:
        bill = 100 * 1.5 + (total_units - 100) * 2.5
    else:
        bill = 100 * 1.5 + 200 * 2.5 + (total_units - 300) * 4

    return bill

# Lambda to add GST (18%)
add_gst = lambda amount: amount + (amount * 0.18)

# Example Usage
monthly_units = [120, 95, 150]  # User can change this
raw_bill = calculate_bill(*monthly_units)
final_bill = add_gst(raw_bill)

print(f"Units Consumed: {sum(monthly_units)}")
print(f"Bill before GST: ₹{raw_bill:.2f}")
print(f"Final Bill after GST: ₹{final_bill:.2f}")
