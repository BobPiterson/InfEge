import turtle as t
from random import random

t.delay(0)
for i in range(10000):
    steps = int(random() * 10)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.exitonclick()