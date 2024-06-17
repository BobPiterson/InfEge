from itertools import product


def f(x, y, z, w):
    return ((x <= y) == (z <= w)) or (x and w)


print('xyzw')
for x, y, z, w in product(range(2), repeat=4):
    v = int(f(x, y, z, w))
    if v == 0:
        print(z, y, x, w, sep='')
