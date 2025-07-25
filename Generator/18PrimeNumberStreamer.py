import math

def gen_primes_upto(N):
    """Efficient prime generator up to N."""
    if N >= 2:
        yield 2
    primes = []
    for num in range(3, N+1, 2):  # skip even numbers
        is_prime = True
        limit = int(math.isqrt(num))
        for p in primes:
            if p > limit:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num

# Usage:
N = 30
print(f"Primes up to {N}:")
for prime in gen_primes_upto(N):
    print(prime, end=" ")
