f = open("D:/Downloads/24_17535.txt").read()
#print(f.count('CD' * 160))
first = 0
count = 0
max = 0
for i in range(len(f)-1):
    if f[i] == 'C' and f[i+1] == 'D' and first == 0:
        first = i
        
    if f[i] == 'C' and f[i+1] == 'D' and first != 0:
        count += 1
        if count == 160:
            print(count)
            if i - first > max:
                max = i - first
                count = 0
                first = i

print(count, max)

