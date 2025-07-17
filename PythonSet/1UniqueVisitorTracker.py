# 1. Unique Visitor Tracker

# Set to store unique visitor IPs
visitor_ips = set()

# Adding new visitor IPs
visitor_ips.add("192.168.1.10")
visitor_ips.add("192.168.1.20")
visitor_ips.add("192.168.1.30")
visitor_ips.add("192.168.1.10")  # duplicate, will not be added

# Total unique visitors
print("Total unique visitors:", len(visitor_ips))

# Blacklist an IP and remove it
blacklisted_ip = "192.168.1.20"
visitor_ips.discard(blacklisted_ip)

# Backup the current visitor set
backup_visitors = visitor_ips.copy()

# Check membership
check_ip = "192.168.1.30"
if check_ip in visitor_ips:
    print(check_ip, "visited the website.")

print("Current visitor IPs:", visitor_ips)
print("Backup visitor IPs:", backup_visitors)
