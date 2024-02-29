# https://inf-ege.sdamgia.ru/problem?id=60251
# Файл электронной таблицы содержит в каждой строке семь натуральных чисел
# Найти количество строк таблицы, для которых выполнены оба условия:
# 1) в строке есть два числа, каждое из которых повторяется дважды,
# остальные числа различны.
# среднее арифметическое всех повторяющихся чисел строке меньше
# среднего арифметического всех ее чисел.

f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/9_2024.txt").readlines()

# счетчик пар повторяющихся чисел в строке
count_repeat = 0
# счетчик строк, удовлетворяющих условию
count_string = 0
# каждая строка - отдельный список. все строки одинаковой длины.
len_string = len(f[0].split())
# пройдем по всем строкам файла
for i in range(len(f)):
    count_repeat = 0
    # сумма всех чисел строки
    summa1 = 0
    # сумма повторяющихся чисел (по одному числу из пары)
    summa2 = 0
    # пройдем по всем числам в строке
    for k in range(0, len_string):
        # и сосчитаем сумму всех чисел строки
        summa1 += int(f[i].split()[k])
        # пройдем по оставшимся числам в строке
        for m in range(k+1, len_string):
            # если первое число = второму числу, далее третьему числу и так до 7 числа
            if f[i].split()[k] == f[i].split()[m]:
                # сосчитаем сумму чисел, образующих одинаковые пары и количество таких пар
                summa2 += int(f[i].split()[m])
                count_repeat += 1
    # посчитаем среднее арифметическое всех чисел (sred1) и среднее арифметическое повторяющихся чисел (sred2)
    sred1 = summa1 / 7
    sred2 = summa2 / 2
    # если в строке найдено 2 повторяющихся пары и выполнено условие 2 в задаче, увеличиваем счетчик подходящих по условиям строк
    if count_repeat == 2 and sred2 < sred1:
        count_string += 1

print(count_string)

