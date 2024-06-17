def f(s1, s2, h):
    if s1 + s2 > 40 and h == 1:
        return True
    if s1 + s2 > 40:
        return False
    if h > 1:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 == 0:
        v = f(min_s, max_s + 1, h + 1) or f(min_s, max_s + 2, h + 1) or f(min_s, max_s + 3, h + 1)
        if min_s != max_s:
            v |= f(min_s * 2, max_s, h + 1)
        return v
    else:
        v = f(min_s, max_s + 1, h + 1) or f(min_s, max_s + 2, h + 1) or f(min_s, max_s + 3, h + 1)
        if min_s != max_s:
            v |= f(min_s * 2, max_s, h + 1)
        return v


mn = 1e9
for s1 in range(1, 41):
    for s2 in range(1, 41):
        if f(s1, s2, 0):
            mn = min(mn, s1 + s2)

print(mn)
print()


def f(s1, s2, h):
    if s1 + s2 > 40 and h == 3:
        return True
    if s1 + s2 > 40:
        return False
    if h > 3:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 != 0:
        v = f(min_s, max_s + 1, h + 1) and f(min_s, max_s + 2, h + 1) and f(min_s, max_s + 3, h + 1)
        if min_s != max_s:
            v &= f(min_s * 2, max_s, h + 1)
        return v
    else:
        v = f(min_s, max_s + 1, h + 1) or f(min_s, max_s + 2, h + 1) or f(min_s, max_s + 3, h + 1)
        if min_s != max_s:
            v |= f(min_s * 2, max_s, h + 1)
        return v


mn = 1e9
mx = -1
for s in range(1, 36):
    if f(5, s, 0):
        mn = min(mn, s)
        mx = max(mx, s)

print(mn, mx)
print()


def f(s1, s2, h):
    if s1 + s2 > 40 and h == 4:
        return True
    if s1 + s2 > 40:
        return False
    if h > 4:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 == 0:
        v = f(min_s, max_s + 1, h + 1) and f(min_s, max_s + 2, h + 1) and f(min_s, max_s + 3, h + 1)
        if min_s != max_s:
            v &= f(min_s * 2, max_s, h + 1)
        return v
    else:
        v = f(min_s, max_s + 1, h + 1) or f(min_s, max_s + 2, h + 1) or f(min_s, max_s + 3, h + 1)
        if min_s != max_s:
            v |= f(min_s * 2, max_s, h + 1)
        return v


def f2(s1, s2, h):
    if s1 + s2 > 40 and h == 2:
        return True
    if s1 + s2 > 40:
        return False
    if h > 2:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 == 0:
        v = f2(min_s, max_s + 1, h + 1) and f2(min_s, max_s + 2, h + 1) and f2(min_s, max_s + 3, h + 1)
        if min_s != max_s:
            v &= f2(min_s * 2, max_s, h + 1)
        return v
    else:
        return f2(min_s, max_s + 1, h + 1) or f2(min_s, max_s + 2, h + 1) or f2(min_s, max_s + 3, h + 1) or (
                f2(min_s * 2, max_s, h + 1) and min_s != max_s)


for s in range(1, 24):
    print(f(17, s, 0))
    if f(17, s, 0) and not f2(17, s, 0):
        print(s)

print()
