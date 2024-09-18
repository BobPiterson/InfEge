min_a = 100000
for a0 in range(5, 65):
    for a1 in range(a0, 67):
        for x in range(0, 100):
            f = (x >= 15 and x <= 40) <= (((x >= 21 and x <= 63) and not (x >= a0 and x <= a1)) <= (not (x >= 15 and x <= 40)))
            if f:
                print(a0, a1)
                if (a1 - a0) < min_a:
                    min_a = a1 - a0

print(min_a)

