# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида:
# согласная  + гласная.
# Для выполнения этого задания следует написать программу.

# Перечислим возможные пары: CA, DA, FA, CO, DO, FO
# Правильность работы программы проверяйте на укороченной строке!!!
s = open(r"C:\Users\vngorlachev\Downloads\47228.txt").readline()
maxi = 0
k = 0
s = s.replace('CA', '!')
s = s.replace('DA', '!')
s = s.replace('FA', '!')
s = s.replace('CO', '!')
s = s.replace('DO', '!')
s = s.replace('FO', '!')
for i in s:
    if i == '!':
        k += 1
        maxi = max(maxi, k)
    else:
        k = 0

print('Ответ:', maxi)
# Ответ: 95