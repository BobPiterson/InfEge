# Программа рисует сетку 8х8 без закраски квадратов
from turtle import *
# ускорить выполнение
delay(0)
# зададим шаг сетки
scale = 70
# Зададим смещение центра координат
offset_x = (8 * scale) / 2
offset_y = (8 * scale) / 2
# поднять кисть
penup()
# нарисовать 9 вертикальных линий сетки 8х8
for x in range(9):
    goto (x * scale - offset_x, -offset_y)
    # опустить кисть
    pendown()
    goto (x * scale - offset_x, offset_y)
    # поднять кисть
    penup()
# нарисовать 9 горизонтальных линий сетки 8х8
for y in range(9):
    goto (-offset_x, y * scale - offset_y)
    # опустить кисть
    pendown()
    goto (offset_x, y * scale - offset_y)
   # поднять кисть
    penup()

# не закрывать окно, пока не сделал по нему клик мышкой
exitonclick()
