# Дан файл формата Excel с 12000 строк по 7 чисел в каждой строке
# Определить количество строк, для которых выполняются условия:
# 1) в строке есть ровно 3 числа, каждое из которых повторяется дважды
# и одно число, которое не повторяется
# 2) среднее арифметическое минимального и максимального среди повторяющихся
# чисел строки меньше неповторяющегося числа.

# сохраним файл xls в текстовом формате с разметкой символами табуляции

s = []
count = 0
file = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/9_12241.txt').readlines()
#print(file[0].split())
for i in file:
    # берем строку из файла и откидываем табуляцию и перевод строки, складываем значения в список (список значений одной строки)
    s = i.split()
    mins = 1e6
    maxs = 0
    n = 0
    # перебираем все значения (7 штук) в списке по порядку
    for j in s:
        # если значение повторяется два раза, запоминаем минимальное и максимальное значения и увеличиваем счетчик таких значений
        if s.count(j) == 2:
            if mins > int(j):
                mins = int(j)
            if maxs < int(j):
                maxs = int(j)
            n += 1
        # если значение в списке не повторяется, это непарный элемент, сохраним его во временной переменной
        elif s.count(j) == 1:
            tmp = j
    # если после перебора списка из 7 значений счетчик n = 6 (3 пары одинаковых значений)
    # и среднее арифметическое минимального и максимального значений меньше непарного значения списка, увеличиваем счетчик строк
    if n == 6 and (mins + maxs) / 2 < int(tmp):
        count += 1

print(count)
