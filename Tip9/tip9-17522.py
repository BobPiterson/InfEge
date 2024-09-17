f = open('D:/downloads/9_17522.txt').readlines()
print(len(f))
print(f[0])
m = [[]]
for i in range(len(f)):
    m[i].append(f[i].split())

print(m[0], m[0][0])  
