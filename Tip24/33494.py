with open('inputs/24 (2).txt', 'r') as file:
    line = file.readline()

cnt = {}

for i in range(len(line) - 1):
    if line[i] == 'E':
        if line[i + 1] not in cnt:
            cnt[line[i + 1]] = 0
        cnt[line[i + 1]] += 1

print(max(cnt, key=lambda x: cnt[x]))
