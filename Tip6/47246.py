from turtle import *

k = 38
tracer(0)

print((10 + 8 + 6 + 5 + 3 + 1) * 2 + 12)

left(90)
for i in range(4):
    forward(14 * k)
    right(120)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)

update()
done()

