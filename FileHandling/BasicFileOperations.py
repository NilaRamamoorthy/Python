#     Basic File Operations (1–10)
# Create a new text file and write a welcome message.
with open("example.txt","w") as file:
    content=file.write("Welcome") 

# Open a file, write multiple lines, and close it manually.
file=open("example2.txt","a")
file.write("\n First Line")
file.write("\n Second Line")
file.write("\n Third Line")
file.write("\n Fourth Line")
file.close()

# Use the with statement to read a file without manually closing it.

with open("example2.txt", "r") as file:
    content=file.read()
    print(content)

# Read the contents of a file using .read().
file=open("example.txt","r")
content=file.read()
print(content)

# Read a file line-by-line using .readline().
with open("example2.txt", "r") as file:
    line1=file.readline()
    line2=file.readline()
    line3=file.readline()
    line4=file.readline()
print(line1.strip())
print(line2.strip())
print(line3.strip())
print(line4.strip())

# Read all lines of a file into a list using .readlines().
with open("example2.txt", "r") as file:
   print(file.readlines())


# Write a function that takes user input and appends it to a file.
user_input=input("Enter your ideas: ").strip()
with open("example.txt","a") as file:
    file.write("\n"+user_input)


# Write and overwrite a file using 'w' mode.

with open("example3.txt","w") as file:
    file.write("This is the first sentence")
with open("example3.txt","w") as file:  
    file.write("This is overwritten")

# Append data to a file using 'a' mode and then display the full content.

with open("example4.txt","a") as file:
    file.write("Append the data")
with open("example4.txt","r") as file:
    print(file.read())


# Use 'x' mode to create a file, and handle the error if it already exists.

with open("example.txt","x") as file:
    pass


# Working with Context Managers & Modes (11–20)

# Rewrite a script using with to ensure file auto-closing.

with open("sample.txt", "w") as file:
    file.write("Hello World")
    print("File written and automatically closed.")

# Demonstrate reading and writing a binary file using 'wb' and 'rb'.
# Writing binary data to a file
data = b"This is binary data.\nSecond line in binary."
with open("binary_file.bin", "wb") as binary_write:
    binary_write.write(data)
    print("Binary data written to binary_file.bin")

# Reading binary data from the file
with open("binary_file.bin", "rb") as binary_read:
    content = binary_read.read()
    print("Binary data read from file:")
    print(content)

# Build a file reader that checks if a file is readable or writable.

def check_file_access(file_name, mode):
    try:
        with open(file_name, mode) as f:
            print(f"File '{file_name}' opened in mode '{mode}'")
            print("Readable:", f.readable())
            print("Writable:", f.writable())
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print("Error:", e)

# Sample usage
# Create a test file first
with open("test_access.txt", "w") as f:
    f.write("Checking access modes.")

# Check in different modes
check_file_access("test_access.txt", "r")
check_file_access("test_access.txt", "w")
check_file_access("test_access.txt", "r+")

# Create a function that returns the number of words, lines, and characters in a file.

def count_file_stats(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

        return line_count, word_count, char_count

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0, 0, 0

# Sample usage
sample_text = """Python is fun.
It is powerful.
Let's learn file handling."""

# Write the sample to a file
with open("sample_text.txt", "w") as f:
    f.write(sample_text)

# Count stats
lines, words, chars = count_file_stats("sample_text.txt")
print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {chars}")

# Create a report file that logs the time when a user logs in and out.

from datetime import datetime
import time

def log_event(username, event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{username} - {event} at {timestamp}\n"
    
    with open("login_log.txt", "a") as log_file:
        log_file.write(log_line)

# Sample usage
user = "nila_ramamoorthy"

# Simulate login
log_event(user, "Login")
print("Logged in...")

# Simulate session time (e.g., user does something)
time.sleep(2)

# Simulate logout
log_event(user, "Logout")
print("Logged out.")


# Open a file and count how many times a specific word appears.
def count_word_occurrences(filename, target_word):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()  # Convert to lowercase for case-insensitive matching
            count = content.count(target_word.lower())
            return count
    except FileNotFoundError:
        return f"File '{filename}' not found."

# Sample usage
filename = "sample_text.txt"
target_word = "python"

# You can create this file with sample text manually or by writing some text using another script
occurrences = count_word_occurrences(filename, target_word)
print(f"The word '{target_word}' appears {occurrences} times in '{filename}'.")


# Replace a word in a file with another word and save the result.
def replace_word_in_file(source_file, target_word, replacement_word, output_file):
    try:
        with open(source_file, "r") as file:
            content = file.read()

        updated_content = content.replace(target_word, replacement_word)

        with open(output_file, "w") as file:
            file.write(updated_content)

        print(f"All occurrences of '{target_word}' have been replaced with '{replacement_word}' in '{output_file}'.")

    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)

# Sample usage
source_file = "sample_text.txt"         # Original file
output_file = "updated_text.txt"        # File to save modified content
replace_word_in_file(source_file, "Python", "Java", output_file)

# Copy contents from one file to another file using file read and write.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, "r") as src:
            content = src.read()
        
        with open(destination_file, "w") as dest:
            dest.write(content)

        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")

    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)

