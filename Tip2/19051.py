def f(x, y, z, w):
    return (x and (not y)) or (x == z) or (not w)


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                v = int(f(x, y, z, w))
                if v == 0:
                    print(x, w, z, y, v, sep='')