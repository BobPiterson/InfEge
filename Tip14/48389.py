mn = 1e9
for x in range(7):
    for y in range(7):
        v = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if v % 181 == 0:
            mn = min(mn, v // 181)

print(mn)