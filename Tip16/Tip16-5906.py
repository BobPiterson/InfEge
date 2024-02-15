# https://kompege.ru/variant
import sys
sys.setrecursionlimit(14000)
def f(x, y):
    if x == 0:
        return y + 1
    if y == 0:
        #print(x, y)
        return f(x - 1, 1)
    return f(x - 1, f(x, y - 1))

print(f(3, 8))