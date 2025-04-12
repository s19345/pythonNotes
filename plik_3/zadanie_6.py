import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fibo_cached(n):
    if n < 2:
        return n
    return fibo_cached(n - 1) + fibo_cached(n - 2)


def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


n = 20

start_plain = time.time()
result_plain = fibo(n)
end_plain = time.time()
print(f"Bez cache: F({n}) = {result_plain}, czas: {end_plain - start_plain:.4f} sekundy")

start_cached = time.time()
result_cached = fibo(n)
end_cached = time.time()
print(f"Z cache:  F({n}) = {result_cached}, czas: {end_cached - start_cached:.4f} sekundy")

