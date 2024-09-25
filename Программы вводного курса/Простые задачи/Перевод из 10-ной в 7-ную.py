# Программа для перевода числа из 10-ной в 7-ную систему счисления
a = 9999
print('Исходное число в десятичной системе: ', a)
result = ''
while a > 0:
    ostatok = a % 7
    a = a // 7
    result = result + str(ostatok)

result = result[::-1]
print('В 7-ной системе получилось: ', result)
print('Обратное преобразование: ', int(result, 7))