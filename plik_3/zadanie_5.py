import functools

def memo(func):
    @functools.wraps(func)
    def memo(*args):
        if args not in memo.cache:
            memo.cache[args] = func(*args)
        return memo.cache[args]
    memo.cache = {}
    return memo

@memo
def fibo(n):
    if n < 2: return n
    else: return fibo(n-1) + fibo(n-2)

for i in range(50, 201, 50):
    print(f'fibonacci[{i}] = {fibo(i)}')

