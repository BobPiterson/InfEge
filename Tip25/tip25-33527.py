x = 101_000_000
y = 102_000_000
#count = 0
#maxcount = 0
#number = 0
s = set()

def deliteli(a):
    # пустой набор
    count_deli = 0
    # перебираем все числа от 2 до заданного числа с шагом 2 (только четные)
    for i in range(2, int(a ** 0.5) + 1, 2):
        # проверяем, является ли число делителем
        if a % i == 0:
            #print('deliteli = ', i)
            # если является, добавляем его в набор
            count_deli += 1
            if count_deli > 3:
                return(-1)
    if count_deli == 3:
        number = a
    else:
        number = -1
    # возвращаем количество четных делителей числа
    return number

for i in range(x, y + 1):
    w = deliteli(i)
    if i % 10000 == 0: print(i)
    if  w > 0:
        print(w)
        s.add(w)

print(s)
