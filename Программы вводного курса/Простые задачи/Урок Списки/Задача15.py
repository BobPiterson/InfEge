# Вывести список, у которого каждый элемент является суммой всех предыдущих элементов исходного списка, 
# например: исходный список: [8,7,6,5,4,3,2,1], полученный список: [8,15,21,26,30,33,35,36].  
# Размер исходного списка и все элементы должны вводиться с клавиатуры.
n = int(input('Введите размер списка: '))
a = []
for i in range(n):
    print('Введите ', i, 'элемент списка: ', end='')
    el = int(input())
    a.append(el)
print('Введен список: ', a)

# Решение
b = []
summa = 0
for i in a:
    summa = summa + i
    b.append(summa)

print('полученный список: ', b)