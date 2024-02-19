# https://kompege.ru/variant
def chet(set_num):
    count = 0
    for i in set_num:
        if i % 2 == 0:
            count += 1
    if count == 6:
        #print('chet: ', set_num)
        return True
    else:
        return False

set_t = []
# Примем х за начальное число, у - за конечное
# учитываем, что обязательным промежуточным результатом в траектории вычислений должно быть число 20, а число 16 нужно избегать
def f(x, y):
    global set_t
    set_t.append(x)
    #if len(set_t) > 12 and len(set_t) < 14: print(set_t)
    # Если перепрыгнули число 25 выйдем из функции и вернем 0
    if x > y:
        set_t = []
        return 0
    # Если дошли до конца траектории, вернем 1 (работает вместо счетчика) чтобы посчитать количество возможных программ
    if x == y:
        if len(set_t) > 10 and len(set_t) < 24: print(set_t)
        if chet(set_t):
            return 1
    # Если не выполняются предыдущие условия, идем дальше всеми возможными командами
    return f(x + 1, y) + f(x + 3, y) + f(x + 5, y)

a1 = f(3, 25)
print(a1)



