# ------------------------------  СПИСОК  ------------------------------------
# Напишите программу, которая добавляет вводимые пользователем числа в СПИСОК. 
# Если пользователь ввел число 0, работа программы должна закончиться и вывести полученный список.
print('Чтобы выйти, наберите число 0')
a = []
while True:
    x = int(input('Введите число для добавления в список: '))
    if x == 0:
        print('Получился список: ', a)
        break
    else:
        a.append(x)
