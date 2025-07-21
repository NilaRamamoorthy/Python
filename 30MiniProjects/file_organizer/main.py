import os
from scanner import scan_directory
from mover import move_files_by_type

directory = os.getcwd()  # You can change this to any path you want

print(f"Scanning directory: {directory}")
files_by_type, file_types = scan_directory(directory)

print("\nDetected file types:")
for file_type in file_types:
    print(f"  {file_type if file_type else 'No Extension'}")

move_files_by_type(directory, files_by_type)

print("\nFiles have been organized by type.")
