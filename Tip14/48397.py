from string import digits, ascii_uppercase

alp = digits + ascii_uppercase

mn = 1e9
for x in range(13):
    v = int(f'8{alp[x]}71', 13) + int(f'3{alp[x]}DF', 17)
    if v % 197 == 0:
        mn = min(mn, v // 197)

print(mn)
