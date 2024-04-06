from string import ascii_uppercase, digits


alp = digits + ascii_uppercase

mn = 1e9
for x in range(15):
    v = int(f'97968{alp[x]}13', 15) + int(f'7{alp[x]}213', 15)
    if v % 14 == 0:
        mn = min(mn, v // 14)

print(mn)
