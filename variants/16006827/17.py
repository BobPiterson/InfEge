with open('inputs/17.txt', 'r') as file:
    arr = list(map(int, file.readlines()))

l = list(filter(lambda x: x % 2 == 0, arr))
sr = sum(l) / len(l)

cnt = 0
mx = -1e9
for i in range(len(arr) - 1):
    if (arr[i] % 3 == 0 or arr[i + 1] % 3 == 0) and (arr[i] < sr or arr[i + 1] < sr):
        cnt += 1
        mx = max(mx, arr[i] + arr[i + 1])

print(cnt, mx)
