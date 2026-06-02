# translate_numeric_system
# Для популярных систем исчисления есть встроенные функции:
# - в десятичную из любой системы, указанной в параметре 'base': result = int(number, base)
# - в двоичную: result = bin(number)[2:]
# - в восьмиричную: result = oct(number)[2:]
# - в шестнадцатеричную: result = hex(number)[2:]
# Функция перевода из 10-й в 7-ную систему, подходит для систем с 2-й по 9-ю
def convert_to7(number):
    result = ''
    while number > 0:
        result = str(number % 7) + result
        number = number // 7
    return result

# Функция перевода из 10-ной в произвольную систему исчисления до 36-й.
def convert_to_base(number : int, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    # Проверка на ошибочно заданную систему с номером более 36
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result

# Функция перевода из 16-ной в 10-ную систему счисления.
def convert_to_10(number : str, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = 0
    for i in range(len(number)):
        result = result + digits.find(number[len(number) - i - 1]) * base**i
    return result


# Исходное число в десятиричной системе:
a = 255
base = 16
print('Исходное число в десятичной: ', a)
# с применением универсальной функции, переведем в 20-ричную систему и обратно:
b = convert_to_base(a, base)
print('Получено в : ',str(base),'-ной:', b)
print('Проверка: ', convert_to_10(b, base))
print('Проверка: ', int(b, base))
# print(convert_to7(a))
# print(int(convert_to7(a), 7))
