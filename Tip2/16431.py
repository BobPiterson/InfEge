from itertools import product


def f(x, y, z, w):
    return (y <= x) == (x <= w) and (z or x)


print(*'xyzw', sep=' ')
for x, y, z, w in product(range(2), repeat=4):
    v = int(f(x, y, z, w))
    if v == 1:
        print(x, y, z, w, sep=' ')
