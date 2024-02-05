#
import turtle
# поднять кисть
turtle.penup()
# ускорить выполнение
turtle.delay(0)
# задать коэффициент масштабирования и смещение. Смещение необходимо, т.к. начало координат находится в середине окна.
# необходимо подобрать такие параметры, чтобы рисунок вошел в окно, но при этом был максимально большим для удобства подсчета.
coefficient = 30
# нарисовать сетку
for x in range(0, 20):
    for y in range(-14, 15):
        turtle.goto(x * coefficient, y * coefficient)
        turtle.dot(3)

# вернуться в начало рисунка и развернуть исполнителя для движения вверх
turtle.goto(0, 0)
# повернуть вдоль положительного направления оси ординат
turtle.left(90)
# замедлить выполнение
turtle.delay(10)
# опустить кисть
turtle.pendown()

# Выполнить задание
for i in range(2):
    turtle.forward(5 * coefficient)
    turtle.left(90)
    turtle.back(13 * coefficient)
    turtle.left(90)
# поднять кисть
turtle.penup()

turtle.back(10 * coefficient)
turtle.right(90)
turtle.forward(9 * coefficient)
turtle.left(90)

# опустить кисть
turtle.pendown()
for i in range(2):
    turtle.forward(11 * coefficient)
    turtle.right(90)
    turtle.forward(7 * coefficient)
    turtle.right(90)

# не закрывать окно, пока не сделал по нему клик мышкой
turtle.exitonclick()

# ответ: 170