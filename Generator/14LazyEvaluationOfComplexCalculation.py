ops = [
    (5, 3, '+'),
    (10, 2, '/'),
    (6, 7, '*'),
    (8, 5, '-'),
]

def calc_result(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/' and b != 0:
        return a / b
    return None

# Generator expression with lazy evaluation & on-demand result computation
lazy_results = (calc_result(a, b, op) for a, b, op in ops)

print("Results lazily computed:")
for res in lazy_results:
    print(res)
