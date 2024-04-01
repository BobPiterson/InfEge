mn = 1e9
for c1 in range(50):
    for c2 in range(50):
        for c3 in range(50):
            for c4 in range(50):
                if c1 * 2 + c3 == c2 * 2 + c4 and c2 + c4 * 2 == 40 and c1 + c3 * 2 > 50:
                    mn = min(mn, c1 + c3 * 2)

print(mn)
