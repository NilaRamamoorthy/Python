# Set of visitor IPs trying to access the system
incoming_ips = {"192.168.0.1", "10.0.0.2", "172.16.0.3", "203.0.113.5"}

# Set of blacklisted IPs
blacklist_ips = {"10.0.0.2", "203.0.113.5"}

# Logger to store only clean IPs
logged_ips = set()

# Process each incoming IP
for ip in incoming_ips:
    if {ip}.isdisjoint(blacklist_ips):  # Check if IP is not blacklisted
        logged_ips.add(ip)
    else:
        print(f"Blocked blacklisted IP: {ip}")

print("\nLogged Clean IPs:", logged_ips)

# Attempting to discard a blacklisted IP just in case it got added
for ip in blacklist_ips:
    logged_ips.discard(ip)

print("Final IP Log After Cleanup:", logged_ips)
