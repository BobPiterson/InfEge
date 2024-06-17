from functools import cache


@cache
def f(n):
    if n == 1:
        return 2
    if n == 2:
        return 1

    return f(n - 2) + f(n - 1)

print(f(8))
for i in range(1, 100):
    print(i, f(i))
