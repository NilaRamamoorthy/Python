# main.py

from parcel import update_parcel, fetch_parcel_info, display_all_parcels

print(update_parcel("T123", "Dispatched", "Chennai"))
print(update_parcel("T123", "In Transit", "Bangalore"))
print(update_parcel("T123", "Delivered", "Mysore"))

print(update_parcel("T456", "Dispatched", "Delhi"))
print(update_parcel("T456", "In Transit", "Agra"))

print(fetch_parcel_info("T123"))
print(fetch_parcel_info("T456"))

display_all_parcels()
