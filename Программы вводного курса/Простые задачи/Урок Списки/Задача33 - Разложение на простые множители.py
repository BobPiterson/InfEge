import time
# Разложить число на простые множители, т.е. все множители должны быть простыми числами
# Проверка: Если перемножить все простые множители числа, получим само число
# n = 45809893240877        # результат: [1, 43, 392351, 2715289]
n = 458098932408778647    # результат: [1, 3, 3, 3, 7, 2423803875178723] - имеется зеркальный множитель
# n = 2423803875178723      # результат: [1, 2423803875178723] - Исходное число - простое!
# n = 6661                  # результат: [1, 6661] - Исходное число было простым числом!
# n = 44100                 # результат: [1, 2, 2, 3, 3, 5, 5, 7, 7]
# n = 256                   # результат: [1, 2, 2, 2, 2, 2, 2, 2, 2]
# n = 48                    # результат: [1, 2, 2, 2, 2, 3]
#n = 12                      # результат: [1, 2, 2, 3]
# n = 2**5 * 3**6 * 5**8 * 7**9
# Создадим список множителей с 1
start_time = time.time() 
multipliers = [1]
tmp = n
# Перебираем диапазон всех возможных делителей от 2 до корня от искомого числа
for i in range(2, int(n ** (1/2)) + 1):
    while tmp % i == 0:
        multipliers.append(i)
        tmp = tmp // i

# Проверяем, не забыт ли зеркальный множитель. Он появляется из-за того, что мы перебираем не все возможные множители, 
# а только до корня из самого числа. Зеркальный множитель всегда больше этого корня:
mul = 1
for i in multipliers:
    mul = mul * i
if mul < n:
    multipliers.append(n // mul)

stop_time = time.time() 
exec_time = stop_time - start_time
print('Затраченное время: ', exec_time, 'sec')
print(sorted(multipliers))