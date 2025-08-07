import time
import datetime
import winsound
from functools import wraps

def snooze(duration=5):
    """Decorator to snooze the alarm for a specified duration."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Snoozing for {duration} minutes...")
            time.sleep(duration * 60)  # Convert minutes to seconds
            return func(*args, **kwargs)
        return wrapper
    return decorator

@snooze(duration=5)  # Set snooze duration to 5 minutes
def set_alarm(alarm_time_str):
    """Set an alarm to play a sound at the specified time."""
    try:
        # Parse the alarm time from the string
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
        print(f"Alarm set for {alarm_time.strftime('%H:%M')}.")

        while True:
            # Get the current time
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(f"Current time: {current_time}", end="\r")

            # Check if the current time matches the alarm time
            if current_time == alarm_time.strftime("%H:%M"):
                print("\nTime to Wake up!")
                winsound.Beep(2500, 1000)  # Frequency 2500 Hz, Duration 1000 ms
                break

            time.sleep(30)  # Check every 30 seconds

    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

# Example usage
if __name__ == "__main__":
    alarm_time_input = input("Enter alarm time (HH:MM): ")
    set_alarm(alarm_time_input)
