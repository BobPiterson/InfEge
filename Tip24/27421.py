with open('inputs/24_demo.txt', 'r') as file:
    line = file.readline()


ans = 0
cnt = 0
for i in range(len(line) - 1):
    if line[i] != line[i + 1]:
        cnt += 1
        ans = max(ans, cnt + 1)
    else:
        cnt = 0

print(ans)
