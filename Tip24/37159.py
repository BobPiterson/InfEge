with open('inputs/24 (3).txt', 'r') as file:
    line = file.readline()

ans = 0
l = 0
for i in range(len(line) - 1):
    if sorted(line[i:i + 2]) == ["a", "d"]:
        ans = max(ans, i - l + 1)
        l = i + 1

ans = max(ans, len(line) - l)
print(ans)
