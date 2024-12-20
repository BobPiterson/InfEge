# Игра Быки и Коровы
# Компьютер задумывает и тайное 4-значное число с неповторяющимися цифрами от 0 до 9
# Игрок должен угадать число, используя подсказки компьютера и несколько попыток
# Игрок вводит вариант числа, компьютер сообщает в ответ, сколько цифр угадано без совпадения с их позициями 
# в задуманном числе (то есть количество коров) и сколько угадано вплоть до позиции 
# в задуманном числе (то есть количество быков).
# Например загадано число: «3219». Игрок сделал попытку: «2310». 
# Результат: две «коровы» (две цифры: «2» и «3» — угаданы на неверных позициях) и один «бык» (одна цифра «1» угадана вплоть до позиции).

from random import randrange
s = set()
n = []
# Генерация случайного 4-х значного числа без повторяющихся цифр
while len(s) < 4:
    n1 = randrange(0, 10) # генерируется одна цифра из четырехзначного числа
    s.add(n1)
    n.append(n1)
    if len(s) < len(n): # если цифра повторилась, то она удаляется и генерируется новая цифра
        n.remove(n1)

#print(n)
count = 0 # Счетчик попыток
print('Для завершения игры введите 0')

while True:
    x = input('Введите четырехзначное число для проверки. Цифры не должны повторяться: ')
    if x == '0':
        print('Игра окончена!')
        break
    count += 1
    t = set()
    for i in range(4):
        t.add(int(x[i]))
    if len(t) != 4:
        print('В числе повторяются цифры! ')
        continue

    cows = 8 - len(s | t) # Объединение множеств с целью определения количества коров
    bulls = 0
    for i in range(4):
        if n[i] == int(x[i]):
            bulls += 1
    if bulls == 4:
        print('ПОЗДРАВЛЯМ! Было загадано число ', str(n[0])+str(n[1])+str(n[2])+str(n[3]), ' Вы отгадали его с ', count, 'попыток!')
        exit()
    cows = cows - bulls
    print('Коров: ', cows, '|   Быков: ', bulls)
        

