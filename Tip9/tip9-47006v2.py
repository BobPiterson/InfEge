f = open("C:/Users/vngorlachev/Documents/15.Материалы ЕГЭ/скаченные файлы/107_9.txt").readlines()
#print(f[0].split()[0])
#print(len(f))
count = 0
# Перебираем все строки в файле
for i in range (0, len(f)):
    # составляем список, состощий из одной строки файла
    line = []
    for k in range(4):
         line.append(int(f[i].split()[k]))
    # сортируем список по возрастанию
    sorted_line = sorted(line)
    # проверяем, что два минимальных числа в сумме больше максимального, значит составить треугольник возможно
    if sorted_line[0] + sorted_line[1] > sorted_line[3]:
        count += 1

print('count = ', count)



