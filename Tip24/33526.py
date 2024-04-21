with open('24.txt', 'r') as file:
    line = file.readline()

d = {}
for i in range(len(line) - 2):
    if line[i] == line[i + 2]:
        if line[i + 1] not in d:
            d[line[i + 1]] = 0
        d[line[i + 1]] += 1

print(max(d, key=lambda x: d[x]))
