import datetime
import time

def digital_clock():
    try:
        while True:
            now = datetime.datetime.now()
            print(now.strftime("%H:%M:%S"), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    digital_clock()
