import os
from datetime import datetime

LOG_DIR = "logs"
MAX_ENTRIES = 10

def write_log(message):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"log_{today}.txt")
    
    # Read current log to count entries
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            lines = f.readlines()
    else:
        lines = []

    # Rotate log if more than MAX_ENTRIES
    if len(lines) >= MAX_ENTRIES:
        timestamp = datetime.now().strftime("%H-%M-%S")
        archive_file = os.path.join(LOG_DIR, f"log_{today}_{timestamp}.txt")
        os.rename(log_file, archive_file)
        lines = []  # Reset

    # Append log entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"

    with open(log_file, 'a') as f:
        f.write(entry)
    print("Log written.")

# Demo
write_log("Function executed successfully.")
