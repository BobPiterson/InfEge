with open('24_demo.txt', 'r') as file:
    line = file.readline()

ans = 0
idx = 0
c = 0
substr = 'XYZ'
for i in range(len(line)):
    if line[i] == substr[idx]:
        c += 1
        idx = (idx + 1) % 3
        ans = max(ans, c)
    else:
        c = 0
        idx = 0

print(ans)
