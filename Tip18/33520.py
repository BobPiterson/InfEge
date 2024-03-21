from pprint import pprint

with open('input.txt', 'r') as f:
    lines = list(map(lambda a: list(map(int, a.split())), f.readlines()))

h = len(lines)
w = len(lines[0])
dp = [[0 for x in range(w)] for y in range(h)]
pr = [[(-1, -1) for x in range(w)] for y in range(h)]
for x in range(h):
    for y in range(w):
        mx = 0
        idx = -1
        for y1 in range(0, y):
            if dp[x][y1] > 0:
                if dp[x][y1] > mx:
                    idx = y1
                    mx = dp[x][y1]

        dp[x][y] = mx + lines[x][y]
        pr[x][y] = (x, idx)

        mx = 0
        idx = -1
        for x1 in range(0, x):
            if dp[x1][y] > 0:
                if dp[x1][y] > mx:
                    idx = x1
                    mx = dp[x1][y]

        if mx + lines[x][y] > dp[x][y]:
            dp[x][y] = mx + lines[x][y]
            pr[x][y] = (idx, y)

pprint(dp)
pprint(pr)

path = []
p = (14, 14)
while p[0] != -1 and p[1] != -1:
    path.append(p)
    p = pr[p[0]][p[1]]
path.append((0, 0))

path.reverse()

for p in path:
    print(lines[p[0]][p[1]])
