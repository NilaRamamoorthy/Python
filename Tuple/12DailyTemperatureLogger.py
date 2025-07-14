# 12. Daily Temperature Logger
temps = [
    ('2025-07-01', (28, 35)),
    ('2025-07-02', (27, 36)),
    ('2025-07-03', (26, 34))
]
for date, (morning, evening) in temps:
    print(f"{date}: Morning {morning}°C, Evening {evening}°C")
highest_evening = max(t[1][1] for t in temps)
print("Highest evening temp:", highest_evening)
