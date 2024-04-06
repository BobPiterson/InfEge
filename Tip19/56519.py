def f(s1, s2, h):
    if s1 + s2 > 45 and h == 1:
        return True
    if s1 + s2 > 45:
        return False
    if h > 1:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 == 0:
        v = False
        for i in range(1, min_s + 1):
            v |= f(min_s + i, max_s, h + 1)
        return v
    else:
        v = False
        for i in range(1, min_s + 1):
            v |= f(min_s + i, max_s, h + 1)
        return v


mn = 1e9
for s1 in range(1, 46):
    for s2 in range(1, 46):
        if f(s1, s2, 0):
            mn = min(mn, s1 + s2)

print(mn)
print()


def f(s1, s2, h):
    if s1 + s2 > 45 and h == 3:
        return True
    if s1 + s2 > 45:
        return False
    if h > 3:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 == 0:
        v = False
        for i in range(1, min_s + 1):
            v |= f(min_s + i, max_s, h + 1)
        return v
    else:
        v = True
        for i in range(1, min_s + 1):
            v &= f(min_s + i, max_s, h + 1)
        return v


mn = 1e9
mx = 0
for s in range(1, 46):
    if f(5, s, 0):
        mn = min(mn, s)
        mx = max(mx, s)

print(mn, mx)
print()


def f(s1, s2, h):
    if s1 + s2 > 45 and h == 4:
        return True
    if s1 + s2 > 45:
        return False
    if h > 4:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 == 0:
        v = True
        for i in range(1, min_s + 1):
            v &= f(min_s + i, max_s, h + 1)
        return v
    else:
        v = False
        for i in range(1, min_s + 1):
            v |= f(min_s + i, max_s, h + 1)
        return v

def f2(s1, s2, h):
    if s1 + s2 > 45 and h == 2:
        return True
    if s1 + s2 > 45:
        return False
    if h > 2:
        return False

    min_s = min(s1, s2)
    max_s = max(s1, s2)
    if h % 2 == 0:
        v = True
        for i in range(1, min_s + 1):
            v &= f2(min_s + i, max_s, h + 1)
        return v
    else:
        v = False
        for i in range(1, min_s + 1):
            v |= f2(min_s + i, max_s, h + 1)
        return v


for s in range(1, 46):
    if f(5, s, 0) and not f2(5, s, 0):
        print(s)
        break

