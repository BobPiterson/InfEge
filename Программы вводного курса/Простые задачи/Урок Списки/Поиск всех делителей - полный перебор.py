# Найти все делители заданного числа полным перебором. 
# делителем называется число, на которое заданное число делится без остатка,
# например, делителями числа 12 являются числа 1, 2, 3, 4, 6 и 12.
# проверка: 12 / 1 = 12, 12 / 2 = 6, 12 / 3 = 4, 12 / 4 = 3, 12 / 6 = 2, 12 / 12 = 1
n = 116757427
# Переберем все числа от 1 до самого числа
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
