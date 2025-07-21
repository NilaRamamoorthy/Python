from student_ops import add_student, update_grades
from report_gen import display_all_reports, top_performers

def main():
    while True:
        print("\n1. Add Student\n2. Update Grades\n3. Show Reports\n4. Top Performers\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            update_grades()
        elif choice == "3":
            display_all_reports()
        elif choice == "4":
            top_performers()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
