mn = 1e9
for x in range(9):
    for y in range(9):
        v = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
        if v % 61 == 0:
            mn = min(mn, v // 61)

print(mn)