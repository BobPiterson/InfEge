from turtle import *

k = 30

tracer(0)

left(90)

for i in range(7):
    forward(10 * k)
    right(120)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(4)

update()
done()
