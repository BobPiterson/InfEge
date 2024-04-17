with open('zadanie24_1.txt', 'r') as file:
    line = file.readline()

ans = 0
c = 0
for i in range(len(line)):
    if line[i] == 'A':
        c += 1
        ans = max(ans, c)
    else:
        c = 0

print(ans)
