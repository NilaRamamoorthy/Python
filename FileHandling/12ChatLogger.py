import os
from datetime import datetime

def get_log_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"chat_log_{timestamp}.txt"

def write_log(filename, user, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {user}: {message}\n")

def delete_log(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("Log file deleted.")
    else:
        print("Log file not found.")

def main():
    filename = get_log_filename()
    print(f"Chat session started. Logs will be saved in {filename}")

    while True:
        user = input("Enter username (or 'admin' for admin options): ")
        if user.lower() == 'admin':
            choice = input("Do you want to delete the log? (yes/no): ").lower()
            if choice == 'yes':
                delete_log(filename)
                break
            else:
                continue
        message = input("Enter your message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Session ended.")
            break
        write_log(filename, user, message)
        print("Message logged.")

main()
