# https://inf-ege.sdamgia.ru/problem?id=60266
f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/24_2024.txt").read().split()
s = f[0]
max_len = 0
for i in range(len(s)):
    count = 0
    j = 0
    while i + j < len(s):
        if s[i + j] == 'T':
            count += 1
        if count == 100:
            lens = j + 1
            break
        j += 1
    if max_len < lens:
        max_len = lens
print(max_len)