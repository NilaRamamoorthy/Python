def trx_id_generator(limit=1000):
    num = 1
    while num <= limit:
        reset = yield f"TRX{num:03d}"
        if isinstance(reset, int):
            num = reset
        else:
            num += 1
    return f"Reached limit of {limit} IDs"

# Demo usage:
gen = trx_id_generator(limit=10)
print("Generated IDs:", end=" ")
try:
    for _ in range(5):
        print(next(gen), end=" ")
    print("\n**Reset to TRX005**")
    print(gen.send(5))  # reset
    for _ in range(6):
        print(next(gen), end=" ")
except StopIteration as e:
    print("\nStop:", e.value)
