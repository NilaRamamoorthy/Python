# records.py

# Dictionary to hold patient records
patient_records = {}

# Set to store unique illness types
illness_types = set()

def add_record(patient_id, name, age, illness, prescribed_meds):
    key = (patient_id,)
    if key in patient_records:
        print(f"Patient {name} already has a record.\n")
        return

    patient_records[key] = {
        "name": name,
        "age": age,
        "illness": illness,
        "medications": prescribed_meds
    }

    illness_types.add(illness)
    print(f"Medical record added for {name} with illness '{illness}'.\n")

def view_records():
    print("🩺 Patient Records:")
    for pid, data in patient_records.items():
        print(f"ID: {pid}, Name: {data['name']}, Age: {data['age']}, Illness: {data['illness']}, Meds: {', '.join(data['medications'])}")
    print()

def view_illnesses():
    print("Recorded Illness Types:")
    print(", ".join(illness_types), "\n")
