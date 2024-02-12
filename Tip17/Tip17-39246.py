# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 5, а их сумма делится на 7.
# В ответе запишите два числа: сначала количество найденных пар, а затем  — максимальную сумму элементов таких пар.
#
m = []
count = 0
maxsumm = 0
f =  open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/17.txt')
m = f.readlines()
for i in range(len(m)):
    m[i] = int(m[i])
#print(m)
for i in range(len(m)-1):
    if (m[i] % 5 == 0 or m[i+1] % 5 == 0) and (m[i] + m[i+1]) % 7 == 0:
        count += 1
        maxsumm = max(maxsumm, m[i]+m[i+1])
print(count)
print(maxsumm)