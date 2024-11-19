# Программа поиска совершенных чисел
def deliteli(x):
    result = set()
    for i in range(1, int(x ** (1/2)) + 1):
        if x % i == 0:
            result.add(i)
            if i != 1:
                result.add(x // i)
    return result

#print(deliteli(100))
stop = 10000 # верхняя граница диапазона поиска
for x in range(2, stop + 1):
    if x == sum(deliteli(x)):
        print(x, '- Совершенное число!')