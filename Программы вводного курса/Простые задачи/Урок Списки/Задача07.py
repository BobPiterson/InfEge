# Посчитать и вывести среднее арифметическое всех элементов списка. 
# Удалить все элементы списка, которые не превышают среднее арифметическое. 
# Размер списка и все элементы должны вводиться с клавиатуры.
n = int(input('Введите размер списка: '))
a = []
for i in range(n):
    print('Введите ', i, 'элемент списка: ', end='')
    el = int(input())
    a.append(el)
print('Введен список: ', a)

# Решение
sred = sum(a)/len(a)
print('Среднее арифметическое равно: ', sred)
b = []
for i in a:
    if i > sred:
        b.append(i)
print('полученный список: ', b)