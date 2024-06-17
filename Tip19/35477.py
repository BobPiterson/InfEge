def f(s1, s2, h):
    if s1 + s2 >= 77 and h == 2:
        return True
    if s1 + s2 >= 77:
        return False
    if h > 2:
        return False

    if h % 2 == 0:
        return f(s1 + 1, s2, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 + 1, h + 1) or f(s1, s2 * 2, h + 1)
    else:
        return f(s1 + 1, s2, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 + 1, h + 1) or f(s1, s2 * 2, h + 1)


for s in range(1, 69):
    if f(8, s, 0):
        print(s)
        break

print()


def f(s1, s2, h):
    if s1 + s2 >= 77 and h == 3:
        return True
    if s1 + s2 >= 77:
        return False
    if h > 2:
        return False

    if h % 2 == 0:
        return f(s1 + 1, s2, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 + 1, h + 1) or f(s1, s2 * 2, h + 1)
    else:
        return f(s1 + 1, s2, h + 1) and f(s1 * 2, s2, h + 1) and f(s1, s2 + 1, h + 1) and f(s1, s2 * 2, h + 1)


for s in range(1, 69):
    if f(8, s, 0):
        print(s)

print()


def f(s1, s2, h):
    if s1 + s2 >= 77 and h % 2 == 0:
        return True
    if s1 + s2 >= 77:
        return False

    if h % 2 == 0:
        return f(s1 + 1, s2, h + 1) and f(s1 * 2, s2, h + 1) and f(s1, s2 + 1, h + 1) and f(s1, s2 * 2, h + 1)
    else:
        return f(s1 + 1, s2, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 + 1, h + 1) or f(s1, s2 * 2, h + 1)


for s in range(68, 0, -1):
    if f(8, s, 0):
        print(s)
        break

print()
