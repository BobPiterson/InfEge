# переберем все возможные варианты и выведем те из них, когда функция принимает значение "0"
print("x y z w")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if (((x <= y) == (y <= z)) and (y or w)) == 1:
                    print(x,y,z,w)




# from itertools import product, permutations
# from fnmatch import fnmatch
# from operator import ior
# from functools import reduce


# def f(x, y, z, w):
#     return ((x <= y) == (y <= z)) and (y or w)


# pats = ['0?0?', '00?0', '???0']
# for perm in permutations('xyzw', r=4):
#     d = dict({pat: set() for pat in pats})
#     for x, y, z, w in product(range(2), repeat=4):
#         v = int(f(x, y, z, w))
#         if v == 1:
#             vals = '{{{}}}{{{}}}{{{}}}{{{}}}'.format(*perm).format(x=x, y=y, z=z, w=w)
#             for pat in pats:
#                 if fnmatch(vals, pat):
#                     d[pat].add(vals)

#     if sum(len(set1) >= 1 for set1 in d.values()) == 3 and len(reduce(ior, [set1 for set1 in d.values()])) == 3:
#         print(*perm)
