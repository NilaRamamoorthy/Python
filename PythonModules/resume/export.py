import os

def export_resume(content, filename="resume.txt"):
    folder = "output"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w") as file:
        file.write(content)
    print(f"Resume saved to {path}")
