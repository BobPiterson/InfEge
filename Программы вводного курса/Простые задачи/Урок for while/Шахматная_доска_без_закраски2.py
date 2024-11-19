# Программа рисует сетку 8х8
# Использует функции Forward
from turtle import *
delay(0) # ускорить выполнение
# зададим шаг сетки в пикселях
scale = 35

for i in range(14): # повороты линий квадратов
    for a in range(8 - (i + 1) // 2): # рисование линии из нескольких квадратов
        for b in range(4): # рисование одного квадратика
            forward (scale)
            left(90)
        forward(scale)
    left(90)
    forward(scale)

exitonclick()
