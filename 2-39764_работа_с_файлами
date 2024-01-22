# Назовём тройкой три идущих подряд элемента последовательности. Определите количество троек чисел таких, которые могут являться 
# сторонами прямоугольного треугольника. В ответе запишите два числа: сначала количество найденных троек, 
# а затем  — максимальную сумму элементов таких троек. Если таких троек не найдётся  — следует вывести 0 0.
#
#
count = 0
maxsumma = 0
n = []
with open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/Новый план/17.txt') as file:
    for line in file:
        n.append(int(line))
#print(len(n), n[len(n) - 1])
for i in range(0, len(n)-2):
    if (n[i] ** 2 + n[i + 1] ** 2 == n[i + 2] ** 2) or \
    (n[i] ** 2 + n[i + 2] ** 2 == n[i + 1] ** 2) or \
    (n[i + 1] ** 2 + n[i + 2] ** 2 == n[i] ** 2):
        count += 1
        maxsumma = max(maxsumma, n[i] + n[i + 1] + n[i + 2])
print(count, maxsumma)

