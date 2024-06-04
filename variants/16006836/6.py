from turtle import *

k = 40
tracer(0)

left(90)
for i in range(6):
    forward(7 * k)
    right(90)
    forward(7 * k)
    right(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)

done()
