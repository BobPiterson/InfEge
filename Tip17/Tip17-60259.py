# https://inf-ege.sdamgia.ru/problem?id=60259
f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/17_2024.txt").read().split()
count = 0
max_summ = 0
max_13 = 0
for i in f:
    if int(i) > max_13 and i[-2:] == '13':
        max_13 = int(i)
#print(max_13)
for i in range(len(f) - 2):
    a = len(f[i])
    b = len(f[i + 1])
    c = len(f[i + 2])
    if (a == 3 and b == 3 and c != 3) or (b == 3 and c == 3 and a != 3) or (c == 3 and a == 3 and b != 3):
        summa = int(f[i]) + int(f[i + 1]) + int(f[i + 2])
        if summa <= max_13:
            count += 1
            if summa > max_summ:
                max_summ = summa
print(count, max_summ)
