# https://inf-ege.sdamgia.ru/problem?id=60256
# Функция перевода из 10-ной в произвольную систему исчисления до 36-й.
def convert_10_to_base(number: int, base: int) -> str:
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    # Проверка на ошибочно заданную систему с номером более 36
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result

number = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
print(convert_10_to_base(number, 25).count('0'))