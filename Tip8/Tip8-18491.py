# 18491
# Ольга составляет 5-⁠буквенные коды из букв О, Л, Ь, Г, А. Каждую букву нужно использовать ровно 1 раз,
# при этом Ь нельзя ставить первым и нельзя ставить после гласной. Сколько различных кодов может составить Ольга?
#
m = []
alf = 'ОЛЬГА'
for a in 'ОЛГА':
    for b in alf:
        for c in alf:
            for d in alf:
                for e in alf:
                    s = set()
                    s.add(a)
                    s.add(b)
                    s.add(c)
                    s.add(d)
                    s.add(e)
                    tmp = a+b+c+d+e
                    if len(s) == 5 and tmp.count('ОЬ') == 0 and tmp.count('АЬ') == 0:
                        m.append(tmp)
print(m)
print('Ответ =', len(m))
# Ответ = 48

