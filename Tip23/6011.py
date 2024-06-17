def f(x, s):
    if x == s:
        return 1
    if x > s:
        return 0

    return f(x + 1, s) + f(x * 2, s)


print(f(2, 22))
