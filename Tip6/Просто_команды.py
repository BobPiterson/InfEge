import turtle
#turtle.shape("turtle")
turtle.dot(5)

# рисование окружности радиуса r
# поднять кисть
turtle.penup()
r = 120
# сместиться вверх на высоту радиуса
turtle.setheading(90)
turtle.forward(r)
# опустить кисть
turtle.pendown()
turtle.left(90)
turtle.circle(r)

# поднять кисть
turtle.penup()
# ускорить выполнение
turtle.delay(0)
# задать коэффициент масштабирования и смещение. Смещение необходимо, т.к. начало координат находится в середине окна.
# необходимо подобрать такие параметры, чтобы рисунок вошел в окно, но при этом был максимально большим для удобства подсчета.
coefficient = 38
#offset = 300

# смещение в левый нижний угол экрана
turtle.goto(-760, -382)

# опустить кисть
turtle.pendown()
# рамка по всему экрану размером 1516х770
turtle.forward(1516)
turtle.left(90)
turtle.forward(770)
turtle.left(90)
turtle.forward(1516)
turtle.left(90)
turtle.forward(770)
turtle.left(90)

# поднять кисть
turtle.penup()
# нарисовать сетку
for x in range(-19, 20):
    for y in range(-9, 10):
        turtle.goto(x * coefficient, y * coefficient)
        turtle.dot(3)

# не закрывать окно, пока не сделал по нему клик мышкой
turtle.exitonclick()