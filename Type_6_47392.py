# Type 6 № 47392

from turtle import *

k = 40
tracer(0)
left(90)

for i in range(6):
    forward(10 * k)
    right(60)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(3)

update()
done()