# Sample usage
copy_file("sample_text.txt", "copied_text.txt")


# Reverse the contents of a file line by line and save into a new file.

def reverse_file_lines(source_file, destination_file):
    try:
        with open(source_file, "r") as src:
            lines = src.readlines()

        # Reverse each line's content
        reversed_lines = [line[::-1] for line in lines]

        with open(destination_file, "w") as dest:
            dest.writelines(reversed_lines)

        print(f"Lines reversed and saved to '{destination_file}' successfully.")

    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)

# Sample usage
reverse_file_lines("original.txt", "reversed.txt")

# Write and read structured data using writelines() and readlines().
def write_structured_data(filename, data_lines):
    try:
        with open(filename, "w") as file:
            # Each line should end with a newline character
            file.writelines([line + "\n" for line in data_lines])
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print("Error writing to file:", e)

def read_structured_data(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        print("Structured Data Read from File:")
        for line in lines:
            print(line.strip())
    except Exception as e:
        print("Error reading file:", e)

# Sample usage
data = [
    "Name: Alice, Age: 25, City: New York",
    "Name: Bob, Age: 30, City: London",
    "Name: Charlie, Age: 28, City: Paris"
]

filename = "structured_data.txt"
write_structured_data(filename, data)
read_structured_data(filename)

import os
import shutil
import glob
import time
from pathlib import Path

# 21. Handle FileNotFoundError
def handle_file_not_found(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

# Demo
handle_file_not_found("missing.txt")


# 22. Display file size and last modified date
def display_file_info(filename):
    try:
        size = os.path.getsize(filename)
        modified_time = time.ctime(os.path.getmtime(filename))
        print(f"File Size: {size} bytes")
        print(f"Last Modified: {modified_time}")
    except FileNotFoundError:
        print("File does not exist.")

# Demo
with open("sample.txt", "w") as f:
    f.write("Checking file info.")
display_file_info("sample.txt")


# 23. Check file existence and write permission
def check_write_permission(filename):
    if os.path.exists(filename) and os.access(filename, os.W_OK):
        print("File exists and is writable.")
    else:
        print("File does not exist or is not writable.")

# Demo
check_write_permission("sample.txt")


# 24. Use try-except-finally to always close the file
def safe_file_write(filename, text):
    file = None
    try:
        file = open(filename, "w")
        file.write(text)
    except Exception as e:
        print("Error:", e)
    finally:
        if file:
            file.close()
            print("File closed successfully.")

# Demo
safe_file_write("newfile.txt", "This is safely written text.")


# 25. Print file extensions in a folder
def list_file_extensions():
    print("File Extensions in Directory:")
    for file in os.listdir():
        if os.path.isfile(file):
            print(f"{file}: {Path(file).suffix}")

# Demo
list_file_extensions()


# 26. List all .txt files using glob
def list_txt_files():
    txt_files = glob.glob("*.txt")
    print(".txt Files:")
    for file in txt_files:
        print(file)

# Demo
list_txt_files()


# 27. Rename file and handle if new name exists
def rename_file(old_name, new_name):
    try:
        if os.path.exists(new_name):
            raise FileExistsError("New filename already exists.")
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} to {new_name}")
    except Exception as e:
        print("Rename Error:", e)

# Demo
rename_file("newfile.txt", "renamed_file.txt")


# 28. Delete file with error handling
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

# Demo
delete_file("renamed_file.txt")


# 29. Create folder structure using os.makedirs()
def create_folder_structure():
    nested_path = "folder1/folder2/folder3"
    os.makedirs(nested_path, exist_ok=True)
    print(f"Created: {nested_path}")

# Demo
create_folder_structure()


# 30. Move a file using shutil
def move_file(filename, target_folder):
    os.makedirs(target_folder, exist_ok=True)
    try:
        shutil.move(filename, f"{target_folder}/{filename}")
        print(f"Moved {filename} to {target_folder}")
    except Exception as e:
        print("Move Error:", e)

# Demo
with open("move_me.txt", "w") as f:
    f.write("I will be moved.")
move_file("move_me.txt", "folder1")
