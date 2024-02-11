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
def convert_to(number, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    # Проверка на ошибочно заданную систему с номером более 36
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result

# Исходное число в десятиричной системе:
a = 9999
# с применением универсальной функции, переведем в 20-ричную систему и обратно:
print(convert_to(a, 20))
print(int(convert_to(a, 20), 20))