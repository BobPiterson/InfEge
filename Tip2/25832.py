from fnmatch import fnmatch
from random import shuffle


def f(x, y, z, w):
    return (x and (not y)) or (x == z) or (not w)


s = set()
vs = ['x', 'y', 'z', 'w']
while len(s) != 3:
    s.clear()
    shuffle(vs)
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    v = int(f(x, y, z, w))
                    if v == 0:
                        expr = '{{{}}}{{{}}}{{{}}}{{{}}}'.format(*vs).format(x=x, y=y, z=z, w=w)
                        if fnmatch(expr, '??00') or fnmatch(expr, '1110') or fnmatch(expr, '10??'):
                            s.add(expr)
print(s)
print(*vs, sep='')
