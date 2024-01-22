s = ['a', 'b', 'c', 'd']
set1 = set()
set2 = set()
k = 0
for a1 in s:
    for b1 in s:
        for c1 in s:
            for d1 in s:
                set1.add(a1)
                set1.add(b1)
                set1.add(c1)
                set1.add(d1)
                if len(set1) == len(s):
                    m = a1+b1+c1+d1
#                    print(a1, b1, c1, d1)
                    set2.add(m)
                    k += 1
                set1 = set()
print(sorted(set2))
print('Общее количество комбинаций: ',k)
