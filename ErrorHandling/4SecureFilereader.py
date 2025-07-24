import os
import logging

# Setup logging
logging.basicConfig(filename="file_reader_errors.log", level=logging.ERROR, format='%(asctime)s - %(message)s')

def secure_file_reader(filename):
    file = None
    try:
        try:
            # Attempt to open file
            file = open(filename, "r")

            # Check read permissions manually (optional enhancement)
            if not os.access(filename, os.R_OK):
                raise PermissionError("You do not have read access to this file.")

            # Attempt to read file
            content = file.read()
            print("📄 File Content:\n", content)

        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
            print("❌ Error: File not found.")

        except PermissionError as e:
            logging.error(f"Permission error: {e}")
            print("❌ Error:", e)

        except Exception as e:
            logging.error(f"Unknown file read error: {e}")
            print("❌ An unexpected error occurred:", e)

    finally:
        if file:
            file.close()
            print("🔐 File closed.")
        else:
            print("ℹ️ File was never opened.")

# Sample Usage
# Make sure the file "example.txt" exists or change the filename
secure_file_reader("example.txt")
# secure_file_reader("nonexistent.txt")  # Uncomment to test
