import os
import functools
import feedparser  # pip install feedparser
from datetime import datetime

def update_check(func):
    """Decorator to log the last update time after fetching."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        new_items = list(func(self, *args, **kwargs))
        if new_items:
            self.last_checked = datetime.now()
            print(f"[Update] {len(new_items)} new article(s) found. Checked at {self.last_checked}")
        else:
            print("[Update] No new articles found.")
        return (item for item in new_items)
    return wrapper

class Feed:
    def __init__(self, url, storage_dir='feeds'):
        self.url = url
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)
        self.seen_ids = set()
        self.last_checked = None
        # Load previously seen IDs if exists
        self._load_seen()

    def _load_seen(self):
        path = os.path.join(self.storage_dir, self._filename())
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    self.seen_ids.add(line.strip())

    def _filename(self):
        safe = self.url.replace('://', '_').replace('/', '_')
        return f"{safe}.seen"

    @update_check
    def fetch_new(self):
        try:
            feed = feedparser.parse(self.url)
        except Exception as e:
            print(f"[Error] Failed to parse feed: {e}")
            return

        new_entries = []
        for entry in feed.entries:
            entry_id = entry.get('id', entry.get('link'))
            if not entry_id:
                continue  # skip if no unique ID
            if entry_id not in self.seen_ids:
                new_entries.append(entry)
                self.seen_ids.add(entry_id)
        # Save updated seen IDs
        with open(os.path.join(self.storage_dir, self._filename()), 'w', encoding='utf-8') as f:
            for eid in self.seen_ids:
                f.write(f"{eid}\n")
        # Yield new entries as generator
        for entry in new_entries:
            yield entry

if __name__ == "__main__":
    feed_url = input("Enter RSS feed URL: ").strip()
    feed = Feed(feed_url)

    print("\nChecking for new articles...\n")
    for item in feed.fetch_new():
        title = item.get('title', 'No Title')
        link = item.get('link', 'No Link')
        published = item.get('published', 'No Date')
        print(f"• {title}\n  Link: {link}\n  Published: {published}\n")
