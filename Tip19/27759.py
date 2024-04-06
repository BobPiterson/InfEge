def f(s1, s2, h):
    if s1 + s2 >= 41 and h == 2:
        return True
    if s1 + s2 >= 41:
        return False
    if h > 2:
        return False

    if h % 2 == 0:
        return f(s1 + 1, s2 + 2, h + 1) or f(s1 + 2, s2 + 1, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)
    else:
        return f(s1 + 1, s2 + 2, h + 1) or f(s1 + 2, s2 + 1, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)


for s in range(1, 33):
    if f(8, s, 0):
        print(s)
        break


def f(s1, s2, h):
    if s1 + s2 >= 41 and h == 3:
        return True
    if s1 + s2 >= 41:
        return False
    if h > 3:
        return False

    if h % 2 == 0:
        return f(s1 + 1, s2 + 2, h + 1) or f(s1 + 2, s2 + 1, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)
    else:
        return f(s1 + 1, s2 + 2, h + 1) and f(s1 + 2, s2 + 1, h + 1) and f(s1 * 2, s2, h + 1) and f(s1, s2 * 2, h + 1)


for s in range(32, 0, -1):
    if f(8, s, 0):
        print(s)
        break


def f(s1, s2, h):
    if s1 + s2 >= 41 and (h == 2 or h == 4):
        return True
    if s1 + s2 >= 41:
        return False
    if h > 4:
        return False

    if h % 2 == 0:
        return f(s1 + 1, s2 + 2, h + 1) and f(s1 + 2, s2 + 1, h + 1) and f(s1 * 2, s2, h + 1) and f(s1, s2 * 2, h + 1)
    else:
        return f(s1 + 1, s2 + 2, h + 1) or f(s1 + 2, s2 + 1, h + 1) or f(s1 * 2, s2, h + 1) or f(s1, s2 * 2, h + 1)


def f2(s1, s2, h):
    if s1 + s2 >= 41 and h == 2:
        return True
    if s1 + s2 >= 41:
        return False
    if h > 2:
        return False

    if h % 2 == 0:
        return f2(s1 + 1, s2 + 2, h + 1) and f2(s1 + 2, s2 + 1, h + 1) and f2(s1 * 2, s2, h + 1) and f2(s1, s2 * 2, h + 1)
    else:
        return f2(s1 + 1, s2 + 2, h + 1) or f2(s1 + 2, s2 + 1, h + 1) or f2(s1 * 2, s2, h + 1) or f2(s1, s2 * 2, h + 1)


for s in range(1, 33):
    if f(8, s, 0) and not f2(8, s, 0):
        print(s)
        break
