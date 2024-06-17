def divs(x):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            if x // i != i:
                d.append(x // i)

    return sorted(d)


for i in range(210235, 210301):
    d = divs(i)
    if len(d) == 4:
        print(*d)
