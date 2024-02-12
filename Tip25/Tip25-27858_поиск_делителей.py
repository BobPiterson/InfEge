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
    for i in range(1, a + 1):
        if a % i == 0:
            s.add(i)
    return len(s)

for i in range(x, y + 1):
    count = deliteli(i, s)
    s = set()
    if count >= maxcount:
        maxcount = count
        number = i

print(maxcount, number)


