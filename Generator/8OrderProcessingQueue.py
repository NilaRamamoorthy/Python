def order_processor(orders):
    total = 0
    try:
        for order in orders:
            received = yield order
            total += 1
            if received:
                # send() provided desired extra count: yield one more
                for _ in range(received - 1):
                    order = next(orders_iter)
                    total += 1
                    yield order
    except Exception as e:
        print(f"[ERROR] Processing failed: {e}")
        raise
    return f"Processed {total} orders"

# Usage:
orders = iter(["ord1", "ord2", "ord3", "ord4"])
orders_iter = orders  # for inner use

gen = order_processor(orders)
print("Order:", next(gen))
print("Order:", next(gen))
print("Request 2 more:", gen.send(2))
try:
    next(gen)
except StopIteration as e:
    print("Completed:", e.value)
