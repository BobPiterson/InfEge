def f(x, y, z, w):
    return (x == (not y)) <= (z == (y or w))


print('xyzw')
# print('zxyw')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                v = int(f(x, y, z, w))
                if v == 0:
                    print(z, w, y, x, v, sep='')
