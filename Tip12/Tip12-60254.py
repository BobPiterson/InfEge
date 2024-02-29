# https://inf-ege.sdamgia.ru/problem?id=60254
import time
def proga(s: str) -> int:
    time.sleep(10)
    print('до цикла:', s)
    while s.find('52') != -1 or s.find('2222') != -1 or s.find('1122') != -1:
        if s.find('52') != -1:
            s = s.replace('52', '11')
        if s.find('2222') != -1:
            s = s.replace('2222', '5')
        if s.find('1122') != -1:
            s = s.replace('1122', '25')
    print('После цикла', s)
    summa = 0
    for i in s:
        summa = summa + int(i)
    print('summa =', summa)
    return summa

s = '5'
for n in range(4, 10000):
    s = s + '2' * n
    if proga(s) == 64:
        print(n)