def convert_to3(number):
    result = ''
    while number > 0:
        result = str(number % 3) + result
        number = number // 3
    return result

#print(convert_to3(8000), int(convert_to3(8000), 3))

for x in range (2031):
    s = convert_to3(3 ** 100 - x)
    if s.count('0') == 5:
        print(x)