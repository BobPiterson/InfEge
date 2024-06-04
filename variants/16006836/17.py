with open('inputs/17.txt', 'r') as file:
    arr = list(map(int, file.readlines()))

mn = 1e9
for x in arr:
    if str(x)[-1] == '3':
        mn = min(mn, x)

mn = mn * mn
cnt = 0
mx = -1e9

for i in range(len(arr) - 1):
    if str(min(arr[i], arr[i + 1]))[-1] == '3' and (arr[i] * arr[i] + arr[i + 1] * arr[i + 1]) < mn:
        cnt += 1
        mx = max(mx, arr[i] * arr[i] + arr[i + 1] * arr[i + 1])

print(cnt, mx)
