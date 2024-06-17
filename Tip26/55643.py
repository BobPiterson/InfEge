import sys

sys.stdin = open('inputs/55643.txt', 'r')

n = int(input())

lines = [tuple(map(int, input().split())) for i in range(n)]

d = dict()
for x, y in lines:
    if x not in d:
        d[x] = set()
    d[x].add(y)

for key in d.keys():
    d[key] = sorted(d[key])

mx = 0
ans = 0
for key, val in d.items():
    l = 0
    for i in range(len(val) - 1):
        if abs(val[i + 1] - val[i]) > 8:

            cnt = val[i] - val[l] + 1
            if cnt > mx:
                mx = cnt
                ans = key

            l = i + 1

    cnt = val[len(val) - 1] - val[l] + 1
    if cnt > mx:
        mx = cnt
        ans = key


print(mx, ans)
sys.stdin.close()
