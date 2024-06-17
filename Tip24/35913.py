with open('24.txt', 'r') as file:
    lines = file.readlines()

l = sorted(list((line, line.count('N')) for line in lines), key=lambda x: x[1])[0][0]
d = {}
for i in range(len(l)):
    if l[i] not in d:
        d[l[i]] = 0
    d[l[i]] += 1

print(max(d, key=lambda x: d[x]))
