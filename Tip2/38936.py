def f(x, y, z, w):
    return (x == (not y)) <= ((x and w) == (z and (not w)))


print('xyzwv')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                v = int(f(x, y, z, w))
                if v == 0:
                    print(w, z, y, x, v, sep='')
