# https://inf-ege.sdamgia.ru/problem?id=60265
# Пусть x - начало траектории, y - конец
def f(x, y):
    if x > y or x == 11:
        return 0
    if x == y:
        return 1
    return(f(x + 1, y) + f(x * 2, y) + f(x ** 2, y))

print(f(2, 20))