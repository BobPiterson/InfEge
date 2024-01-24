# Найдите количество пятизначных восьмеричных чисел, в которых все цифры различны и никакие две четные или нечетные не стоят рядом.
#
# максимальное пятизначное число в восьмиричной системе - это 77777.
max_decimal = int('77777', 8)
min_decimal = int('7777', 8) + 1
s = set()
count = 0
for i in range(min_decimal, max_decimal):
    octal_number = format(i, 'o')
    for number in octal_number:
        s.add(number)
        if len(s) == 5:
            count += 1
    s = set()
print(count)

