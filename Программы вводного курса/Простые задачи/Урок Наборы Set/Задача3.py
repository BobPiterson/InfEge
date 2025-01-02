# Найти все делители числа, на которые заданное число делится без остатка
# n = 45809893240877  # результат: [1, 43, 392351, 2715289, 16871093, 116757427, 1065346354439, 45809893240877]
n = 116757427   # результат: [1, 43, 2715289, 116757427] - имеется зеркальный делитель "2715289"
# n = 9               # результат: [1, 3, 9]
# Создадим пустой набор для уникальных множителей
multipliers = set()
# Переберем все числа от 1 до корня от искомого числа
for i in range(1, int(n ** (1/2)) + 1):
    if n % i == 0:
        multipliers.add(i)
        # Не забываем сохранять симметричные делители, для этого число делим на найденные делители
        # симметричным называется делитель, который больше корня из заданного числа и в перебор цикла не попадает
        # Обратить внимание: если пользоваться списком, а не набором, в ответе с n=9 получится две цифры "3" 
        multipliers.add(n // i)
print(sorted(multipliers))
print('Найдено делителей: ', len(multipliers))