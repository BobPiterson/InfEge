# Значение выражения 49^7 + 7^20 − 28? записали в системе счисления с основанием 7.
# Сколько цифр 6 содержится в этой записи?
#
res = 49 ** 7 + 7 ** 20 - 28

def convert_to7(number):
    result = ''
    while number > 0:
        result = str(number % 7) + result
        number = number // 7
    return result

print(convert_to7(res).count('6'))
