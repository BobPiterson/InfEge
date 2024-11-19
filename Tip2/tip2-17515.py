def f(w,x,y,z):
    fun = not(x <= w) or (y <= z) or not (y)
    return fun

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not (f(w,x,y,z)):
                    print(w,x,y,z, '  F = ', f(w,x,y,z))

