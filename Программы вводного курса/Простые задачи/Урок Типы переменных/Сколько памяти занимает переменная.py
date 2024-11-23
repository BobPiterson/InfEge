# 1. Импортируем функцию из модуля
from sys import getsizeof, set_int_max_str_digits
# Увеличим максимальную длину целых чисел до 10 000 000 знаков
set_int_max_str_digits(10000000)
# 2. Находим объем занимаемом памяти в Мегабайтах
#print(getsizeof(3 ** 9090001) / (1024 * 1024))
#print(len(str(3 ** 9090001)))
print(getsizeof(123**2057) / 1024)

# Размеры памяти в байтах, занимаемые простыми переменными
print('------ Сравнение занимаемой переменными памяти в байтах ------')
x = 1
print('Целое x = 1                ', getsizeof(x))
x = 1_000_000
print('Целое x = 1_000_000        ', getsizeof(x))
fl = 1.1
print('float fl = 1.1             ', getsizeof(fl))
fl = 1.234567890123456e-50
print('float fl = 1.234567890e-50 ', getsizeof(fl))
s = 'a'
print('Строка s = \'a\'             ', getsizeof(s))
s = 'ab'
print('Строка s = \'ab\'            ', getsizeof(s))
s = 'ab1'
print('Строка s = \'ab1\'           ', getsizeof(s))
s = 'Б'
print('Строка s = \'Б\'             ', getsizeof(s))
s = 'БД'
print('Строка s = \'БД\'            ', getsizeof(s))
s = 'БД1'
print('Строка s = \'БД1\'           ', getsizeof(s))
sp = [1, 2, 3]
print('Список sp = [1, 2, 3]      ', getsizeof(sp))
kor = (1, 2, 3)
print('Кортеж kor = (1, 2, 3)     ', getsizeof(kor))
set1 = {1, 2, 3}
print('Набор set1 = {1, 2, 3}     ', getsizeof(set1))
bl = True
print('boolean bl = True          ', getsizeof(bl))