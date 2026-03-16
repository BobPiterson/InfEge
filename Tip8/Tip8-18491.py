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
<<<<<<< HEAD
                    kod = a+b+c+d+e
                    if kod.count('О') == 1 and kod.count('Л') == 1 and kod.count('Ь') == 1 and kod.count('Г') == 1 and kod.count('А') == 1 and kod.count('ОЬ') == 0 and kod.count('АЬ') == 0:
                        m.append(kod)
print(m)
print('Ответ =', len(m))
# Ответ = 48
=======
                    if len({a,b,c,d,e}) == 5 and (a+b+c+d+e).count('ОЬ') == 0 and (a+b+c+d+e).count('АЬ') == 0:
                        m.append((a+b+c+d+e))
print(m)
print('Ответ =', len(m))
# Ответ = 48
>>>>>>> 0e8fb460031eca4322e90a46e1b095723d105e7e
