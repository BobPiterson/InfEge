with open('input.txt', 'r') as f:
    lines = list(map(lambda a: list(map(int, a.split())), f.readlines()))

cnt = 0
for line in lines:
    m = max(line)

    flag = False
    for x in line:
        if line.count(x) > 1:
            flag = True
            break

    sa = (sum(line) - m) / 5 * 3
    if line.count(m) == 1 and flag and m > sa:
        cnt += 1

print(cnt)
