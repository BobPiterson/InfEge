# После каждого элемента исходного списка добавить его удвоенное значение, 
# например: исходный список [5,4,3,2,1], полученный список: [5,10,4,8,3,6,2,4,1,2].       
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
for i in a:
    b.append(i)
    b.append(i * 2)

print('Получен список: ', b)