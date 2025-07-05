marks = []
for i in range(5):
    score = int(input(f"Enter mark {i+1}: "))
    marks.append(score)

maximum = marks[0]
minimum = marks[0]
total = 0

for mark in marks:
    if mark > maximum:
        maximum = mark
    if mark < minimum:
        minimum = mark
    total += mark

average = total / 5
print("Highest:", maximum)
print("Lowest:", minimum)
print("Average:", average)
