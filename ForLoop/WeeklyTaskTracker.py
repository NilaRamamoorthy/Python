tasks = ["Buy groceries", "Meeting", "Gym", "Coding", "Reading", "Cleaning", "Rest"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day, task in zip(days, tasks):
    print(f"{day}: {task}")
