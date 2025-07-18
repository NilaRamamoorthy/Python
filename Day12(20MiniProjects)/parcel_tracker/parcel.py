# parcel.py

parcel_records = {}  # { (tracking_id): { "status": ..., "cities": set([...]) } }

def update_parcel(tracking_id, status, city):
    if tracking_id not in parcel_records:
        parcel_records[tracking_id] = {"status": status, "cities": set([city])}
    else:
        parcel_records[tracking_id]["status"] = status
        parcel_records[tracking_id]["cities"].add(city)
    return f"📦 Updated: {tracking_id} - {status} @ {city}"

def fetch_parcel_info(tracking_id):
    if tracking_id in parcel_records:
        record = parcel_records[tracking_id]
        cities = ', '.join(record["cities"])
        return f"🔎 Parcel {tracking_id} - Status: {record['status']}, Route: {cities}"
    return "⚠️ Parcel not found."

def display_all_parcels():
    print("\n📦 All Parcels Info:")
    for tid, info in parcel_records.items():
        print(f"ID: {tid} | Status: {info['status']} | Cities: {', '.join(info['cities'])}")
