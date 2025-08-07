import os
import zipfile
from pathlib import Path
from datetime import datetime
import functools
import schedule  # Requires: pip install schedule

# Decorator to schedule functions
def schedule_job(interval: str, time_str: str = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        # Hook into scheduler based on interval spec
        if interval == 'daily' and time_str:
            schedule.every().day.at(time_str).do(wrapper)
        elif interval == 'hourly':
            schedule.every().hour.do(wrapper)
        # Extend with other intervals as needed
        return wrapper
    return decorator

# Backup class for OOP structure
class Backup:
    def __init__(self, source: str, destination: str, max_backups: int = 5):
        self.source = Path(source).expanduser().resolve()
        self.destination = Path(destination).expanduser().resolve()
        self.max_backups = max_backups
        self.destination.mkdir(parents=True, exist_ok=True)

    def _cleanup_old_backups(self):
        backups = sorted(
            [f for f in self.destination.iterdir() if f.suffix == '.zip' and f.name.startswith('backup-')],
            key=lambda x: x.name
        )
        while len(backups) >= self.max_backups:
            old = backups.pop(0)
            old.unlink()

    def create_backup(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_name = f'backup-{timestamp}-{self.source.name}.zip'
        backup_path = self.destination / backup_name

        self._cleanup_old_backups()

        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if self.source.is_file():
                zipf.write(self.source, arcname=self.source.name)
            elif self.source.is_dir():
                for file in self.source.rglob('*'):
                    if file.is_file():
                        zipf.write(file, arcname=str(file.relative_to(self.source)))
        print(f"[{timestamp}] Backup created at: {backup_path}")

    def progress_generator(self):
        for file in self.source.rglob('*'):
            if file.is_file():
                yield file.relative_to(self.source)

# Instantiate backup (change paths as needed)
backup = Backup(source="~/source_folder", destination="~/backups", max_backups=3)

@schedule_job(interval='daily', time_str="23:00")
def scheduled_backup():
    print("Starting scheduled backup...")
    for p in backup.progress_generator():
        print(f"Processing: {p}")
    try:
        backup.create_backup()
    except FileNotFoundError as e:
        print(f"Error during backup: {e}")

def run_scheduler():
    print("Scheduler started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        import time
        time.sleep(1)

if __name__ == "__main__":
    scheduled_backup()  # Register the job
    run_scheduler()
