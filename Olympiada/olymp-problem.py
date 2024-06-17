# n = input()
# s = input()
s = '1+1'
#s = '1*4/2+4/8*2*4+8/2*1*2+1+2/2'
#s = '1+1*2/2'
s += '+'    # добавим в конце строки для удобства следующего цикла

# 1. создаем список из слагаемых
c_plus = s.count('+')
string_m = []
for i in range(c_plus):
    j = 0
    string_p = ''
    while s[j] != '+':
        string_p += s[j]
        j += 1
    if len(string_p) < len(s) - 1:
        s = s[len(string_p) + 1:]
    else:
        string_p = s[:-1]
    string_m.append(string_p)
#print(string_m)


#2. вычисляем каждое слагаемое
string_slag = []

for slag in string_m:
    num_div = 1
    num_mul = int(slag[0])
    for j in range(1, len(slag) - 1):
        #print(slag[j], slag[j+1])
        if slag[j] == '*':
            num_mul *= int(slag[j + 1])
            #print(slag[j+1], num_mul)
        if slag[j] == '/':
            num_div *= int(slag[j + 1])
            #print(slag[j+1], num_div)
    string_slag.append(num_mul // num_div % (10**9 + 7))
#print(string_slag)

#3. сумма элементов
summa = 0
for i in string_slag:
    summa += i
print(summa)


