#f = open("D:/Downloads/26_17537.txt").readlines()
f = open("D:/Downloads/26.txt").readlines()
n = int(f[0].split()[0])
m = int(f[0].split()[1])
k = int(f[0].split()[2])
print(n,m,k)
#f.pop(0)
p = []
row = []
place = []
for i in range(1, len(f)):
    p.append([int(f[i].split()[0]), int(f[i].split()[1])])
    row.append(int(f[i].split()[0]))
    place.append(int(f[i].split()[1]))

#print(row[0], place[0])
# ряд и место
max_row = []
# Перебор мест j в ряду i 
for j in range(0, k-1):
        for i in range(0, m):
            print(p[i])
            # Если места в i-том ряду заняты
            if j in p[i] or (j+1) in p[i]:
                 # Сохраним номер ряда и занятые места в список
                 print(i, j)
                 max_row.append([i, j+1])
                 break
            
max_sort = sorted(max_row, reverse=True)
print(max_sort[0])          
