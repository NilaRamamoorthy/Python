# Initial data
expenses = {
    "2025-07-14": {"food": 200, "transport": 100, "misc": 50},
    "2025-07-15": {"food": 250, "transport": 80, "misc": 70},
    "2025-07-16": {"food": 180, "transport": 120, "misc": 60}
}

# 1. Daily total
print("Daily Totals:")
for date, items in expenses.items():
    total = sum(items.values())
    print(f"{date}: ₹{total}")

# 2. Monthly total
monthly_total = sum(sum(items.values()) for items in expenses.values())
print(f"\nMonthly Total: ₹{monthly_total}")

# 3. Filter highest spending days
daily_totals = {date: sum(items.values()) for date, items in expenses.items()}
max_spent = max(daily_totals.values())
high_spending_days = [date for date, total in daily_totals.items() if total == max_spent]
print("\nHighest Spending Day(s):", high_spending_days)

# 4. Copy structure to new month
august_expenses = expenses.copy()
august_expenses.update({"2025-08-01": {"food": 0, "transport": 0, "misc": 0}})

# 5. Days with food > 200
high_food_days = {date: data["food"] for date, data in expenses.items() if data["food"] > 200}
print("\nDays with food expense > 200:")
for date, amt in high_food_days.items():
    print(f"{date}: ₹{amt}")
