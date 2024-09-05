from turtle import *
# ускорить выполнение
delay(0)
# функция рисования одного квадрата доски с указанием координаты левого нижнего угла квадрата и его размера
def square(offset_x, offset_y, size):
    penup()
    goto (offset_x, offset_y)
    # установить направление движения указателя - вверх
    setheading(90)
    pendown()
    for i in range(4):
        forward(size)
        right(90)

fillcolor("yellow")
# зададим размер квадрата
size = 70
# Зададим смещение центра координат
offset_x = (8 * size) / 2
offset_y = (8 * size) / 2

for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            begin_fill()
            square(-offset_x + x * size, -offset_y + y * size, size)
            end_fill()
        else:
            square(-offset_x + x * size, -offset_y + y * size, size)

# не закрывать окно, пока не сделал по нему клик мышкой
exitonclick()
