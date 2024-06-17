from itertools import product


def f(x, y, z, w):
    return (not (x <= w)) or (y == z) or y


print('xyzwv')
for x, y, z, w in product(range(2), repeat=4):
    v = int(f(x, y, z, w))
    if v == 0:
        print(z, x, w, y, v, sep='')
