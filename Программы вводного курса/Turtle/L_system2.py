import turtle
from random import randint

rules = {'1': '12', '0': '1[0]0'} # правила преобразования
steps = 14                        # количество шагов рекурсии
sequence = '0'                    # аксиома последовательности

# выполнение преобразований по правилам, если в правилах нет, оставляем как есть
for i in range(steps):
    sequence = ''.join(rules[c] if c in rules else c for c in sequence)


line_len = 30          # длина отрезка (одна ветка может состоять из нескольких отрезков)
branch_color = 'black' # цвет ветки
leaf_color = 'green'   # цвет листа
angle = 15             # угол поворота
stack = []             # стек

# ----- инициализация черепахи -----
turtle.tracer(0)
turtle.screensize(500, 500)
turtle.penup()
turtle.setpos(0, -450)
turtle.speed(0)
turtle.seth(90)
turtle.color(branch_color)
turtle.pendown()

width = steps + 1 # ширина ветки
turtle.width(width)
# ----- инициализация черепахи -----

for c in sequence:
    turtle.width(width)
    if c == '0':
        # рисуем лист
        turtle.color(leaf_color)
        turtle.forward(line_len)
        turtle.color(branch_color)
    elif c == '1':
        # рисуем отрезок ветки
        turtle.forward(line_len)
    elif c == '2':
        '''
        В оригинальном дереве Пифагора операция 2 отсутствует.
        1 -> 11 --- стандартная версия (В стандартной версии каждый уровень веток короче в два раза)
        1 -> 12 --- измененная версия  (В измененной версии каждый уровень веток короче в 1.15 раза)
        Операция 2 рисует уменьшенную ветку.
        Сделано для замедления укорачивания веток.
        '''

        turtle.forward(line_len * 0.15)
    elif c == '[':
        width -= 1 # уменьшаем ширину, т.к. переходим на новый уровень веток
        stack.append((turtle.pos(), turtle.heading(), width)) # сохраняем в стек: позицию, направление, ширину
        turtle.left(angle + randint(-15, 15)) # поворот влево с добавлением случайности
    elif c == ']':
        turtle.penup()
        # достаем значения из стека
        pos, h, width = stack.pop()
        turtle.setpos(*pos)
        turtle.right(angle + randint(-15, 15)) # поворот вправо с добавлением случайности
        turtle.pendown()

turtle.penup()
turtle.setpos(1000, 1000)
turtle.update()
turtle.exitonclick()
