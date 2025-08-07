import os
import sys
import subprocess
import functools

def os_handler(func):
    """Decorator to catch OS-specific exceptions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[Error] {func.__name__} failed: {e}")
            return []
    return wrapper

class WiFiPasswordViewer:
    def __init__(self):
        self.os_type = sys.platform
        self.networks = []  # list of saved network names (SSIDs)

    @os_handler
    def fetch_saved_networks(self):
        """Populate self.networks with saved WiFi profiles."""
        if self.os_type.startswith('win'):
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8', errors='ignore')
            self.networks = [line.split(":")[1].strip() for line in output.splitlines() if "All User Profile" in line]
        else:
            # Linux (NetworkManager)
            output = subprocess.check_output(['nmcli', '-t', '-f', 'NAME', 'connection', 'show'], encoding='utf-8', errors='ignore')
            self.networks = output.splitlines()
        return self.networks

    @os_handler
    def get_password_for(self, ssid):
        """Return the password for a given SSID, or empty if unavailable."""
        if self.os_type.startswith('win'):
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'],
                                             encoding='utf-8', errors='ignore')
            for line in output.splitlines():
                if "Key Content" in line:
                    return line.split(":", 1)[1].strip()
        else:
            # Try nmcli first
            try:
                output = subprocess.check_output(['nmcli', 'connection', 'show', ssid], encoding='utf-8', errors='ignore')
                for line in output.splitlines():
                    if '802-11-wireless-security.psk:' in line:
                        return line.split(':', 1)[1].strip()
            except subprocess.CalledProcessError:
                pass
            # Fallback: read from NetworkManager files
            path = f"/etc/NetworkManager/system-connections/{ssid}"
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if line.lstrip().startswith("psk="):
                            return line.split("=", 1)[1].strip()
        return ""

    def passwords(self):
        """Generator yielding (ssid, password) tuples."""
        for ssid in self.networks:
            pwd = self.get_password_for(ssid)
            yield ssid, pwd

if __name__ == "__main__":
    viewer = WiFiPasswordViewer()
    nets = viewer.fetch_saved_networks()
    if not nets:
        print("No saved Wi-Fi networks found or unable to fetch list.")
        sys.exit()

    print("Saved Wi‑Fi networks:")
    for ssid in nets:
        print(f" - {ssid}")

    print("\nPasswords:")
    for ssid, pwd in viewer.passwords():
        print(f"{ssid}: {pwd or '[No password found or access denied]'}")
