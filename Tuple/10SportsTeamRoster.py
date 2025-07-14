# 10. Sports Team Roster
team = [
    (1, 'Ravi', ('striker', 12)),
    (2, 'Amit', ('goalkeeper', 2)),
    (3, 'Raj', ('striker', 8))
]
for pid, name, (position, goals) in team:
    if goals > 10:
        print(f"{name} has scored more than 10 goals.")
striker_count = sum(1 for _, _, (pos, _) in team if pos == 'striker')
print("Number of strikers:", striker_count)

