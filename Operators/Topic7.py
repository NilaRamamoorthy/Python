# Bitwise Operations Tasks (36–40)

# Task 36
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print(f"a & b = {a & b}")
print(f"a | b = {a | b}")
print(f"a ^ b = {a ^ b}")
print("-" * 40)

# Task 37
num = int(input("Enter a positive number: "))
print(f"~{num} = {~num}")
print("-" * 40)

# Task 38
num_shift = int(input("Enter a number to shift: "))
shift = int(input("Enter shift amount: "))
print(f"Original binary: {bin(num_shift)}")
print(f"{num_shift} << {shift} = {num_shift << shift} (binary: {bin(num_shift << shift)})")
print(f"{num_shift} >> {shift} = {num_shift >> shift} (binary: {bin(num_shift >> shift)})")
print("-" * 40)

# Task 39
x = 12
y = 5
print(f"x = {x} -> {bin(x)}")
print(f"y = {y} -> {bin(y)}")
print(f"x & y = {x & y} -> {bin(x & y)}")
print(f"x | y = {x | y} -> {bin(x | y)}")
print(f"x ^ y = {x ^ y} -> {bin(x ^ y)}")
print("-" * 40)

# Task 40
bit_num = int(input("Enter a number: "))
bit_position = int(input("Enter bit position to toggle (0 for LSB): "))
mask = 1 << bit_position  # Create mask for the position
print(f"Original: {bit_num} -> {bin(bit_num)}")
toggled = bit_num ^ mask
print(f"After toggling bit {bit_position}: {toggled} -> {bin(toggled)}")
print("-" * 40)