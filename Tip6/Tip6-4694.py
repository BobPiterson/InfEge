# https://kompege.ru/variant
import turtle
# поднять кисть
turtle.penup()
# ускорить выполнение
turtle.delay(0)
# задать коэффициент масштабирования и смещение. Смещение необходимо, т.к. начало координат находится в середине окна.
# необходимо подобрать такие параметры, чтобы рисунок вошел в окно, но при этом был максимально большим для удобства подсчета.
coefficient = 60
offset = 300
# нарисовать сетку
for x in range(0, 10):
    for y in range(-10, 10):
        turtle.goto(x * coefficient, y * coefficient)
        turtle.dot(3)

# вернуться в начало рисунка и развернуть исполнителя для движения вверх
turtle.goto(0, 0 - offset)
# повернуть вдоль положительного направления оси ординат
turtle.left(90)
# опустить кисть
turtle.pendown()

# Выполнить задание
for i in range(7):
    turtle.forward(10 * coefficient)
    turtle.right(120)

# не закрывать окно, пока не сделал по нему клик мышкой
turtle.exitonclick()

# ответ: 38