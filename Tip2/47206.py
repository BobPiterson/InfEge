from itertools import product


def f(x, y, z, w):
    return not (y <= x) or (z <= w) or not z


print('xyzwv')
for x, y, z, w in product(range(2), repeat=4):
    v = int(f(x, y, z, w))
    if v == 0:
        print(x, y, z, w, v, sep='')
