def f(n):
    if n <= 2:
        return n + 1

    return f(n - 1) + 2 * f(n - 2)

print(f(4))
