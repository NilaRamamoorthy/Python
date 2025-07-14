# 2. GPS Location Logger
locations = [(12.97, 77.59), (12.98, 77.60), (12.99, 77.61), (13.00, 77.62), (13.01, 77.63), (13.02, 77.64)]
last_5 = locations[-5:]
for lat, lon in last_5:
    print(f"Latitude: {lat}, Longitude: {lon}")
