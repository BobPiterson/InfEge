from itertools import permutations
from math import sqrt, dist

points = list([tuple(map(float, input().split(', '))) for i in range(6)])
variants = list(permutations(points, 4))
results = []

for element in variants:
    dist_1 = dist(element[0], element[1])
    dist_2 = dist(element[1], element[2])
    dist_3 = dist(element[2], element[3])

    t_1 = sqrt(dist_1)
    t_2 = dist_2 / 4
    t_3_1 = -4 + (16 + 2 * dist_3) ** 0.5
    t_3_2 = -4 - (16 + 2 * dist_3) ** 0.5

    if t_3_1 >= 0 >= t_3_2:
        t_3 = t_3_1
    elif t_3_2 >= 0 >= t_3_1:
        t_3 = t_3_2
    else:
        if 4 - t_3_1 < 0:
            t_3 = t_3_2
        elif 4 - t_3_2 < 0:
            t_3 = t_3_1
        else:
            t_3 = min(t_3_1, t_3_2)

    # t_3 = min(t_3_1, t_3_2)        
    results.append((dist_1 + dist_2 + dist_3, t_1 + t_2 + t_3))

answer = min(results, key=lambda x: x[1])
print((str(abs(round(answer[0], 2))) + '0000')[:4])
print((str(abs(round(answer[1], 2))) + '0000')[:4])
