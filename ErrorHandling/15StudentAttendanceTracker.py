# Custom exception
class AttendanceOverflowError(Exception):
    pass

# Constants
MAX_DAYS = 30
student_list = {
    "101": "Alice",
    "102": "Bob",
    "103": "Charlie",
    "104": "David",
    "105": "Eva"
}

# Log file for absentees and errors
log_file = "attendance_log.txt"

def track_attendance():
    print("📋 Student Attendance Tracker")
    with open(log_file, "w") as log:
        for roll in student_list:
            try:
                days = input(f"Enter attendance for {student_list[roll]} (Max {MAX_DAYS}): ")
                if not days.isdigit():
                    raise ValueError("Attendance must be a number.")
                
                days = int(days)

                if days > MAX_DAYS:
                    raise AttendanceOverflowError(f"{student_list[roll]}'s attendance exceeds maximum days.")
                
                if days == 0:
                    log.write(f"{student_list[roll]} (Roll: {roll}) was absent all days.\n")
                
                print(f"✅ Recorded: {student_list[roll]} - {days} days present")

            except AttendanceOverflowError as aoe:
                log.write(f"ERROR: {aoe}\n")
                print(f"⚠️ {aoe}")
            except Exception as e:
                log.write(f"ERROR: {student_list.get(roll, 'Unknown')} (Roll: {roll}) - {e}\n")
                print(f"⚠️ Unexpected Error: {e}")

    print("📝 Attendance processing complete. Check 'attendance_log.txt' for logs.")

# Run tracker
track_attendance()
