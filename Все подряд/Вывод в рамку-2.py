#!/usr/bin/env python3
import random
import time
import shutil

def set_cursor_in_line(n):
    # :param n: Установить курсор на указанное количество линий вверх от курсора
    print(f'\033[{n}F', end='')

x = shutil.get_terminal_size().columns  # ширина терминала
y = shutil.get_terminal_size().lines    # высота терминала

interval = 1 / 5 # Период обновления экрана
for i in range(y - 3):
    # # Наполнение строк в рамке
    # strings = [] # список из строк
    # s = j * ' ' + '0' + (x - j) * ' ' 
    # strings.append(s)

    time.sleep(0.1)    
    print('\u250F' + '\u2501' * (x - 2) + '\u2513') # - верхняя рамка
    print('\u2503', end = '')   # левая граница

    for j in range(x - 2):
#        time.sleep(0.1) 
        for j in range(x - 2):
            print(strings[i][j], end = '') # по индексу обращаемся к нужной строке (первый индекс - номер строки, второй - номер символа в строке)
        print('\u2503')             # правая граница

        print('\u2517' + '\u2501' * (x - 2) + '\u251B') # - нижняя рамка

        set_cursor_in_line(y - 1)
        time.sleep(interval - time.monotonic() % interval)




