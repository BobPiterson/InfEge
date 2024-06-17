with open('inputs/24.txt', 'r') as file:
    line = file.readline()

mx = 0
cnt = 0
for i in range(len(line) - 1):
    if line[i] != line[i + 1]:
        cnt += 1
        mx = max(mx, cnt + 1)
    else:
        cnt = 0

print(mx)
