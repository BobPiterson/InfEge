with open('inputs/1.txt') as file:
    lines = list(map(int, file.readlines()))

mx = 0
for a in lines:
    if abs(a) % 10 == 3:
        mx = max(mx, a * a)

cnt = 0
mx2 = 0
for i in range(len(lines) - 1):
    if (int(abs(lines[i]) % 10 == 3) + int(abs(lines[i + 1]) % 10 == 3)) == 1 and lines[i] ** 2 + lines[i + 1] ** 2 >= mx:
        cnt += 1
        mx2 = max(mx2, lines[i] ** 2 + lines[i + 1] ** 2)

print(cnt, mx2)
