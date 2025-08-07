from pytube import YouTube
import os
import functools
import sys
from tqdm import tqdm

# ========== Decorator for progress bar ==========
def progress_bar(func):
    @functools.wraps(func)
    def wrapper(self, url, output_path=None):
        yt = None
        try:
            yt = YouTube(url, on_progress_callback=self._on_progress)
        except Exception as e:
            print(f"[Error] Failed to initialize YouTube: {e}")
            return None

        try:
            return func(self, yt, output_path)
        except Exception as e:
            print(f"[Error] Download failed: {e}")
            return None
    return wrapper

class Downloader:
    def __init__(self):
        self.pbar = None

    def _on_progress(self, stream, chunk: bytes, bytes_remaining: int):
        if not self.pbar:
            self.pbar = tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=stream.default_filename)
        current = stream.filesize - bytes_remaining
        self.pbar.update(current - self.pbar.n)
        if bytes_remaining == 0:
            self.pbar.close()

    @progress_bar
    def download(self, yt: YouTube, output_path: str = "."):
        """Selects highest-resolution progressive stream and downloads it."""
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        if not stream:
            raise ValueError("No suitable mp4 progressive stream found")
        os.makedirs(output_path, exist_ok=True)
        filepath = stream.download(output_path=output_path)
        print(f"Downloaded to: {filepath}")
        return filepath

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ").strip()
    target_dir = input("Enter output folder (default current): ").strip() or "."
    dl = Downloader()
    result = dl.download(url, target_dir)
    if result:
        print("✅ Download completed!")
    else:
        print("❌ Download failed.")
