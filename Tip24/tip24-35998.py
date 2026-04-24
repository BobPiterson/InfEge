f = open(r"C:\Users\vngorlachev\Downloads\35998.txt").readlines()
#print(f[0])
#print(len(f))
maxlen = 0
# Переберем все строки
for s in f:
    # найдем строки, в которых количество символов "А" меньше 25
    if s.count('A') < 25:
        # переберем все символы в найденной строке
        for h in s:
            # максимальная разница между номерами последнего и первого вхождения символа:
            maxlen = max(maxlen, s.rfind(h) - s.find(h))
print('Ответ:', maxlen)
# Ответ: 1004