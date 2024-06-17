def f(s, h):
    if s > 45 and h == 2:
        return True
    if s > 45:
        return False
    if h > 2:
        return False

    if h % 2 == 0:
        return f(s + 1, h + 1) or f(s * 2, h + 1)
    else:
        return f(s + 1, h + 1) or f(s * 2, h + 1)


for s in range(1, 46):
    if f(s, 0):
        print(s)
        break


def f(s, h):
    if s > 45 and h == 3:
        return True
    if s > 45:
        return False
    if h > 3:
        return False

    if h % 2 == 0:
        return f(s + 1, h + 1) or f(s * 2, h + 1)
    else:
        return f(s + 1, h + 1) and f(s * 2, h + 1)


print()
for s in range(1, 46):
    if f(s, 0):
        print(s)


def f(s, h):
    if s > 45 and (h == 2 or h == 4):
        return True
    if s > 45:
        return False
    if h > 4:
        return False

    if h % 2 == 0:
        return f(s + 1, h + 1) and f(s * 2, h + 1)
    else:
        return f(s + 1, h + 1) or f(s * 2, h + 1)


def f2(s, h):
    if s > 45 and h == 2:
        return True
    if s > 45:
        return False
    if h > 2:
        return False

    if h % 2 == 0:
        return f2(s + 1, h + 1) and f2(s * 2, h + 1)
    else:
        return f2(s + 1, h + 1) or f2(s * 2, h + 1)


print()
for s in range(1, 46):
    if f(s, 0) and not f2(s, 0):
        print(s)
