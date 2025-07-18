# inventory_ops.py

# Dictionary to store device info with tuple as key
devices = {}

# Set to track unique brands added
brands = set()

def add_device(device_id, name, brand, specs):
    key = (device_id,)
    if key in devices:
        print(f"Device ID '{device_id}' already exists.\n")
        return
    
    devices[key] = {
        "name": name,
        "brand": brand,
        "specs": specs
    }
    brands.add(brand)
    print(f"Device '{name}' added successfully.\n")

def view_device(device_id):
    key = (device_id,)
    if key not in devices:
        print(f"Device ID '{device_id}' not found.\n")
        return

    data = devices[key]
    print(f"--- Device {device_id} ---")
    print(f"Name: {data['name']}")
    print(f"Brand: {data['brand']}")
    print("Specifications:")
    for spec in data["specs"]:
        print(f" - {spec}")
    print()

def list_all_brands():
    print("Unique Brands in Inventory:")
    print(", ".join(brands), "\n")
