with open('inputs/24_58327.txt', 'r') as file:
    line = file.readline()

cnt = 0
ans = 0
for i in range(len(line) - 1):
    if int(line[i]) >= int(line[i + 1]):
        cnt += 1
        ans = max(ans, cnt + 1)
    else:
        cnt = 0

print(ans)

