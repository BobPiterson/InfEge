def divs(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)

    return sorted(d)


mx = 0
ans = 0
for i in range(84052, 84131):
    d = divs(i)
    if len(d) > mx:
        mx = len(d)
        ans = i

print(len(divs(ans)), ans)
