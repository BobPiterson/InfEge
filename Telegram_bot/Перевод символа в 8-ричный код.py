
c = input('Введите строку: ')
a = ''
for i in c:
    tmp = oct(ord(i))[2:]
    while len(tmp) < 3:
        tmp = '0' + tmp
    a = a + '\\' + tmp
print(a)
