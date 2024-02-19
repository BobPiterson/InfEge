# https://kompege.ru/variant
def f(x, c):
    if x % 2 == 0:
        c += 1

    if c > 6 or c > 25:
        return 0

    if c == 6 and x == 25:
        return 1

    return f(x + 1, c) + f(x + 3, c) + f(x + 5, c)


print(f(3, 0))



