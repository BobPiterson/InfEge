# https://inf-ege.sdamgia.ru/problem?id=60268
import sys
sys.setrecursionlimit(14000)

f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/26_2024.txt").readlines()
#print(f[0])
m = []
for i in range(1, len(f)):
    m.append([int(f[i].split()[0]), int(f[i].split()[1])])
#print(m[0])
m.sort()
#print(m)
#print(m[0][0], m[0][1])
start = []
stop = []
for i in range(len(m)):
    start.append(m[i][0])
    stop.append(m[i][1])
#print(start[0], stop[0])
print('--------------------------------------------------------')
select = []
max_merop = 0
max_perer = 0
select2 = []
def rek(d, k):
    global select
    global max_merop
    global max_perer
    if k < len(m):
        #print(d, k, start[k], stop[d])
        if start[k] >= stop[d]:
            select.append([start[k], stop[k]])
            #print(select)
            if len(select) >= max_merop:
                max_merop = len(select)
                #select2.append(list(select))
                #print(select)
            rek(k, d)
        rek(d, k + 1)
    else:
        select.pop()
        return(k)

for d in range(len(m)):
    print(d)
    select.append([start[d], stop[d]])
    rek(d, d)


# for i in range(len(select2)):
#     for j in range(len(select2[i])-1):
#         if len(select2[i]) == max_merop and select2[i][j + 1][0] - select2[i][j][1] > max_perer:
#             max_perer = select2[i][j + 1][0] - select2[i][j][1]
#             print(select2[i])


print(max_merop, max_perer)





