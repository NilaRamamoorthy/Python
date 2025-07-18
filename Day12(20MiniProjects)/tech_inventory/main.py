# main.py

from inventory_ops import add_device, view_device, list_all_brands

# Add devices
add_device(1001, "Laptop Pro", "TechBrand", ["16GB RAM", "512GB SSD", "Intel i7"])
add_device(1002, "Smartphone X", "MobileMaster", ["128GB Storage", "AMOLED Display"])
add_device(1003, "Laptop Pro", "TechBrand", ["8GB RAM", "256GB SSD", "Intel i5"])  # same brand, allowed
add_device(1001, "Duplicate Device", "OtherBrand", ["Invalid"])  # duplicate ID

# View devices
view_device(1001)
view_device(1002)

# List all brands
list_all_brands()
