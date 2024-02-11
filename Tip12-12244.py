def sum(s):
    result = 0
    for i in s:
        result = result + int(i)
    return result

summa = 0
s_fine = ''
for n in range(3, 10001):
    if n % 1000 == 0: print(n)
    s = '3' + n * '5'
    while '555' in s or '333' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    if summa < sum(s):
        summa = sum(s)
        s_fine = s

print(summa, s_fine)