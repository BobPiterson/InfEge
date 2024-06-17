from itertools import product

cnt = 0
for i in product('ЕГЭ', repeat=5):
    x = ''.join(i)
    if x[0] != 'Г':
        cnt += 1

print(cnt)
