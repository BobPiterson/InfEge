#
m = []
with open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/28133_B.txt') as file:
    for line in file:
        m.append(int(line.split()[0]))
# удалим из списка первый элемент, полученный из первой строки файла
m.pop(0)
#print(m)
maxsumma = 0
item1 = 0
item2 = 0

for i in range(len(m)-1):
    for j in range(i+1, len(m)):
        if m[i] > m[j] and (m[i] + m[j]) % 120 == 0 and maxsumma < m[i] + m[j]:
            maxsumma = m[i] + m[j]
            item1 = m[i]
            item2 = m[j]

print(item1, item2)

