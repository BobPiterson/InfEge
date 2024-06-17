s = set()


def f(x, n):
    s.add(x)
    if n == 5:
        return 0
    return f(x + 1, n + 1) + f(x * 2, n + 1)


f(1, 0)
print(sorted(s))
