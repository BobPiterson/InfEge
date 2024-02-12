# h - номер хода

def f(x, y, h):
    print(x, y, h)
    if h == 3 and x + y >= 84:
        return 1
    elif h == 3 and x + y < 84:
        return 0
    elif x + y >= 84 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x * 3, y, h + 1)  # стратегия победителя
        else:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x * 3, y, h + 1)  # стратегия проигравшего(неудачный ход)
 
for x in range(1, 68):
    if f(x, 16, 1) == 1:
        print("Задача 19:", x)
        break
