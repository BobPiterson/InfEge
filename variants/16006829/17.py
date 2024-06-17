with open('inputs/17.txt', 'r') as file:
    arr = list(map(int, file.readlines()))

cnt = 0
mx = -1e9

for x in range(len(arr)):
    for y in range(x + 1, len(arr)):
        if (arr[x] + arr[y]) % 8 == 0:
            cnt += 1
            mx = max(mx, arr[x] + arr[y])

print(cnt, mx)

