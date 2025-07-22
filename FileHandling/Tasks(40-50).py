# 41. Simple Logger with Timestamp
import datetime

def write_log(message):
    with open("app.log", "a") as file:
        timestamp = datetime.datetime.now()
        file.write(f"{timestamp}: {message}\n")

# Demo
write_log("Application started.")
write_log("User logged in.")

# 42. Directory Monitor Mock (New File Log)
def monitor_directory_mock(existing_files, new_snapshot):
    added_files = set(new_snapshot) - set(existing_files)
    with open("monitor.log", "a") as log:
        for file in added_files:
            log.write(f"{datetime.datetime.now()}: New file added - {file}\n")

# Demo
old_files = ["file1.txt", "file2.txt"]
new_files = ["file1.txt", "file2.txt", "file3.txt"]
monitor_directory_mock(old_files, new_files)

# 43. Track User Login
def track_login(username):
    with open("login_activity.log", "a") as file:
        file.write(f"{datetime.datetime.now()}: {username} logged in\n")

# Demo
track_login("nila123")

# 44. Program Execution Logger with Filtering
def log_step(step_type, message):
    with open("execution.log", "a") as log:
        log.write(f"{datetime.datetime.now()} [{step_type.upper()}]: {message}\n")

def read_logs_by_type(step_type):
    with open("execution.log", "r") as log:
        for line in log:
            if f"[{step_type.upper()}]" in line:
                print(line.strip())

# Demo
log_step("info", "Started processing")
log_step("error", "Null pointer exception")
print("Filtered ERROR logs:")
read_logs_by_type("error")

# 45. Rotate Logs Daily (Mock)
import os
def rotate_log_file(logfile="rotation.log"):
    today = datetime.date.today().isoformat()
    if os.path.exists(logfile):
        os.rename(logfile, f"{logfile}_{today}")

# Demo
with open("rotation.log", "w") as f:
    f.write("Dummy log\n")
rotate_log_file("rotation.log")

# ----------------------------
# 46. To-Do List App with .txt
def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")

def list_tasks():
    with open("todo.txt", "r") as file:
        print("To-Do List:")
        print(file.read())

# Demo
add_task("Buy groceries")
add_task("Call doctor")
list_tasks()

# 47. Merge Two Text Files
def merge_files(file1, file2, output):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(output, "w") as out:
        out.write(f1.read())
        out.write("\n")
        out.write(f2.read())

# Demo
with open("f1.txt", "w") as f: f.write("Hello from file1")
with open("f2.txt", "w") as f: f.write("Hello from file2")
merge_files("f1.txt", "f2.txt", "merged.txt")

# 48. Convert .txt to .pdf using fpdf
from fpdf import FPDF

def txt_to_pdf(txt_file, pdf_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open(txt_file, "r") as file:
        for line in file:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
    pdf.output(pdf_file)

# Demo
with open("sample.txt", "w") as f:
    f.write("This is line one.\nThis is line two.")
txt_to_pdf("sample.txt", "output.pdf")

# 49. File Difference Checker
def file_diff(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i, (a, b) in enumerate(zip(lines1, lines2), start=1):
            if a != b:
                print(f"Line {i} differs:\nFile1: {a}File2: {b}")

# Demo
with open("diff1.txt", "w") as f: f.write("Line1\nLine2\nLine3\n")
with open("diff2.txt", "w") as f: f.write("Line1\nLineX\nLine3\n")
file_diff("diff1.txt", "diff2.txt")

# 50. Daily Diary Entry by Date
def write_diary_entry(entry):
    filename = f"{datetime.date.today().isoformat()}.txt"
    with open(filename, "a") as file:
        file.write(entry + "\n")

# Demo
write_diary_entry("Today I learned about file handling and logging.")
