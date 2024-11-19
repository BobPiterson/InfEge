f = open("C:/Users/vngorlachev/Documents/15.Материалы ЕГЭ/скаченные файлы/17.txt").read().split()
#print(f[0])
#print(len(f))
# найдем квадрат максимального элемента последовательности, оканчивающегося на 3
kvad_max_3 = 0
for s in f:
    if s[len(s)-1::] == '3':
        if kvad_max_3 < int(s) ** 2:
            kvad_max_3 = int(s) ** 2
#print('квадрат максимального элемента последовательности = ', kvad_max_3)

count = 0
max_summ_kvad = 0
# Проверим все пары на выполнение условий задачи:
# 1) если первый элемент пары заканчивается на "3", то второй не должен заканчиваться на "3"
# 2) если второй элемент пары заканчивается на "3", то первый не должен заканчиваться на "3"
# 3) сумма квадратов элементов должна быть не меньше квадрата максимального элемента последовательности
for i in range(0, len(f) - 1):
    if ((f[i][len(f[i])-1::] == '3' and f[i + 1][len(f[i+1])-1::] != '3') or \
    (f[i][len(f[i])-1::] != '3' and f[i + 1][len(f[i+1])-1::] == '3')) and \
    int(f[i]) ** 2 + int(f[i + 1]) ** 2 >= kvad_max_3:
        count += 1
        if max_summ_kvad < (int(f[i]) ** 2 + int(f[i + 1]) ** 2):
            max_summ_kvad = int(f[i]) ** 2 + int(f[i + 1]) ** 2

print('Пар = ', count, ', максимальная из сумм квадратов элементов пары = ', max_summ_kvad)

