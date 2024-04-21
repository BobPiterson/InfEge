from functools import reduce
def factorize(x):
    if x <= 1:
        return []

    l = {}
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            if i not in l:
                l[i] = 0
            l[i] += 1
            x //= i

    if x != 1:
        if i not in l:
            l[i] = 0
        l[i] += 1

    return l


print(reduce(lambda a, b: a * b, map(lambda a: a + 1, factorize(43125132514).values())))
