# 1 & 2: Open file and use iter(), next(), and StopIteration
f = open('sample.txt', 'w+')
f.write("\nFirst line\n\nSecond line\nThird line\n\n")
f.seek(0)

it = iter(f)  # file object is its own iterator
print("Reading non-empty lines one by one:")
while True:
    try:
        line = next(it)
    except StopIteration:
        print("End of file reached.")
        break
    if line.strip():  # skip empty lines
        print("Line:", line.rstrip())

f.close()
