f = open('D:/downloads/17_17530.txt').readlines()
#print(f[0])
m = 1e10
for s in f:
    if m > int(s):
        m = int(s)
print ('min = ', m)
count = 0
minsum = 1e10

for i in range(len(f) - 2):
    if int(f[i]) % 55 == m or int(f[i + 1]) % 55 == m:
        count += 1
        if minsum > int(f[i]) + int(f[i + 1]):
            minsum = int(f[i]) + int(f[i + 1])

print (count, ', ', minsum)
