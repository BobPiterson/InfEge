# https://kompege.ru/variant
f = open('D:/Users/bobpi/Downloads/26_4336.txt').readlines()
f.pop(0)
m = []
for i in range(0, len(f)):
    m.append([int(f[i].split()[0]), int(f[i].split()[1])])
m.sort()
#print(m[0], m[1], '...', m[len(m) - 1])

start = []
stop = []
for i in m:
    start.append(i[0])
    stop.append(i[1])
#print('start = ', start)
#print('stop = ', stop)

pos = []
start_stop = []
for i in range(86400):
    if i % 1000 == 0: print(i // 1000)
    for k in range(start.count(i)):
        pos.append(i)
        if len(pos) == 1:
            start_stop.append(i)

    for k in range(stop.count(i)):
        pos.pop(0)
        if len(pos) == 0:
            start_stop.append(i)
start_stop.pop(0)
#print(len(start_stop))
#print(start_stop)
summa = 0
i = 0
while i < len(start_stop) - 2:
    summa = summa + (start_stop[i + 1] - start_stop[i])
    i += 2
print(len(start_stop) // 2, summa)