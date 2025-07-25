def reversed_lines(filepath):
    """Generator yielding reversed content of each non-empty line."""
    with open(filepath, 'r') as f:
        for line in f:
            content = line.rstrip('\n')
            yield content[::-1]  # reverse string

# Demo:
with open('sample.txt', 'w') as f:
    f.write("Hello World\nPython\n\nEnd\n")
print("Reversed lines:")
for rl in reversed_lines('sample.txt'):
    print(f"'{rl}'")
