# attendance_ops.py

from datetime import date

def mark_attendance(attendance_data, students_present, mark_date=None):
    """
    Marks attendance for a given date.
    - attendance_data: dict of date → set of present roll numbers
    - students_present: list/set of roll numbers present
    - mark_date: optional date string (defaults to today)
    """
    if not mark_date:
        mark_date = str(date.today())
    attendance_data[mark_date] = set(students_present)
    print(f"Attendance marked for {mark_date}.")


def view_attendance_by_date(attendance_data, students, query_date):
    print(f"Attendance for {query_date}:")
    present = attendance_data.get(query_date, set())
    if not present:
        print("No records found.")
    else:
        for roll, name in students:
            status = "Present" if roll in present else "Absent"
            print(f"{roll}. {name} - {status}")


def view_attendance_by_student(attendance_data, roll_no):
    print(f"Attendance record for student roll no: {roll_no}")
    for adate, present in attendance_data.items():
        status = "Present" if roll_no in present else "Absent"
        print(f"{adate}: {status}")


def get_absentees(all_students, present_students):
    """Returns set of absent roll numbers"""
    return all_students - present_students
