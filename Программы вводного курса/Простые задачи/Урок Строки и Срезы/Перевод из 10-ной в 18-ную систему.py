# Символы 18-ричной системы: 0 1 2 3 4 5 6 7 8 9 A B C D E F G H
abc = '0123456789ABCDEFGH'
a = 8765
print('Исходное число в десятичной системе: ', a)
result = ''
while a > 0:
    ostatok = a % 18
    ost_symbol = abc[ostatok]
    a = a // 18
    result = result + str(ost_symbol)

result = result[::-1]
print('В 18-ной системе получилось: ', result)
print('Обратное преобразование: ', int(result, 18))