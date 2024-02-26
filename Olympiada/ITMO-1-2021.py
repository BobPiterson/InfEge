# https://olymp.itmo.ru/files/2023-01/bda5/4b3e/6911832a-9c03-7ff520b01746.pdf

# функция сложения больших чисел десятичных дробей одинаковой длины
def summa_in_string(s1, s2):
    if len(s1) != len(s2):
        print('Длины строк должны совпадать!')
        exit()
    else:
        integ = 0
        summa = ''
        for i in range(len(s1)):
            if s1[::-1][i] != '.':
                integ = int(s1[::-1][i]) + int(s2[::-1][i]) + integ
                summa = str(integ % 10) + summa
                integ = integ // 10
            else:
                summa = '.' + summa
    if integ != 0:
        summa = str(integ) + summa
    return summa

# Функция для преобразования дробной части десятичной дроби в систему счисления q
def change_10_to_Q(number,q):
    number = number[2:]
    s = ''
    len_s = len(number)
    i = 0
    while int(number) != 0:
        s1 = str(int(number) * q // (10 ** (len_s)))
        number = str(int(number) * q - (int(s1) * 10 ** (len_s)))
        if s1 == '10': s1 = 'A'
        if s1 == '11': s1 = 'B'
        if s1 == '12': s1 = 'C'
        if s1 == '13': s1 = 'D'
        if s1 == '14': s1 = 'E'
        if s1 == '15': s1 = 'F'
        s = s + s1
        i += 1
        # запасной выход, если дробная часть бесконечной длины
        if i == 500: return '0.' + s
    return '0.' + s

# def change_10_to_Q_int(number,q):
#     s = ''
#     i = 0
#     while number % 1 != 0:
#         drob = number % 1 * q
#         s1 = str(int(drob - drob % 1))
#         if drob - drob % 1 == 10: s1 = 'A'
#         if drob - drob % 1 == 11: s1 = 'B'
#         if drob - drob % 1 == 12: s1 = 'C'
#         if drob - drob % 1 == 13: s1 = 'D'
#         if drob - drob % 1 == 14: s1 = 'E'
#         if drob - drob % 1 == 15: s1 = 'F'
#         s = s + s1
#         number = (number % 1) * q
#         i += 1
#         if i == 500: return '0.' + s
#     return '0.' + s

# def change_Q_to_10(number, q):
#     number = number[2:]
#     len_s = len(number)
#     summa = 0
#     for i in range(len_s):
#         summa = summa + int(number[i],q) / q**(i + 1)
#     return summa

slag1 = format(8**13 / (int('1000',16) ** 13), '.117f') # заранее определена длина дробной части - 117 значащих цифр
slag2 = format(4**7 / (int('100',16) ** 7), '.117f')
slag3 = format(2**2 / (int('10',16) ** 2), '.117f')
res = summa_in_string(slag1, slag2)
res2 = summa_in_string(res, slag3)
print('Результат суммы в десятичной системе:', res2)
print('Результат суммы в шестнадцатиричной системе:', change_10_to_Q(res2, 16))