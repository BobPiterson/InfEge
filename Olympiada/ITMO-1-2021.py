# https://olymp.itmo.ru/files/2023-01/bda5/4b3e/6911832a-9c03-7ff520b01746.pdf
# теория по переводу:
# https://www.yaklass.ru/p/informatika/10-klass/teoreticheskie-osnovy-informatiki-7279404/perevod-drobnoi-chasti-chisla-iz-odnoi-sistemy-schisleniia-v-druguiu-6593586
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
def change_10_to_Q(number: str, q: int) -> str:
    alp = "0123456789ABCDEF"
    # Сохраним круглое число, соответствующее по количеству разрядов с исходным числом
    # сперва из длины исходного числа вычтем два символа: '0.'
    len_s = 10 ** (len(number) - 2) # длина дробной части постоянна
    number = int(number[2:])
    s = ''
    i = 0
    # Цикл, пока дробная часть (представленная в целом виде) не равна 0
    while number:
        # Умножаем дробную часть на показатель системы счисления
        # и сохраняем целую часть в s1
        s1 = number * q // len_s
        # сохраняем дробную часть в целом виде
        number = number * q - s1 * len_s
        s += alp[s1]
        i += 1
        # запасной выход, если дробная часть бесконечной длины
        if i == 500:
            break
    return '0.' + s

# def change_Q_to_10(number, q):
#     number = number[2:]
#     len_s = len(number)
#     summa = 0
#     for i in range(len_s):
#         summa = summa + int(number[i],q) / q**(i + 1)
#     return summa

slag1 = format(8 ** 13 / (int('1000', 16) ** 13), '.117f')  # заранее определена длина дробной части - 117 значащих цифр
slag2 = format(4 ** 7 / (int('100', 16) ** 7), '.117f')
slag3 = format(2 ** 2 / (int('10', 16) ** 2), '.117f')
res = summa_in_string(slag1, slag2)
res2 = summa_in_string(res, slag3)
print('Результат суммы в десятичной системе:', res2)
print('Результат суммы в шестнадцатиричной системе:', change_10_to_Q(res2, 16))
