# maxsize parameter for lru_cache (default is 128)
from functools import lru_cache

@lru_cache(maxsize=3)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(100))
print('\n')