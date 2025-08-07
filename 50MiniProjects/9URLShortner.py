import json
import string
import random
import re
from functools import lru_cache
from datetime import datetime, timedelta

DATA_FILE = "urls.json"

# Decorator for caching frequently accessed URLs
def cache(func):
    cached = lru_cache(maxsize=10)(func)
    return cached

# URL validation
def is_valid_url(url):
    pattern = re.compile(r'https?://[^\s]+')
    return bool(pattern.match(url))

# URLShortener Class
class URLShortener:
    def __init__(self):
        self.urls = {}  # short_code: {url, created_at}
        self.load_data()

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.urls, f)

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                self.urls = json.load(f)
        except FileNotFoundError:
            self.urls = {}

    def generate_shortcode(self, length=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def shorten(self, long_url):
        if not is_valid_url(long_url):
            raise ValueError("Invalid URL format.")

        short_code = self.generate_shortcode()
        while short_code in self.urls:
            short_code = self.generate_shortcode()

        self.urls[short_code] = {
            "url": long_url,
            "created_at": datetime.now().isoformat()
        }
        self.save_data()
        print(f"Shortened URL: {short_code}")
        return short_code

    @cache
    def redirect(self, short_code):
        if short_code in self.urls:
            return self.urls[short_code]["url"]
        else:
            raise KeyError("Short code not found.")

    def delete(self, short_code):
        if short_code in self.urls:
            del self.urls[short_code]
            self.save_data()
            print(f"{short_code} deleted successfully.")
        else:
            print("Short code not found.")

    def list_urls(self):
        print("\nShortened URLs:")
        for code, info in self.urls.items():
            print(f"{code} → {info['url']} (Created: {info['created_at']})")

    def expired_urls(self, days=30):
        now = datetime.now()
        for code, info in self.urls.items():
            created_at = datetime.fromisoformat(info["created_at"])
            if (now - created_at).days > days:
                yield code, info["url"]

# ---------------------------
# 🎮 Demo UI
# ---------------------------
def main():
    shortener = URLShortener()

    while True:
        print("\n--- URL Shortener Menu ---")
        print("1. Shorten URL")
        print("2. Redirect URL")
        print("3. Delete URL")
        print("4. List All URLs")
        print("5. Show Expired URLs (>30 days)")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            url = input("Enter long URL: ")
            try:
                shortener.shorten(url)
            except ValueError as e:
                print(e)

        elif choice == "2":
            code = input("Enter short code: ")
            try:
                original = shortener.redirect(code)
                print("Original URL:", original)
            except KeyError:
                print("Short code does not exist.")

        elif choice == "3":
            code = input("Enter short code to delete: ")
            shortener.delete(code)

        elif choice == "4":
            shortener.list_urls()

        elif choice == "5":
            print("Expired URLs:")
            for code, url in shortener.expired_urls():
                print(f"{code} → {url}")

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
