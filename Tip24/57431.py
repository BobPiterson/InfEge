# with open("inputs/1_24.txt", "r") as file:
#     line = file.readline()
#
# ans = 0
# l = 0
# for i in range(len(line) - 1):
#     s = line[i:i + 2]
#     if s.count('A') + s.count('B') + s.count('C') == 2:
#         ans = max(ans, i - l + 1)
#         l = i + 1
#
# ans = max(ans, len(line) - l)
# print(ans)

with open("inputs/1_24.txt", "r") as file:
    line = file.readline()

ans = 0
c = 0
for i in range(len(line) - 1):
    if line[i] not in "ABC" or line[i + 1] not in "ABC":
        c += 1
        ans = max(ans, c + 1)
    else:
        c = 0

print(ans)
