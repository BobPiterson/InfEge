# https://inf-ege.sdamgia.ru/problem?id=60248
import turtle
koef = 30
turtle.tracer(0)
turtle.up()
for x in range(-10, 10):
    for y in range(-10, 10):
        turtle.goto(x * koef, y * koef)
        turtle.dot(3)

turtle.goto(-300, -300)
turtle.down()
turtle.left(90)
for i in range(2):
    turtle.forward(10 * koef)
    turtle.right(90)
    turtle.forward(18 * koef)
    turtle.right(90)
turtle.up()
turtle.forward(5 * koef)
turtle.right(90)
turtle.forward(7 * koef)
turtle.left(90)
turtle.down()
for i in range(2):
    turtle.forward(10 * koef)
    turtle.right(90)
    turtle.forward(7 * koef)
    turtle.right(90)




turtle.update()
turtle.done()