# main.py

from service_manager import register_vehicle, add_service, get_services, get_owner_info

# Register vehicles
print(register_vehicle(("TN10AB1234",), "Karthik Kumar"))
print(register_vehicle(("TN10AB1234",), "Duplicate Check"))

# Add services
print(add_service(("TN10AB1234",), "Oil Change"))
print(add_service(("TN10AB1234",), "Tire Rotation"))
print(add_service(("TN10AB1234",), "Oil Change"))  # Duplicate ignored by set

# View information
print("\n" + get_owner_info(("TN10AB1234",)))
print(get_services(("TN10AB1234",)))
