from turtle import *

k = 40
tracer(0)

left(90)
right(180)
forward(2 * k)
right(90)
forward(40 * k)
right(90)
forward(2 * k)

for i in range(4):
    right(180)
    circle(5 * k, -180)

up()
for x in range(-50, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)

update()
done()

