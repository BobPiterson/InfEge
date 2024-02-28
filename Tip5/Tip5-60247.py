# https://inf-ege.sdamgia.ru/problem?id=60247
r_min = 1e9
for n in range(0, 1000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-3:]
    else:
        ost = n % 3
        b = b + bin(ost * 3)[2:]
    r = int(b,2)
    if r > 151 and r < r_min:
        r_min = r
        print(n, int(b,2))

