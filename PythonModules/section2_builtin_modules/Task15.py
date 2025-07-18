import os

def list_files(path="."):
    files = os.listdir(path)
    for file in files:
        print(file)

if __name__ == "__main__":
    list_files()
