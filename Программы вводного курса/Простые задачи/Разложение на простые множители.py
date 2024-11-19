# Программа раскладывает число на простые множители
# тестовое число
#n = 45809893240877
n = 8958346436597367
#n = 3570725
# Создадим список множителей с делителем 1
multipliers = [1]
# Переберем все числа от 2 до корня от искомого числа
tmp = n
for i in range(2, int(n ** (1/2)) + 1):
    while tmp % i == 0 and tmp > 0:
        multipliers.append(i)
        tmp = tmp // i
mul = 1
for i in multipliers:
    mul *= i
#print(mul)
if mul < n:
    multipliers.append(n // mul)

mul = 1
for i in multipliers:
    mul *= i
if mul == n:
    print('Все простые множители числа ', n, ' найдены!')
else:
    print('Ошибка подсчета простых множителей')

print(sorted(multipliers))
#print('Найдено множителей: ', len(multipliers))


