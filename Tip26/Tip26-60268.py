# https://inf-ege.sdamgia.ru/problem?id=60268
f = open("D:/Users/bobpi/Downloads/26_2024_tmp.txt").readlines()
#print(f[0])
m = []
for i in range(1, len(f)):
    m.append([int(f[i].split()[0]), int(f[i].split()[1])])
#print(m[0])
m.sort()
print(m)
#print(m[0][0], m[0][1])
start = []
stop = []
for i in range(len(m)):
    start.append(m[i][0])
    stop.append(m[i][1])
#print(start[0], stop[0])

# def kolvo(i: int, count: int) -> int:
#     if stop[i] in start:
#         print('---', stop[i], start.index(stop[i]), count)
#         kolvo(start.index(stop[i]), count + 1)
#     else:
#         print('return:', count)
#         return count


count = 0
for i in range(len(m)):
    for j in range()





