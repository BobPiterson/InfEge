from itertools import product


def f(x, y, z, w):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))


print('xyzwv')
for x, y, z, w in product(range(2), repeat=4):
    v = int(f(x, y, z, w))
    if v == 0 or (v == 1 and (x + y + z + w == 3)):
        print(y, z, x, w, v, sep='')

'''
1 1 1 0 1
1 1 0 0 0
1 0 1 1 0
'''
