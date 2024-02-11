# Решение части А - полный перебор
k = 113
f = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/27-B_12257.txt').read().split()

f.pop(0)
lenf = len(f)
# переворот, если слишком долго выполняется
#f.reverse()

max_len = 0
max_summa = 0
for i in range(len(f)):
    summa = 0
    for j in range(i, len(f)):
        summa = summa + int(f[j])
        if summa % k == 0 and summa > max_summa:
            max_summa = summa
            if max_len < j - i + 1:
                max_len = j - i + 1
        if j % 100000 == 0: print('-------------------', i, j, max_summa, max_len)
    # если мы уже нашли такую длинную подстроку, что все остальные короче, можно закончить цикл
    if max_len > lenf - i:
        break

print(max_summa, max_len)


