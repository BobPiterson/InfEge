# Найти сумму всех элементов с четными индексами (нумерация с нуля) и сумму всех элементов с нечетными индексами, 
# например: исходный список: [9,8,7,6,5,4,3,2,1], сумма элементов с четными индексами: 25, 
# сумма элементов с нечетными индексами: 20.     
# Размер исходного списка и все элементы должны вводиться с клавиатуры.
n = int(input('Введите размер списка: '))
a = []
for i in range(n):
    print('Введите ', i, 'элемент списка: ', end='')
    el = int(input())
    a.append(el)
print('Введен список: ', a)

# Решение
sum_chet = 0
for i in range(0, n, 2):
    sum_chet = sum_chet + a[i]

print('Сумма элементов с четными индексами: ', sum_chet, ', сумма элементов с нечетными индексами: ', sum(a) - sum_chet)