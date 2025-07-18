import json
import os

DATA_FILE = "student_tracker/data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": {}, "courses": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
