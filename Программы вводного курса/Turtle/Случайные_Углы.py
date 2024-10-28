import turtle
from random import randrange
turtle.delay(0)
turtle.dot(10)
for i in range(1000):
    turtle.right(randrange(-180, 180))
    turtle.forward(randrange(-30, 30))

turtle.exitonclick()