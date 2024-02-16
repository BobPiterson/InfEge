# https://kompege.ru/variant
# в задании нужно учитывать, что при подсчете длины числа считается знак "-"
# поэтому чтобы правильно определить трехзначное число, нужно его преобразовать в int, взять модуль, преобразвать в str, подсчитать длину
f = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/17_8161.txt').read().split()

max_n = 0
for s in f:
    if len(s) == 3 and max_n < int(s):
        max_n = int(s)
#print(max_n)
count = 0
max_sum = 0
for i in range(len(f) - 1):
    op1 = len(str(abs(int(f[i]))))
    op2 = len(str(abs(int(f[i + 1]))))
    if op1 == 3 and op2 != 3 and (int(f[i]) + int(f[i + 1]) < max_n) or \
    op1 != 3 and op2 == 3 and (int(f[i]) + int(f[i + 1]) < max_n):
        count += 1
        if max_sum < (int(f[i]) + int(f[i + 1])):
            max_sum = int(f[i]) + int(f[i + 1])
print('count = ', count)
print('max_sum = ', max_sum)