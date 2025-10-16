# 3230
# Все 5-⁠буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Вот начало списка:
#
#1.  ААААА
#2.  ААААК
#3.  ААААР
#4.  ААААУ
#5.  АААКА
#...
# 
#Укажите номер слова УКАРА.

alf = 'АКРУ'
count = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    res = x1+x2+x3+x4+x5
                    count += 1
                    if count <= 5:
                        print(count, res)
                    if res == 'УКАРА':
                        print('Ответ =', count)
                        exit()
# Ответ = 841