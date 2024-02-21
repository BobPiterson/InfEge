# https://kompege.ru/variant
#f = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/26_4336.txt').readlines()
f = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/26_tmp.txt').readlines()
f.pop(0)
m = []
for i in range(0, len(f)):
    m.append([int(f[i].split()[0]), int(f[i].split()[1])])
#print(m[0], m[1], '...', m[len(m) - 1])
m.sort()
#print(m[0], m[1], '...', m[len(m) - 1])
#print(m)

max_start = 0
max_stop = 0
for i in m:
    if i[0] > max_start:
        max_start = i[0]
    if i[1] > max_stop:
        max_stop = i[1]
#print(max_start, max_stop)

start = []
stop = []
for i in m:
    start.append(i[0])
    stop.append(i[1])
print('start = ', start)
print('stop = ', stop)

pos = []
start_stop = []
max_stop = 0
for j in range(len(m)):
    for i in range(j, len(m)):
        if stop[i] >= max_stop:
            max_stop = stop[i]
            if start[i] < stop[j]:
                pos.append(start[i])
            else:
                if len(pos) != 0:
                    pos.pop(len(pos)-1)
                    if len(pos) == 0:
                        start_stop.append(max_stop)
                else:
                    break
            print(max_stop, pos)
print(start_stop)

# start = 0
# stop = 0
# start_stop = []
# for i in range(len(m)):
#     for j in range(i, len(m)):
#         if m[i][1] < m[j][0]:
#             if m[j][0] > stop:
#                 if m[i][1] > start:
#                     start = m[i][1]
#                     stop = m[j][0]
#                     start_stop.append([start, stop])
#                     print(start, stop)
#                     break

#print(start_stop)