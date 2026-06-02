# translate_numeric_system
# Для популярных систем исчисления есть встроенные функции:
# - в десятичную из любой системы, указанной в параметре 'base': result = int(number, base)
# - в двоичную: result = bin(number)[2:]

# Функция перевода из 10-ной в произвольную систему исчисления до 36-й.
def convert_to_164(number : int, base):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789!@#$%^&*()_+-=[]{}|;:\'",./<>?`~\\\n\t '
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result

# Функция перевода из 164-ной в 10-ную систему счисления.
def convert_to_10(number, base):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789!@#$%^&*()_+-=[]{}|;:\'",./<>?`~\\\n\t '
    # Проверка на ошибочно заданную систему с номером более 36
#    if base > len(digits): return None
    result = 0
    for i in range(len(number)):
        result = result + digits.find(number[len(number) - i - 1]) * base**i
    return result

#a = ')'
base = 164
#print('Исходное число: ', a)
# с применением универсальной функции, переведем в 164-ричную систему и обратно:
#b = convert_to_10(a, base)
b = 2
print('Получено: ', b)
print('Проверка: ', convert_to_164(b, base)
)
