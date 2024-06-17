with open('inputs/24 (1).txt', 'r') as file:
    line = file.readline()

l = 0
ans = 0
for i in range(len(line) - 2):
    if sorted(line[i:i + 3]) == ["A", "B", "C"]:
        ans = max(ans, i - l)
        l = i + 3

print(ans)
