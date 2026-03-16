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
                    kod = a+b+c+d+e
                    if kod.count('О') == 1 and kod.count('Л') == 1 and kod.count('Ь') == 1 and kod.count('Г') == 1 and kod.count('А') == 1 and kod.count('ОЬ') == 0 and kod.count('АЬ') == 0:
                        m.append(kod)
print(m)
print('Ответ =', len(m))
# Ответ = 48
