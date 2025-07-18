import os

filename = "output.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Hello, file created!")
    print("File created and written to.")
else:
    print("File already exists.")
