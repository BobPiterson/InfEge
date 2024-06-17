with open('inputs/24 (5).txt', 'r') as file:
    line = file.readline()

pos = []
ans = 1e9
for i in range(len(line)):
    if line[i] == 'U':
        pos.append(i)
        if len(pos) >= 110:
            ans = min(ans, i - pos[len(pos) - 110] + 1)

print(ans)

