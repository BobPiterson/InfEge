with open('inputs/2.txt', 'r') as file:
    arr = list(map(int, file.readlines()))

mn = 1e9
for a in arr:
    if a % 21 == 0:
        mn = min(mn, a)


cnt = 0
mx = -1
for i in range(len(arr) - 1):
    if arr[i] % mn == 0 or arr[i + 1] % mn == 0:
        cnt += 1
        mx = max(mx, arr[i] + arr[i + 1])


print(cnt, mx)
