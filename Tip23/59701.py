def f(x, s):
    if x == s:
        return 1
    if x > s or x == 17:
        return 0

    return f(x + 2, s) + f(x + 3, s) + f(x * 2, s)


print(f(3, 10) * f(10, 25))
