# переберем все числа от 0 до 255
for n in range(0, 256):
    b = bin(n)[2:]
    # дополним впереди незначащими нулями
    while len(b) < 8:
        b = "0" + b
    # заменим все "0" на "1" , а "1" на "0" и запишем в переменную s
    s = ''
    for i in b:
        if i == '0':
            i = '1'
        else:
            i = '0'
        s = s + i
    d = int(s, 2)
    if d - n == 111:
        print (n)