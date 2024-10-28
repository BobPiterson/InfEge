from turtle import *

delay(0)
# ширина пера
width(2)
# цвет пера и цвет закраски
pencolor('red')

running = True
while running: # пока не закончилась
    print('Выберите номер фигуры: \n \
        1. Треугольник\n \
        2. Квадрат\n \
        3. Пятиугольник\n \
        4. Шестиугольник\n \
        5. Семиугольник\n \
        6. Восьмиугольник\n \
        7. Пятиконечная звезда\n \
        8. Звезда № 1\n \
        9. Звезда № 2\n \
        10. Звезда № 3\n \
        11. Выход \n')
    choice = int(input())
    penup()
    goto(-100, -100)
    pendown()

    if choice == 1:
        corner = 360 / 3
        repeat = 3
        length = 400
    elif choice == 2:
        corner = 360 / 4
        repeat = 4
        length = 350
    elif choice == 3:
        corner = 360 / 5
        repeat = 5
        length = 300
    elif choice == 4:
        corner = 360 / 6
        repeat = 6
        length = 250
    elif choice == 5:
        corner = 360 / 7
        repeat = 7
        length = 250
    elif choice == 6:
        corner = 360 // 8
        repeat = 8
        length = 200
    elif choice == 7:
        corner = 144
        repeat = 9
        length = 300
    elif choice == 8:
        corner = 145
        repeat = 72
        length = 300
    elif choice == 9:
        corner = 170
        repeat = 36
        length = 300
    elif choice == 10:
        corner = 175
        repeat = 72
        length = 300
    else:
        running = False


    for i in range(repeat):
        forward(length)
        left(corner)
exitonclick()