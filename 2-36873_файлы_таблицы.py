#
import time
n = 15
count = 0
m = []
fixsum = 0
def way(fixsum, maxs, pointsum, x,y):
    if x < n and y < n:
        if pointsum < m[x][y]:
            pointsum = m[x][y]
            maxs = maxs + pointsum
        #print(x, y, m[x][y], fixsum, maxs, pointsum)
        #time.sleep(1)
        fixsum, maxs = way(fixsum, maxs, pointsum, x+1, y)
        fixsum, maxs = way(fixsum, maxs, pointsum, x, y+1)
    if (x == n-1) and (y == n-1):
        fixsum = max(fixsum, maxs)
        #print(fixsum)
        #maxs = maxs - pointsum
    return fixsum, maxs


with open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/Новый план/inf_26_04_21_18.txt') as file:
    for line in file:
        s = line.split()
        #добавлять в конец списка: 
        #m.append(s)
        #добавлять в начало списка:
        m.insert(0,s)
    # Преобразовать строковые в int
    for i in range(n):
        for j in range(n):
            m[i][j] = int(m[i][j])

#print(m)

fixsum, maxsumma = way(m[0][0], m[0][0], m[0][0], 1, 0)
fixsum2, maxsumma = way(m[0][0], m[0][0], m[0][0], 0, 1)

print (max(fixsum, fixsum2))

