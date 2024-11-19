# Программа для решения квадратного уравнения вида a*x**2 + b*x + c = 0
# коэффициенты a, b, c - заданы, требуется найти корни
# d = b**2 - 4*a*c
# x1 = (-b + sqrt(d)) / (2*a)
# x2 = (-b - sqrt(d)) / (2*a)
from math import sqrt

print('Введите коэффициенты a, b, c, после каждого нажмите \'Enter\'')
a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4*a*c
if d < 0:
    print('Корней нет')
if d == 0:
    print('один корень: ', -b / (2*a))
if d > 0:
    print('два корня, х1 = ', (-b + sqrt(d)) / (2*a), ', x2 = ', (-b - sqrt(d)) / (2*a))
