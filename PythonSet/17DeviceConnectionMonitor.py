# Devices currently connected to Server A and Server B
server_A_devices = {"Device1", "Device2", "Device3"}
server_B_devices = {"Device4", "Device5", "Device3"}  # Device3 connected to both

# Current connections on Server A
current_connections = server_A_devices.copy()

print("Initial connections on Server A:", current_connections)

# Device disconnects randomly
disconnected_device = current_connections.pop()
print(f"Device disconnected: {disconnected_device}")
print("Updated connections after disconnection:", current_connections)

# Merge connections from both servers
all_connected_devices = server_A_devices.union(server_B_devices)
print("All connected devices across both servers:", all_connected_devices)

# Membership test
check_device = "Device5"
if check_device in all_connected_devices:
    print(f"{check_device} is connected.")
else:
    print(f"{check_device} is not connected.")
