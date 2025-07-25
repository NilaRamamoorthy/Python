class WeatherLogIterator:
    def __init__(self, filepath, threshold=30):
        self.file = open(filepath, 'r')
        self.threshold = threshold
        self.it = iter(self.file)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = next(self.it)  # may raise StopIteration at EOF
            line = line.strip()
            if not line:
                continue  # skip empty lines
            try:
                temp = float(line)
            except ValueError:
                continue  # skip non-numeric lines
            if temp > self.threshold:
                return temp
            # otherwise, continue looping

    def close(self):
        self.file.close()

# Create a sample file
with open('temps.txt', 'w') as f:
    f.write("""
25.0
31.2

29.5
35.0
invalid
30.1
""")

it = WeatherLogIterator('temps.txt', threshold=30)

print("Temperatures above 30°C:")
try:
    while True:
        temp = next(it)
        print(temp)
except StopIteration:
    print("End of file reached.")
finally:
    it.close()

# Expected output:
# Temperatures above 30°C:
# 31.2
# 35.0
# 30.1
# End of file reached.
