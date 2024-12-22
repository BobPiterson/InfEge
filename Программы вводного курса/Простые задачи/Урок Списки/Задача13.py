# Вывести список, у которого удален каждый третий элемент, 
# например: исходный список: [10,20,30,40,50,60,70,80], полученный список: [10,20,40,50,70,80]  
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
for i in range(n):
    if (i + 1) % 3 == 0:
        continue
    b.append(a[i])
    
print('полученный список: ', b)