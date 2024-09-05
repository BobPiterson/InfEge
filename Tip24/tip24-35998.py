f = open('C:/Users/vngorlachev/Documents/15.Материалы ЕГЭ/скаченные файлы/inf_26_04_21_24.txt').read().split()
#print(f[0])
#print(len(f))
maxlen = 0
# Переберем все строки
for s in f:
    # найдем строки, в которых количество символов "А" меньше 25
    if s.count('A') < 25:
        # переберем все символы в найденной строке
        for c in s:
            # если разница между номерами последнего и первого вхождения символа больше "maxlen", сохраняем
            if s.rfind(c) - s.find(c) > maxlen:
                maxlen = s.rfind(c) - s.find(c)
print(maxlen)


