# Применение сложных сравнений
from random import randrange

a = randrange(1, 7)
b = randrange(1, 7)

print('a = ', a, ', b = ', b)
if a == 1 and b == 1:
    print('a = 1 и b = 1. Вероятность события 1/36')
if a == 1 or b == 1:
    print('a = 1 или b = 1. Вероятность события 1/3')
if a > b or b > a:
    print('a > b или b > a. Вероятность события очень большая')
if a > b and b > a:
    print('a > b и b > a. Событие никогда не произойдет')
if a == b or a != b:
    print('a = b или a != b. Событие произойдет при любых a и b!')
if a >= 3 and b <= 3:
     print('a >= 3 и b <= 3. Событие произойдет с вероятностью 50%')
if a % 2 == 0 or b % 2 == 0:
    print('a четное или b четное')
if a % 2 == 0 and b % 2 == 0:
    print('a четное и b четное')
if a % 2 != 0 and b % 2 != 0:
    print('a нечетное и b нечетное')
if a in range(1, 4) and b in range(4, 7):
    print('a в диапазоне от 1 до 3, b в диапазоне от 4 до 6')
if a >= 3 and b >= 3 or a < 3 and b < 3:
    print('a >= 3 и b >= 3 или a < 3 и b < 3. a и b близки по значению')
if a >= 3 and a <= 5:
    print('a лежит в диапазоне от 3 до 5')




