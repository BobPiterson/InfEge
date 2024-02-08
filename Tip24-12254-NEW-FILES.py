#
s = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/24_12254.txt').read()
max_len = 0
i = 0
count = 0
# Обозначение цепочки
link = False
while i < len(s)-5:
    # Проверяем окончание цепочки R-S-Q-R-S
    if s[i] == 'R' and s[i + 1] == 'S' and s[i + 2] == 'Q' and s[i + 3] == 'R' and s[i + 4] == 'S' and s[i + 5] != 'Q':
        count = count + 5
        i += 5
        link = False # Найдено окончание цепочки
        if max_len < count:
            max_len = count
        count = 0
    # Проверяем окончание цепочки R-S-Q-R
    elif s[i] == 'R' and s[i + 1] == 'S' and s[i + 2] == 'Q' and s[i + 3] == 'R' and s[i + 4] != 'S':
        count = count + 4
        i += 4
        link = False # Найдено окончание цепочки
        if max_len < count:
            max_len = count
        count = 0
    # Проверяем окончание цепочки R-S-Q
    elif s[i] == 'R' and s[i + 1] == 'S' and s[i + 2] == 'Q' and s[i + 3] != 'R':
        count = count + 3
        i += 3
        link = False # Найдено окончание цепочки
        if max_len < count:
            max_len = count
        count = 0

    # Проверяем длинное начало цепочки S-Q-R-S-Q
    elif s[i] == 'S' and s[i + 1] == 'Q' and s[i + 2] == 'R' and s[i + 3] == 'S' and s[i + 4] == 'Q' and link == False:
        count = count + 2
        i += 2
        link = True # Найдено начало цепочки
    # Проверяем длинное начало цепочки Q-R-S-Q
    elif s[i] == 'Q' and s[i + 1] == 'R' and s[i + 2] == 'S' and s[i + 3] == 'Q' and link == False:
        count = count + 1
        i += 1
        link = True # Найдено начало цепочки
    # Проверяем начало или продолжение цепочки R-S-Q
    elif s[i] == 'R' and s[i + 1] == 'S' and s[i + 2] == 'Q':
        count = count + 3
        i += 3
        link = True # Найдено начало цепочки
    else:
        i += 1

print(max_len)