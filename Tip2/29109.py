def f(x, y, z, w):
    return ((z <= w) or (y == w)) and ((x or z) == y)


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                v = int(f(x, y, z, w))
                if v == 1:
                    print(x, y, z, w, v, sep='')

'''

0110
*10*
0**1

'''