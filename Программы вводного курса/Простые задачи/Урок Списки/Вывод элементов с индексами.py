# вывод элементов с индексами
a = [3,6,2,7,3,9]
print('Задан список: ', a)
print('a[0] = ', a[0])
print('последний элемент = ', a[-1]) # первый элемент с конца
for i in range(len(a)):
    print('индекс i =', i , '    a[i] =', a[i])
