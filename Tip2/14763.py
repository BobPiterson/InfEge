def f(x, y, z):
    return (x or y) <= (y == z)


print('xyzv')
for x in range(2):
    for y in range(2):
        for z in range(2):
            v = int(f(x, y, z))
            if v == 0:
                print(z, x, y, v, sep='')
