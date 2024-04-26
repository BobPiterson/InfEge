import sys

sys.stdin = open('inputs/28141.txt', 'r')

s, n = map(int, input().split())

files = [int(input()) for i in range(n)]
files.sort()

sm = 0
cnt = 0
for file in files:
    if sm + file > s:
        break
    sm += file
    cnt += 1

sm -= files[cnt - 1]
for idx, file in enumerate(files):
    if sm + file > s:
        break

print(cnt, files[idx - 1])

sys.stdin.close()
