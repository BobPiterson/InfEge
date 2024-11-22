# Программа рисует сетку 8х8, используя Forward
from turtle import *
delay(0) # ускорить выполнение

for i in range(1, 15): # повороты линий квадратов
    for a in range(8 - i // 2): # рисование линии из нескольких квадратов
        for b in range(4): # рисование одного квадратика
            forward (35)
            left(90)
        forward(35)
    left(90)
    forward(35)

exitonclick()
