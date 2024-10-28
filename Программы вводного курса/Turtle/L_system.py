import turtle

rules = {'1': '11', '0': '1[0]0'}

steps = 7
sequence = '0'

for i in range(steps):
    sequence = ''.join(rules[c] if c in rules else c for c in sequence)

line_len = 8
branch_color = 'black'
leaf_color = 'green'
angle = 45
stack = []

turtle.screensize(500, 500)
turtle.penup()
turtle.setpos(0, -500)
turtle.speed(0)
turtle.seth(90)
turtle.color(branch_color)
turtle.pendown()

for c in sequence:
    if c == '0':
        turtle.color(leaf_color)
        turtle.forward(line_len)
        turtle.color(branch_color)
    elif c == '1':
        turtle.forward(line_len)
    elif c == '[':
        stack.append((turtle.pos(), turtle.heading()))
        turtle.left(angle)
    elif c == ']':
        turtle.penup()
        pos, h = stack.pop()
        turtle.setpos(*pos)
        turtle.seth(h)
        turtle.right(angle)
        turtle.pendown()

turtle.penup()
turtle.setpos(1000, 1000)
turtle.exitonclick()
