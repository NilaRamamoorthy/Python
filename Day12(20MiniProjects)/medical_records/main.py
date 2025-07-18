# main.py

from healthcare_records.records import add_record, view_records, view_illnesses

# Add medical records
add_record(1001, "Arjun", 35, "Diabetes", ["Metformin", "Insulin"])
add_record(1002, "Leela", 28, "Asthma", ["Inhaler", "Montelukast"])
add_record(1001, "Arjun", 35, "Hypertension", ["Amlodipine"])  # Duplicate

# View all records
view_records()

# View all illness types recorded
view_illnesses()
