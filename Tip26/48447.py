import sys

sys.stdin = open('inputs/26.txt', 'r')

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

arr2 = arr[:]
cnt = 0
mx = 0
while len(arr2) > 0:
    d = [0]
    for i in range(len(arr2)):
        if abs(arr2[d[-1]] - arr2[i]) >= 5:
            d.append(i)

    d.sort(reverse=True)
    for i in d:
        arr2.pop(i)

    mx = max(mx, len(d))
    cnt += 1

print(cnt, mx)

sys.stdin.close()
