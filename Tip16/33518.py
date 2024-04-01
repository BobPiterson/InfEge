def f(n):
    if n == 0:
        return 0

    if n % 2 == 0:
        return f(n // 2)

    return 1 + f(n - 1)


print(bin(4095)[2:])
for n in range(10000):
    if f(n) == 12:
        print(n)
        break
