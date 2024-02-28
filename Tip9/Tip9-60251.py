# https://inf-ege.sdamgia.ru/problem?id=60251
f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/9_2024.txt").readlines()
#print(f[0].split())
print(len(f))
s = set()
count_repeat = 0
count_string = 0
len_string = len(f[0].split())
for i in range(len(f)):
    count_repeat = 0
    summa1 = 0
    summa2 = 0
    for k in range(0, len_string):
        summa1 += int(f[i].split()[k])
        for m in range(k+1, len_string):
            if f[i].split()[k] == f[i].split()[m]:
                summa2 += int(f[i].split()[m])
                #print(f[i].split()[k],f[i].split()[m])
                count_repeat += 1
    sred1 = summa1 / 7
    sred2 = summa2 / 2
    if count_repeat == 2 and sred2 < sred1:
        count_string += 1

print(count_string)

