def divisors(x):
    divs = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.add(i)
            divs.add(x // i)

    return sorted(divs)


for i in range(185311, 185331):
    divs = divisors(i)
    if len(divs) == 4:
        print(*divs)
