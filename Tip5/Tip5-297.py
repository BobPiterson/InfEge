# https://kompege.ru/variant
def func(n):
    s10 = str(n) + str(n)[-1]
    s2 = bin(int(s10))[2:]
    if s2.count('1') % 2 == 0:
        s2 = s2 + '0'
    else:
        s2 = s2 + '1'
    return int(s2, 2)

min_n = 10e6
for i in range(1000):
    if func(i) > 413:
        if i < min_n:
            min_n = i
print(min_n)

