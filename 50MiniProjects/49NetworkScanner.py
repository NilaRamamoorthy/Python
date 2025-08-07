from scapy.all import ARP, Ether, srp, conf
import functools
import time

# Decorator to measure execution speed
def speed_test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[Speed Test] {func.__name__} took {elapsed:.2f} seconds")
        return result
    return wrapper

class Scanner:
    def __init__(self, ip_range: str, timeout: float = 1.0):
        self.ip_range = ip_range
        self.timeout = timeout
        self.host_status = {}  # Dict to hold IP -> status ("up"/"down")

    @speed_test
    def scan(self):
        """Perform an ARP scan over the IP range, filling host_status dict."""
        conf.verb = 0
        arp = ARP(pdst=self.ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        try:
            answered = srp(packet, timeout=self.timeout, retry=1, verbose=False)[0]
        except Exception as e:
            print(f"[Error] Scan failed: {e}")
            return

        # Mark all as down initially (could be expanded to full range)
        # Then mark answered ones as up
        for sent, received in answered:
            ip = received.psrc
            self.host_status[ip] = "up"

    def live_hosts(self):
        """Generator yielding IPs that responded (“up”)."""
        for ip, status in self.host_status.items():
            if status == "up":
                yield ip

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # Adjust as needed
    scanner = Scanner(ip_range=ip_range, timeout=2.0)
    scanner.scan()

    print("Live hosts found:")
    for ip in scanner.live_hosts():
        print(f" - {ip}")
