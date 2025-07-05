names = input("Enter student names (comma separated): ").split(',')
present_count = 0
for name in names:
    status = input(f"Is {name.strip()} present? (P/A): ").upper()
    if status == 'P':
        present_count += 1

print(f"Total Present: {present_count}")