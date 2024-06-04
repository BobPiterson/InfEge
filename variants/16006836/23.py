def f(x, n):
    if x == n:
        return 1
    if x > n:
        return 0

    return f(x + 1, n) + f(x * 2, n) + f(2 * x + 1, n)

print(f(2, 16))
