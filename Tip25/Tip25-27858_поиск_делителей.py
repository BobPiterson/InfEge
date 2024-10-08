# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [120115; 120200],
# число, имеющее максимальное количество различных натуральных делителей,
# если таких чисел несколько  — найдите максимальное из них.
# Выведите на экран количество делителей такого числа и само число.

x = 120115
y = 120200
# x = 80
# y = 90
count = 0
maxcount = 0
number = 0
s = set()

def deliteli(a, s):
    # перебираем все числа от 1 до заданного числа
    for i in range(1, a + 1):
        # проверяем, является ли число делителем
        if a % i == 0:
            # если является, добавляем его в набор
            s.add(i)
    # возвращаем длину набора, т.е. количество уникальных делителей числа
    return len(s)

# перебираем все числа указанного диапазона
for i in range(x, y + 1):
    # расчитываем количество уникальных делителей. В переменной s передаем набор делителей
    count = deliteli(i, s)
    s = set()
    if count >= maxcount:
        maxcount = count
        number = i

print(maxcount, number)


