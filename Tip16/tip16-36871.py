def f(n):
    if n == 0:
        return(0)
    else:
        if n > 0 and n % 2 == 0:
            return(f(n / 2))
        else:
            return(1 + f(n - 1))

count = 0
for n in range(1, 1001):
    if f(n) == 3:
        count += 1

print(count)