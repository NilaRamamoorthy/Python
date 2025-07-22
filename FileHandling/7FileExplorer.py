import os
from datetime import datetime

def get_file_metadata(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    report_lines = []
    files = os.listdir(folder_path)
    for file in files:
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            size_kb = os.path.getsize(full_path) / 1024
            created = datetime.fromtimestamp(os.path.getctime(full_path))
            modified = datetime.fromtimestamp(os.path.getmtime(full_path))

            line = (
                f"File: {file}\n"
                f"Size: {size_kb:.2f} KB\n"
                f"Created: {created}\n"
                f"Modified: {modified}\n"
                "-------------------------\n"
            )
            print(line)
            report_lines.append(line)

    # Save report
    with open("file_report.txt", "w") as report_file:
        report_file.writelines(report_lines)
    print("Report saved as 'file_report.txt'")

def main():
    folder_path = input("Enter the folder path to explore: ")
    get_file_metadata(folder_path)

main()
