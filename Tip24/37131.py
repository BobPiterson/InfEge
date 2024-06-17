with open('inputs/24 (4).txt', 'r') as file:
    line = file.readline()

ans = 0
cnt = 0
for i in range(len(line) - 1):
    if line[i:i + 2] != "KL" and line[i:i + 2] != "LK":
        cnt += 1
        ans = max(ans, cnt + 1)
    else:
        cnt = 0

print(ans)
