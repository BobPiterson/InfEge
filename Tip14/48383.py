mn = 1e9
for x in range(9):
    v = int(f'88{x}4{x}', 9) + int(f'7{x}344', 9)
    if v % 67 == 0:
        mn = min(mn, v // 67)

print(mn)