# service_manager.py

vehicle_records = {}  # { (plate_number): {"owner": str, "services": set()} }

def register_vehicle(plate_number, owner):
    if plate_number in vehicle_records:
        return "⚠️ Vehicle already registered."
    vehicle_records[plate_number] = {"owner": owner, "services": set()}
    return f"✅ Vehicle {plate_number} registered for {owner}."

def add_service(plate_number, service_type):
    if plate_number not in vehicle_records:
        return "❌ Vehicle not found."
    vehicle_records[plate_number]["services"].add(service_type)
    return f"🛠️ Service '{service_type}' added to vehicle {plate_number}."

def get_services(plate_number):
    if plate_number not in vehicle_records:
        return "❌ Vehicle not found."
    services = vehicle_records[plate_number]["services"]
    return f"🔧 Services for {plate_number}: {', '.join(services) if services else 'No services yet'}"

def get_owner_info(plate_number):
    if plate_number not in vehicle_records:
        return "❌ Vehicle not found."
    owner = vehicle_records[plate_number]["owner"]
    return f"👤 Owner of {plate_number}: {owner}"
