# В задаче есть подвох: в первой строке стоит число 6720, которое учитывается в рассчетах троек наравне с остальными
# (можно принять это число за количество строк в файле, но тогда результат будет неверным)
f = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/17_12249.txt').read().split()
max_el = 0
for i in range(0, len(f)):
    if int(f[i]) > max_el and len(f[i]) == 5 and f[i][-1:] == '3':
        max_el = int(f[i])
#print(max_el)

count = 0
max_sum = 0
for i in range(0, len(f)-2):
    if (f[i][-1:] == '3' or f[i+1][-1:] == '3' or f[i+2][-1:] == '3') and (int(f[i]) + int(f[i+1]) + int(f[i+2]) <= max_el):
        count += 1
        if max_sum < int(f[i]) + int(f[i+1]) + int(f[i+2]):
            max_sum = int(f[i]) + int(f[i+1]) + int(f[i+2])

print(count, max_sum)