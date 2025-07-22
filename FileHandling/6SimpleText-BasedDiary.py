import os
from datetime import datetime

def get_filename(date_str=None):
    if date_str:
        return f"{date_str}.txt"
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        return f"{today}.txt"

def write_entry():
    filename = get_filename()
    entry = input("Write your diary entry:\n")
    with open(filename, 'a') as f:
        f.write(f"\n--- {datetime.now().strftime('%H:%M:%S')} ---\n")
        f.write(entry + "\n")
    print("Entry saved!")

def view_entry(date_str):
    filename = get_filename(date_str)
    try:
        with open(filename, 'r') as f:
            print(f"\nContents of {filename}:\n")
            print(f.read())
    except FileNotFoundError:
        print("No entry found for this date.")

def main():
    while True:
        print("\nDiary Menu:")
        print("1. Write Today's Entry")
        print("2. View Previous Entry")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            write_entry()
        elif choice == '2':
            date_str = input("Enter date (YYYY-MM-DD): ")
            view_entry(date_str)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

main()
