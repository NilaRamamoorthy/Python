import os
from pathlib import Path
import functools

# Decorator to convert bytes to human-readable format
def human_readable(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        size_bytes = func(*args, **kwargs)
        for unit in ['B','KB','MB','GB','TB']:
            if size_bytes < 1024 or unit == 'TB':
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
    return wrapper

class DirectorySizeAnalyzer:
    def __init__(self, root_path):
        self.root = Path(root_path)
        if not self.root.exists():
            raise FileNotFoundError(f"Path not found: {self.root}")
        self.sizes = {}  # dict: Path -> size_in_bytes

    def compute_sizes(self):
        """Walk directory and compute sizes per subdirectory and root."""
        for dirpath, dirnames, filenames in os.walk(self.root):
            total = 0
            for fname in filenames:
                fpath = Path(dirpath) / fname
                try:
                    if not fpath.is_symlink() and fpath.exists():
                        total += fpath.stat().st_size
                except (PermissionError, OSError) as e:
                    print(f"[Warning] Could not access {fpath}: {e}")
            self.sizes[Path(dirpath)] = total

    @human_readable
    def get_total_size(self):
        """Returns total size of the root directory."""
        return sum(self.sizes.values())

    def find_large_files(self, min_size_bytes):
        """
        Generator yielding (Path, size_bytes) for files larger than threshold.
        """
        for dirpath, _, filenames in os.walk(self.root):
            for fname in filenames:
                fpath = Path(dirpath) / fname
                try:
                    size = fpath.stat().st_size
                    if size >= min_size_bytes:
                        yield fpath, size
                except (PermissionError, OSError):
                    continue

if __name__ == "__main__":
    path = input("Enter directory path: ").strip()
    analyzer = DirectorySizeAnalyzer(path)
    analyzer.compute_sizes()

    print(f"\nTotal size of '{path}': {analyzer.get_total_size()}")

    threshold_mb = float(input("List files larger than how many MB? "))
    threshold = threshold_mb * 1024 * 1024
    print(f"\nFiles larger than {threshold_mb} MB:\n")
    for filepath, sz in analyzer.find_large_files(threshold):
        print(f"{filepath} — {sz / 1024 / 1024:.2f} MB")
