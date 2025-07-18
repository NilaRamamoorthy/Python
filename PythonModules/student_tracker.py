from student_tracker.students import add_student
from student_tracker.courses import add_course, enroll_student
from student_tracker.progress import view_student_progress

def main():
    while True:
        print("\nStudent Course Tracker")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. View Student Progress")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            add_student(sid, name)
        elif choice == "2":
            cid = input("Course ID: ")
            cname = input("Course Name: ")
            add_course(cid, cname)
        elif choice == "3":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            enroll_student(sid, cid)
        elif choice == "4":
            sid = input("Student ID: ")
            view_student_progress(sid)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
