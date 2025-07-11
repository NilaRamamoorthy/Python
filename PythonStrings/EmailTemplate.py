# 2. Email Template Customizer
name=input("Enter your name: ").strip()
course=input("Enter course: ").strip()
duration=input("Enter duration in days: ").strip()
print("Dear {}, your {} course starts in {} days.".format(name,course,duration))
print(f"Dear {name}, your {course} course starts in {duration} days.")