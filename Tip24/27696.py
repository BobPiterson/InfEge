with open('inputs/zadanie24_2.txt', 'r') as file:
    line = file.readline()

ans = 0
cnt = 0
for i in range(len(line)):
    if line[i] == 'L':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)


