mn = 1e9
for x in range(1000, 10000):
    N = str(x)
    l = int(N[0]) * int(N[1])
    r = int(N[2]) * int(N[3])
    R = str(max(l, r)) + str(min(l, r))

    if R == '124':
        mn = min(mn, x)

print(mn)