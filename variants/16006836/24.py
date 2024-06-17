with open('inputs/24.txt', 'r') as file:
    line = file.readline()

line = line.replace('A', '*').replace('B', '*').replace('C', '*')

mx = 0
cnt = 0
for i in range(len(line) - 1):
    if line[i] == '*' and line[i + 1] == '*':
        cnt = 0
    else:
        cnt += 1
        mx = max(mx, cnt + 1)

print(mx)
