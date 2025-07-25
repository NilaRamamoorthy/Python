import time

def log_stream(filepath, keywords=None):
    """Generator that watches a file, yielding lines with keywords."""
    keywords = keywords or ["ERROR", "WARNING"]
    try:
        with open(filepath, 'r') as f:
            # Seek to end to follow new lines
            f.seek(0, 2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                if any(key in line for key in keywords):
                    yield line.rstrip()
    except GeneratorExit:
        return

# Usage:
try:
    print("Monitoring log for ERROR or WARNING (Ctrl+C to stop):")
    for entry in log_stream('app.log', keywords=["ERROR", "WARNING"]):
        print(entry)
except KeyboardInterrupt:
    print("\nLog monitoring stopped by user.")
