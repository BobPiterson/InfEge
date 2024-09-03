s = '12345'
# счетчик
count = 0
# создадим список, в который будем складывать найденные шифры замка для проверки правильности
m = []
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    shifr = x1 + x2 + x3 + x4 + x5
                    if shifr.count('1') == 3:
                        count += 1
                        m.append(shifr)
print(count)
print(m)


