# https://inf-ege.sdamgia.ru/problem?id=60254
def proga(s: str) -> int:
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            # Согласно условия задачи, меняем ТОЛЬКО ПЕРВОЕ ВХОЖДЕНИЕ СЛЕВА, для этого третьим параметром указываем "1"
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    summa = 0
    for i in s:
        summa = summa + int(i)
    #if summa == 64: print('s =', s, 'summa =', summa)
    return summa

for n in range(4, 1000):
    s = '5' + '2' * n
    if proga(s) == 64:
        print(n)