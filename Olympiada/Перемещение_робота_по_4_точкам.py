from itertools import permutations
from math import sqrt

points = []
for i in range(4):
    x, y = input().split()
    x = float(x[0:-1])
    y = float(y)
    points.append((x, y))

print(points)
print(points[0], points[1], points[2], points[3])

def dist(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_path_time(path):
    all_d = 0
    all_t = 0

    # 1 - 2
    d = dist(path[0], path[1])
    all_d += d

    a = 2
    t = sqrt(2 * d / a)
    all_t += t

    # 2 - 3
    d = dist(path[1], path[2])
    all_d += d
    
    v = 4
    t = d / v
    all_t += t

    # 3 - 4
    d = dist(path[2], path[3])
    all_d += d

    a = -1
    disc = v ** 2 + 2 * a * d
    t = (-v + sqrt(disc)) / a 
    all_t += t

    return all_d, all_t
   

# print(find_path_time([(1, 0), (2, 0), (4, 0), (7, 0)]))

# min_t = 1e9
# min_d = 1e9
# for i in permutations('012345', r=4):
#     str_path = ''.join(i)

#     path = []
#     for s in str_path:
#         path.append(points[int(s)])

#     d, t = find_path_time(path)
    
#     if d < min_d:
#         min_d = d
#         min_t = t

# print(round(min_d, 2))
# print(round(min_t, 2))

def sqr_eq(a, b, c):
    d = b ** 2 - 4 * (a * c)
    if d < 0: print ('Решения квадратного уравнения не существует')
    if d == 0: return((-b) / (2 * a))
    if d > 0:
        x1 = ((-b + sqrt(d)) / (2 * a))
        x2 = ((-b - sqrt(d)) / (2 * a))
        print('t1, t2 = ', x1, x2)
        return(min(x1, x2))

print(dist(points[0], points[1]) +  dist(points[1], points[2]) + dist(points[2], points[3]))
t12 = sqrt(2 * dist(points[3], points[2]) / 2)
t23 = dist(points[2], points[1]) / 4
t34 = sqr_eq(-0.5, 4, -dist(points[1], points[0]))
print('t12 = ', t12)
print('t23 = ', t23)
print('t34 = ', t34)
print('summa = ', t12 + t23 + t34)