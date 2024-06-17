from functools import cache


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(400))
print(fib.cache_info())

def f(n):
    if n >= 2025:
        return n

    return n + 3 + f(n + 3)


print(f(23) - f(21))
