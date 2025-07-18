# traffic_control.py

signal_status = {}  # { (location, time): "RED"/"GREEN"/"YELLOW" }
active_lights = set()  # to prevent duplicates

def set_signal(location, time, status):
    key = (location, time)
    if status.upper() in {"RED", "GREEN", "YELLOW"}:
        signal_status[key] = status.upper()
        active_lights.add(status.upper())

def get_signal(location, time):
    key = (location, time)
    return signal_status.get(key, "No Signal Found")

def display_all_signals():
    print("\n🚦 Traffic Signals:")
    for key, status in signal_status.items():
        print(f"Location: {key[0]}, Time: {key[1]}, Status: {status}")
    print(f"\nActive Light Types: {active_lights}")
