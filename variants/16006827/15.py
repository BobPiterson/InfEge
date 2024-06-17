def bel(x, l, r):
    return l <= x <= r


def f(x, l, r):
    return (bel(x, l, r) <= (x * x <= 100)) and ((x * x <= 64) <= bel(x, l, r))


mx = 0
for l in range(-200, 200):
    for r in range(l + 1, 200):
        if all(f(x, l, r) for x in range(-200, 200)):
            mx = max(mx, r - l)

print(mx)